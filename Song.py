# -*- coding: utf-8 -*-
import nltk
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
from nltk.tokenize import word_tokenize
import stop_words
from stop_words import get_stop_words
from nltk.stem.isri import ISRIStemmer
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import os

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def read_from_list(self):
        example = self.lyrics
        tokenized_sents = [nltk.word_tokenize(i) for i in example]
        for i in tokenized_sents:
            as_list = u"" + u", ".join(i) + u""
        return as_list

    def tokenizer(self):
        example = self.lyrics
        #list of list of words
        tokenized_sents = [nltk.word_tokenize(i) for i in example]

        xsd=[]
        for i in tokenized_sents[0]:
            xsd.append(i)
        return xsd



    def stop_words_remove(self):
        doc_a = self.lyrics[0]
        sw = get_stop_words('ar')
        tokens = nltk.word_tokenize(doc_a)
        stopped_tokens = [i for i in tokens if not i in sw]
        s = ''
        for i in stopped_tokens:
            s = s + ' ' + i
        return s



    def steamming(self):
        st = ISRIStemmer()
        lis = self.tokenizer()
        xx=""
        for i in lis:
            xx=xx+' '+(st.stem(i))
        return xx


    def part_of_speeach(self):

        os.environ["JAVA_HOME"] = "/usr/bin/java"
        jar = '/home/ahmad/PycharmProjects/untitled1/stanford-postagger-full-2015-12-09/stanford-postagger.jar'
        model = '/home/ahmad/PycharmProjects/untitled1/stanford-postagger-full-2015-12-09/models/arabic.tagger'
        # model = '/home/ahmad/PycharmProjects/untitled1/stanford-postagger-2011-04-20/models/left3words-wasj-0-18.tagger'
        tagger = StanfordPOSTagger(model, jar)
        tagger.java_options = '-mx4096m'  ### Setting higher memory limit for long sentences

        text = tagger.tag(word_tokenize(self.lyrics[0]))
        s = ''
        for i in text:
            f = i[0] + ' ' + i[1]
            s = s + f + ' / '
        return s

# Writing to FILE
# Use for One time

file = open("testfile.txt", "w")
#12
file.write("ليس العيب في أن نسقط و لكن العيب أن لا تستطيع النهوض ")
#9
file.write("من احب الله ، رأى كل شي جميلا. ")
#8
file.write("الفاشلون يقولون: ان النجاح هو مجرد حظ ")
#10
file.write("لا تبصق في البئر ، فقد تشرب منه يوما. ")
#8
file.write(" يسرنا إعلامكم بإنضمام فروعنا التالية لخدمة عملائنا الكرام  ")
#14
file.write(" رسمياً : ريال مدريد سيواجه بايرن ميونخ في دور الربع النهائي لدوري أبطال أوروبا ")


file.close()

file = open("testfile.txt","r")

#print file.readline()
#
rawsong=str(file.read())

rawsong= unicode(rawsong)

my_song= Song([rawsong])






print ('|IIIIIIIIIIIIII| First Stage |IIIIIIIIIIIIII|\n\n')

print ('\n------- tokenizer ------------\n')

print(my_song.tokenizer())

print ('\n------- read ------------\n')

print (my_song.read_from_list())

print ('\n------- stop words ------------\n')
print(my_song.stop_words_remove())

print ('\n------- steamming ------------\n')
print (my_song.steamming())

print ('\n------- part of speach ------------\n')
print (my_song.part_of_speeach())




print ('\n\n|IIIIIIIIIIIIII| Second Stage |IIIIIIIIIIIIII|\n\n ')

print ('\n------- tokenizer ------------\n')
print(my_song.tokenizer())


print ('\n--------- read ------------\n')
print (my_song.read_from_list())

print ('\n--------- stop words ------------\n')
song_stop_word_removed=[]
song_stop_word_removed.append(my_song.stop_words_remove())
my2 =Song(song_stop_word_removed)
print (my2.stop_words_remove())

print ('\n--------- steamming ------------\n')
steamming=[]
steamming.append(my2.steamming())
my3=Song(steamming)
print (my3.steamming())


print ('\n-------- part of speach ------------\n')
print (my_song.part_of_speeach())




