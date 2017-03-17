# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize
import stop_words
from stop_words import get_stop_words
doc_a =u"ذهب محمد الى المدرسه على دراجته. هذا اول يوم له في المدرسة"
sw = get_stop_words('ar')
tokens = nltk.word_tokenize(doc_a)
stopped_tokens = [i for i in tokens if not i in sw]


as_list=""
s=''
#normal tokens
for i in stopped_tokens:
    s =s+' '+i
    # print(i)
   # as_list = u"['" + u"', '".join(i) + u"']"+as_list

print s

#stoptokens

# as_list=""
# for i in stopped_tokens:
#     as_list = u"['" + u"', '".join(i) + u"']"+as_list
#
# print as_list

#printed tokens after removing stopwords
# print(stopped_tokens)