
# Setup

- Install `uv` to install Python 3.13
- `uv sync`

# Use

- Set ChatGPT key for API: `export OPENAI_API_KEY='ADD YOUR KEY HERE'`
- Build index: `uv run build_index.py` (takes about 10 minutes with the three texts, below)
- Ask question: `uv run qa.py` which will prompt for a question.

## Example
```
(sanskrit_qa) kylepjohnson@Kyles-MacBook-Pro sanskrit_qa % uv run qa.py

Question (blank to quit): I have a problem. My job is not spiritually fulfilling or honorable. Should I leave worldly concerns behind and become a hermit?

Answer:

आपकी समस्या के संदर्भ में, भगवद गीता में यह कहा गया है कि कर्म का त्याग करना सरल नहीं है। विद्वान व्यक्ति भी कर्मों का त्याग नहीं कर सकता ैह। गीता में कहा गया है:

"अविद्याध्यारोपितस्य शेषानुपपत्तेः। न हि तैमिरिकदृष्ट्या अध्यारोपितस्य द्विचन्द्रादेः तिमिरापगमेऽपि शेषः अवतिष्ठते।" (Source: Bhagavad Gītā.txt, [1])

इससे यह स्पष्ट होता है कि कर्मों का त्याग करना केवल एक विकल्प नहीं है, और व्यक्ति को अपने कर्तव्यों का पालन करते हुए ही आत्मा की शुद्धि की ओर बढ़ना चाहिए।

इसके अलावा, गीता में यह भी कहा गया है:

"स्वे स्वे कर्मण्यभिरतः संसिद्धिं लभते नरः।" (Source: Bhagavad Gītā.txt, [3])

इसका अर्थ है कि व्यक्ति को अपने स्वाभाविक कर्मों में लगे रहना चाहिए, क्योंकि उसी में उसकी सिद्धि है।

इसलिए, आपको अपने वर्तमान कार्य को छोड़कर साधु बनने के बजाय, अपने कर्मों को सही तरीके से निभाने पर ध्यान केंद्रित करना चाहिए।

Question (blank to quit):
```

# Texts

All from Wikisource:

- भगवद्गीता (Bhagavad Gītā): https://sa.wikisource.org/wiki/%E0%A4%AD%E0%A4%97%E0%A4%B5%E0%A4%A6%E0%A5%8D%E0%A4%97%E0%A5%80%E0%A4%A4%E0%A4%BE
- ईशावास्योपनिषद् (Īśā Upaniṣad): https://sa.wikisource.org/wiki/%E0%A4%88%E0%A4%B6%E0%A4%BE%E0%A4%B5%E0%A4%BE%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%AF%E0%A5%8B%E0%A4%AA%E0%A4%A8%E0%A4%BF%E0%A4%B7%E0%A4%A6%E0%A5%8D
- విష్ణు సహస్రనామ స్తోత్రము: https://te.wikisource.org/wiki/%E0%B0%B5%E0%B0%BF%E0%B0%B7%E0%B1%8D%E0%B0%A3%E0%B1%81_%E0%B0%B8%E0%B0%B9%E0%B0%B8%E0%B1%8D%E0%B0%B0%E0%B0%A8%E0%B0%BE%E0%B0%AE_%E0%B0%B8%E0%B1%8D%E0%B0%A4%E0%B1%8B%E0%B0%A4%E0%B1%8D%E0%B0%B0%E0%B0%AE%E0%B1%81


# Technical considerations

- `build_index.py` uses chunk size of 2000 characters with an overlap of 250. See `RecursiveCharacterTextSplitter()` to adjust this. Short contexts give better detail but run the risk of losing context, and longer contexts vice versa.
- 