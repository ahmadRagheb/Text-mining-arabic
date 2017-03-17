# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize
example = [u' سرير غير مريح. عدم وجود غلاية ماء...']
tokenized_sents = [nltk.word_tokenize(i) for i in example]
for i in tokenized_sents:
    as_list = u"['" + u"', '".join(i) + u"']"

print as_list
