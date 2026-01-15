"""
LSA, TextRank
"""

# import trafilatura
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from underthesea import sent_tokenize, word_tokenize

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

class TokenizerVietNamese:
    def to_sentences(self, text):
        return sent_tokenize(text)
    def to_words(self, text):
        return word_tokenize(text)

# text = trafilatura.extract(html)
# with open("ex_text.txt", "w", encoding="utf-8") as f:
#     f.write(text)

parser = PlaintextParser.from_string(text, TokenizerVietNamese())
summarizer = LsaSummarizer()
summary = summarizer(parser.document, 10)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("\n".join([str(sentence) for sentence in summary]))