import time
import urllib.request
from bs4 import BeautifulSoup

start=time.time()#処理時間計測開始

#日付
for i in range(9801,9813):
    x=str(i)

    #保存用CSVファイルを開く
    f=open("arxiv_"+x+".csv","w",encoding="UTF-8")
    #記録先のArxivページを開く。show以下が１ページに表示する論文数/月
    URL="https://arxiv.org/list/cond-mat/"+x+"?show=500"
    req = urllib.request.urlopen(URL)
    #ページのソースの取得
    soup = BeautifulSoup(req, "lxml")

    #ソース内のうち、class_="list-titleタグのテキスト取得
    for title in soup.find_all(class_="list-title"):
    #ソース内のうち、"span", class_="descriptor"タグのテキスト取得
        title.find("span", class_="descriptor").extract()
        titletext=title.text
        #取得したタイトルをstr化する
        title_csv=str(titletext)
        #print(title_csv.strip())
        #.strip()で文章末尾の空白を取り除く
        f.write(title_csv.strip()+"\n")
        
    #各年月のファイルを閉じる
    f.close()

    #20秒間待つ
    time.sleep(20)
    #各年月が終わったらそれを表示
    print(x+" has been finished!")


elapsed_time=time.time()-start#処理の最初と最後の時間差
print("elapsed_time:{0}".format(elapsed_time))