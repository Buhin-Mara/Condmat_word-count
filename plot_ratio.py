import re
from collections import Counter
import csv
import time
from decimal import Decimal

#各年月の論文タイトルに含まれる単語数のカウント結果を記録するファイルを開く

f = open('count_word_ratio_2018.csv',encoding="utf-8")
g = open('count_word_ratio_2017.csv',encoding="utf-8")
h = open('count_word_ratio_2013.csv',encoding="utf-8")
i = open('count_word_ratio_2008.csv',encoding="utf-8")
j = open('count_word_ratio_2003.csv',encoding="utf-8")
k = open('count_word_ratio_1998.csv',encoding="utf-8")

#単語数ファイルの一行目を読み込む
data_f=f.readline()
data_g=g.readline()
data_h=h.readline()
data_i=i.readline()
data_j=j.readline()
data_k=k.readline()

#単語と単語数を対応付けた辞書を作るための空リスト
d_f={}
d_g={}
d_h={}
d_i={}
d_j={}
d_k={}

#ファイルfに含まれる情報を辞書化
while data_f:
    lists=re.split(r'\s|\,|\(|\)', data_f)
    d_f[lists[0]]=lists[1]
    #タイトルファイルの次の行を読み込む
    data_f=f.readline()

#ファイルgに含まれる情報を辞書化
while data_g:
    lists=re.split(r'\s|\,|\(|\)', data_g)
    d_g[lists[0]]=lists[1]
    #タイトルファイルの次の行を読み込む
    data_g=g.readline()

#ファイルgに含まれる情報を辞書化
while data_h:
    lists=re.split(r'\s|\,|\(|\)', data_h)
    d_h[lists[0]]=lists[1]
    #タイトルファイルの次の行を読み込む
    data_h=h.readline()

#ファイルgに含まれる情報を辞書化
while data_i:
    lists=re.split(r'\s|\,|\(|\)', data_i)
    d_i[lists[0]]=lists[1]
    #タイトルファイルの次の行を読み込む
    data_i=i.readline()

#ファイルgに含まれる情報を辞書化
while data_j:
    lists=re.split(r'\s|\,|\(|\)', data_j)
    d_j[lists[0]]=lists[1]
    #タイトルファイルの次の行を読み込む
    data_j=j.readline()

#ファイルgに含まれる情報を辞書化
while data_k:
    lists=re.split(r'\s|\,|\(|\)', data_k)
    d_k[lists[0]]=lists[1]
    #タイトルファイルの次の行を読み込む
    data_k=k.readline()


#ファイルを閉じる
f.close()
g.close()
h.close()
i.close()
j.close()
k.close()

#終わった表示
print("finish!!")

word_input=input()
word=str(word_input)

#2018年の単語比率
if word in d_f:
    print(str(float(d_f[word])))
else :
    print("0")

#2017年の単語比率
if word in d_g:
    print(str(float(d_g[word])))
else :
    print("0")

#2013年の単語比率
if word in d_h:
    print(str(float(d_h[word])))
else :
    print("0")

#2008年の単語比率
if word in d_i:
    print(str(float(d_i[word])))
else :
    print("0")

#2003年の単語比率
if word in d_j:
    print(str(float(d_j[word])))
else :
    print("0")

#1988年の単語比率
if word in d_k:
    print(str(float(d_k[word])))
else :
    print("0")