import re
from collections import Counter
import csv
import time
from decimal import Decimal

#各年月の論文タイトルに含まれる単語数のカウント結果を記録するファイルを開く
#fからgをマイナスする
init_year=2018
end_year=1998
f = open("count_word_ratio_"+str(init_year)+".csv",encoding="utf-8")
g = open("count_word_ratio_"+str(end_year)+".csv",encoding="utf-8")

#結果を記録するためのファイルを開く
h_diff = open("diff_ratio_"+str(init_year)+"-"+str(end_year)+".csv","w",encoding="utf-8")

#単語数ファイルの一行目を読み込む
data_f=f.readline()
data_g=g.readline()

#単語と単語数を対応付けた辞書を作るための空リスト
d_f={}
d_g={}

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


#辞書fに含まれる単語の数から辞書gに含まれる単語の数をマイナスする
for k in d_f:
    #辞書kに該当する単語が含まれている場合その数をマイナスする
    if k in d_g:
        num=float(d_f[k])-float(d_g[k])
        h_diff.write(str(k)+","+str(num)+"\n")
    #辞書kに該当する単語が存在しない場合、辞書fの単語をそのまま記載
    #else:
    #    num=int(d_f[k])
    #    h_diff.write(str(k)+","+str(num)+"\n")
    #辞書kに存在するが、辞書fに存在しない単語もあり得るが、今回は考慮しない

#ファイルを閉じる
f.close()
g.close()
h_diff.close()
#終わった表示
print("finish!!")