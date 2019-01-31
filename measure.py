import eel
from time import sleep
import csv
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime
import wiringpi as pi
import time
import mcp_adc
import shutil

# def main():
#     # load web file
#     eel.init("web")
#     eel.start("main.html")



#  ----------------------------------------------------   
# 計測のためのpython スクリプト
# ------------------------------------------------------
@eel.expose
def js_func(a):
    # デバッグ用にコンソールにprint
    print("measure.py")
    sleep(5)
    print("measurement start!!")

    # パラメータのセット
    SPI_CE = 0
    # ボーレート
    SPI_SPEED = 1000000
    # 読むチャンネル　回路で決定
    READ_CH0 = 0
    READ_CH1 = 1
    # レファレンス電圧の指定
    VREF = 3.3
     
    # 各パラメータをadcに格納　mcp_adx.mcp3208はmcp_adc.py内の関数なのでいじっていない
    adc = mcp_adc.mcp3208( SPI_CE, SPI_SPEED, VREF )

    # 今日の日付をtodayに、時間をnowに格納
    today = datetime.date.today()
    now = datetime.datetime.now()
    


    # ------------------------------------------------------
    # 保存場所の作成
    # -------------------------------------------------------

    # もしpython-data内に今日の日付のディレクトリがなければ
    if not os.path.exists('python-data/%s' % today):
            print('This is the first experiment today. New repository coreated %s' % today)
            # 今日の日付のディレクトリを作成
            os.mkdir('python-data/%s'% today)
   

    # 今日のディレクトリの中に実験時の時間の名前のcsvファイルを作成する。
    # そのファイルの名前をfmt_nameに代入
    fmt_name = "python-data/{0}/test_{1:%Y%m%d-%H%M%S}.csv".format(today,now)

    print('start collecting data...')





    # ------------------------------------------------------
    # 作製したcsvファイルに一行ずつセンサデータを入力していくスクリプト
    # ------------------------------------------------------

    # open-methodでfmt_nameをひらく
    # open(file location,mode).
    # shorten open-method as "f" 

    with open(fmt_name,'w') as f:
        # i（行）が０から５０まで繰り返す
        for i in range(0,50):
            # 今の時間をnowに代入
            now = datetime.datetime.now()

            # value0 value1にそれぞれセンサデータを代入
            value0 = adc.get_value( READ_CH0 )
            value1 = adc.get_value( READ_CH1 )

            # それぞれのデータの最後に\nを配置し、改行する
            writer = csv.writer(f, lineterminator='\n')

            # 1行目に　i value0 value1をそれぞれのセルに書き込む
            writer.writerow([i,value0,value1])

            # sumpling frequency. もっと頻繁にデータを取りたければここの値を変える
            time.sleep( 0.1 )
    # ファイルの編集が終わればファイルを閉じる。
    f.close()

    print( 'New file has created. Its name is ')
    print(fmt_name)
    # 作製したファイルをweb/data.csvに上書き複製。javascriptでグラフを書く時にここを参照するから
    shutil.copyfile(fmt_name, "/home/pi/Desktop/Ultra-analysis2/web/data.csv")
    print('    ')

    # commands necessary for Google Drive
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)



    # drive内にファイルを作って
    f = drive.CreateFile({'title': "/{0:%Y%m%d-%H%M%S}.csv".format(now), 'mimeType': 'text/comma-separated-values'})
    # コンテンツを複製(多分。必要があれば調べて)
    f.SetContentFile('%s' % fmt_name)
    print('uploading files to Google Drive... ...')
    # google spreadsheetにアップロードします
    f.Upload()

    print('Completed uploading files')
    # serverUp()
    print('Server localhost:8000 built.')
    sleep(1)
   
    # my_javascript_functionにfmt_nameを返して、実行します
    eel.my_javascript_function('%s' % fmt_name)
    
