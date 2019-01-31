import eel
from time import sleep
import wiringpi
# measure.py内にあるjs_funcをimportする
from measure import js_func

# 25番ピンをbutton_pin、26番ピンをsignal_pinと名前を付ける
button_pin = 25
signal_pin = 26
# button_timeに0を代入
button_time = 0
# GPIOピンの初期化
wiringpi.wiringPiSetupGpio()

# GPIOを入力モード（0）に設定
wiringpi.pinMode( button_pin, 0 )
# ボタン(button_pin)が押されていない状態でHIGHの状態の場合（プルアップ）、２
# LOWの場合（プルダウン）、１
wiringpi.pullUpDnControl( button_pin, 2 )

# GPIOを出力モード（1）に設定
wiringpi.pinMode( signal_pin, 1 )
# GPIOを入力モード（０）に設定
wiringpi.digitalWrite( signal_pin, 0 )

# main関数の定義
def main():
    # signal_pinの初期値をLOWにしたい
    wiringpi.digitalWrite( signal_pin, 0 )
#     webページを表示させますよ、というeelの表記　main.htmlを表示させる
    eel.init("web")  
    eel.start("main.html")
    
    


"""script when link1 pushed"""
# "@eel.expose" と書くことでjavascript（ウェブページ）からpythonの関数を認識されるようにする
@eel.expose
# javascript(今回はmain.html内のスクリプト)で定義している関数名(link1_click())とそろえること
def link1_click():
# デバッグ用にターミナルにlink1_clicked1と表示させる
    null = 1
    print("link1_clicked%s" % null)

#     breakまで繰り返す
    while True:
     #     signal_pinを1に書き換える
         wiringpi.digitalWrite( signal_pin, 1 )
     #     もしbutton_pinが押されてなければ
         if( wiringpi.digitalRead(button_pin) == 0 ):
          #     ターミナルにLOWと出力
              print("LOW")
          # もしbutton_pinが押されたら
         else:
          #     ターミナルにHIGHと出力
              print("HIGH")
          #     measure.py内のjs_func()を起動する
              js_func('a')
          #     whileループを抜ける
              break

     #     whileを1秒ごとに繰り返す
         sleep(1)

   
    

"""script when link2 pushed"""
@eel.expose
def link2_click(args):
    null = 2
    print(args)
    print("%s" % null)
    return "link2_clicked"

@eel.expose
def link3_click():
    null = 3
    print("link3_clicked%s" % null)
    js_func('mari')

# main()を実行
# この表記の仕組みはよくわからない
if __name__ == '__main__':
     main()