# -*- coding: utf-8 -*-
from nltk.stem.isri import ISRIStemmer
st = ISRIStemmer()
print (st.stem(u'اعلاميون'))