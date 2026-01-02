import os
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


TEXTS_DIR = Path("texts")
PERSIST_DIR = "chroma_db"
COLLECTION = "hindu_texts"


def load_local_txts() -> list[Document]:
    docs: list[Document] = []
    for p in sorted(TEXTS_DIR.glob("*.txt")):
        text = p.read_text(encoding="utf-8")
        # Minimal metadata; add more later (work, chapter, verse, lang, etc.)
        docs.append(Document(page_content=text, metadata={"source": p.name}))
    return docs


def main() -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("Set OPENAI_API_KEY in your environment.")

    raw_docs = load_local_txts()

    # Simple splitter first; you can replace with verse-aware splitting later.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,      # chars
        chunk_overlap=250,    # chars
    )
    chunks = splitter.split_documents(raw_docs)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    vs = Chroma(
        collection_name=COLLECTION,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR,
    )

    vs.add_documents(chunks)
    print(f"Indexed {len(chunks)} chunks into {PERSIST_DIR!r} / {COLLECTION!r}.")


if __name__ == "__main__":
    main()
