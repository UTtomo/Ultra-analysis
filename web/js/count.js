(function(){
    'use strict';
 
    // measure.htmlのid=timerをtimerと省略する。javascriptではよくやる方法　以下同様
    var timer = document.getElementById('timer');
    var start = document.getElementById('start');
    var caution = document.getElementById('caution')

    // 変数の定義
    var startTime;
    var timeLeft;
    var timeToCountDown = 5 * 1000;
    var timerId;
    // ロードされた状態で見えるか見えないか、ここで決定する
    caution.style.visibility = "visible";
    ifr.style.visibility = "hidden";
    start.style.visibility = "visible";
    

    // 時間を自動的にゲットする関数
    function updateTimer(t) {
        // dに今の日時を代入
        var d = new Date(t);
        // mに時間d内の”分”を取り出し代入
        var m = d.getMinutes();
        // sに時間d内の”秒”を取り出し代入
        var s = d.getSeconds();
        // デバッグ用にconsole.logに秒を表示（一秒多く表示する）
        console.log(s+1);
        // プログラム開始からの秒数をtimer.textContentに代入
        timer.textContent = s+1;
    }

    // カウントダウンをする関数countDown関数を定義
    function countDown() {
        
        // conduct function below after 10 mseconds
        timerId = setTimeout(function(){
            timeLeft = timeToCountDown - (Date.now() - startTime);

            // 秒数によってカウントダウンをとめ、"Start!!"と表示させる
            if (timeLeft < 0){
                // timeLeftがマイナスにならないように0を代入
                timeLeft = 0;
                // timerの表示をStart!!に変更する
                timer.textContent="Start!!"
                
                // setTimeoutで3秒ポーズ
                setTimeout(3000);

                // ifr内にsrc=""内のものを表示
                document.getElementById("ifr").src="https://giphy.com/embed/11T6LuIxeHtJJu"
                // もしifrが隠れているなら表示し、隠れていないなら隠す。
                    if(ifr.style.visibility == "hidden"){
                      ifr.style.visibility = "visible";
                      }else{
                          ifr.style.visibility = "hidden";
                      }
                
                // returnでループを離脱	
                return;
            }
            // updateTimerにtimeLeftを渡す
            updateTimer(timeLeft);
            // ここに入れることで再帰的にcountDownをすることができるようになる。
            countDown();
        },10);
    }

    if (start != null){
     
    // when button start clicked
     start.addEventListener('click',function(){
        
        // cautionが見えているならかくして、隠れているなら見えるようにする
        if(caution.style.visibility == "visible"){
        caution.style.visibility = "hidden";
        }else{
            caution.style.visibility = "visible";
        }
        // startが隠れているなら表示し、表示されているなら隠す
        if(start.style.visibility == "visible"){
            start.style.visibility = "hidden";
            }else{
                start.style.visibility = "visible";
            }
        //  get date and inser it to startTime
        startTime = Date.now();
        // conduct coundDown
        countDown();
        

     });   
    }
})();