import re
from collections import Counter
import csv
import time

#処理時間計測開始
start=time.time()

#各年の論文タイトルに含まれる単語数の比率をカウント結果を記録するファイルを開く
g = open("count_word_ratio_2018.csv","w",encoding="utf-8")

#カウント用のリストの作成
list_o=[]

#論文数
paper_num=0

#日付
for i in range(1801,1813):
    x=str(i)

    #各年月の論文タイトルのファイルを開く
    f = open("arxiv_"+x+".csv",encoding="utf-8")
    
    #タイトルファイルの一行目を読み込む
    data=f.readline()

    #タイトルファイルに含まれるタイトルを順番に読み込んで処理
    while data:
        #単語をすべて小文字にする
        data=data.lower()
        #単語を空白やコンマで区切って分割
        lists=re.split(r'\s|\,|\.|\(|\)', data)
        #カウント用リストに、読み込んだタイトル単語を追加する
        list_o.extend(lists)
        #タイトルファイルの次の行を読み込む
        data=f.readline()
        #論文数を一つ増やす
        paper_num += 1
    
    #開いたファイルを閉じる
    f.close()
    #各年月が終わったらそれを表示
    print(x+" has been inished!!!")
    
#リストの中にある単語の数をカウントする
count=Counter(list_o)

#単語数を出現順にカウントする
for word, count in count.most_common():
    #単語wordが存在するとき
    if len(word) > 0:
    #print("%s,%d" % (word, count))
        ratio=count/17504
        g.write(str(word)+","+str(ratio)+"\n")


#開いたファイルを閉じる
g.close()
#処理の最初と最後の時間差
elapsed_time=time.time()-start
print("elapsed_time:{0}".format(elapsed_time))
#論文数を表示
print(paper_num)