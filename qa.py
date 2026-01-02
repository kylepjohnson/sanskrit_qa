import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma


PERSIST_DIR = "chroma_db"
COLLECTION = "hindu_texts"


SYSTEM = """You are a careful Q&A assistant for Hindu texts (Sanskrit and Telugu).
Rules:
- Use ONLY the provided excerpts as evidence.
- If the answer is not supported by the excerpts, say so.
- Quote the relevant lines and cite the source filename for each key claim.
- Answer in the same language as the user's question when possible.
"""


def format_context(docs) -> str:
    parts = []
    for i, d in enumerate(docs, start=1):
        src = d.metadata.get("source", "unknown")
        parts.append(f"[{i}] Source: {src}\n{d.page_content}")
    return "\n\n---\n\n".join(parts)


def main() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY in your environment.")

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vs = Chroma(
        collection_name=COLLECTION,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR,
    )
    retriever = vs.as_retriever(search_kwargs={"k": 6})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    while True:
        q = input("\nQuestion (blank to quit): ").strip()
        if not q:
            break

        docs = retriever.invoke(q)
        context = format_context(docs)

        user = f"""Question: {q}

Excerpts:
{context}

Now answer, following the rules."""
        resp = llm.invoke([{"role": "system", "content": SYSTEM},
                           {"role": "user", "content": user}])
        print("\nAnswer:\n")
        print(resp.content)


if __name__ == "__main__":
    main()
