# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize
import stop_words
from stop_words import get_stop_words
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
sw = get_stop_words('en')
raw = doc_a.lower()
tokens = nltk.word_tokenize(raw)
stopped_tokens = [i for i in tokens if not i in sw]
print(stopped_tokens)