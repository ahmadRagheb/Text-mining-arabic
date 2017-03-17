# -*- coding: utf-8 -*-
import nltk
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize

import os

# java_path = "/usr/local/java"
# os.environ['JAVAHOME'] = java_path
# os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-7-oracle-cloudera/jre"
os.environ["JAVA_HOME"] = "/usr/bin/java"



# Alternatively to setting the CLASSPATH add the jar and model via their path:
jar = '/home/ahmad/PycharmProjects/untitled1/stanford-postagger-2011-04-20/stanford-postagger.jar'
    #model = 'D:\ArabNLP\stanford-postagger-2015-12-09\models\english-left3words-distsim.tagger'
model = '/home/ahmad/PycharmProjects/untitled1/stanford-postagger-2011-04-20/models/left3words-wsj-0-18.tagger'
# model = '/home/ahmad/PycharmProjects/untitled1/english-left3words-distsim.tagger'
tagger = StanfordPOSTagger(model, jar)

tagger.java_options='-mx4096m'          ### Setting higher memory limit for long sentences


text = tagger.tag(word_tokenize(u'أنا تسلقت شجرة'))



s=''
for i in text:
    f=i[0]+' '+i[1]
    s =s+f+' / '
    # print(i)
   # as_list = u"['" + u"', '".join(i) + u"']"+as_list

print s

#print(text)

