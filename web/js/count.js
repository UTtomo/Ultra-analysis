(function(){
    'use strict';
 
    // include timer and start to js from HTML
    var timer = document.getElementById('timer');
    var start = document.getElementById('start');
    var caution = document.getElementById('caution')

    var startTime;
    var timeLeft;
    var timeToCountDown = 5 * 1000;
    var timerId;
    caution.style.visibility = "visible";

    // define updateTimer function that write text on the format
    function updateTimer(t) {
        var d = new Date(t);
        var m = d.getMinutes();
        var s = d.getSeconds();
        console.log(s+1);
        timer.textContent = s+1;
    }

    // define countDown function that count time and return it
    function countDown() {
        
        // conduct function below after 10 mseconds
        timerId = setTimeout(function(){
            timeLeft = timeToCountDown - (Date.now() - startTime);

            // if-method to stop the countDown and alert "Start!!"
            if (timeLeft < 0){
                // adjust time lag
                timeLeft = 0;
                // change to Start!!
                timer.textContent="Start!!"
                // return means exit roop
                return;
            }
            // return time to updateTimer function
            updateTimer(timeLeft);
            // insert here to conduct CountDown repeatedly
            countDown();
        },10);
    }

    if (start != null){
     
    // when button start clicked
     start.addEventListener('click',function(){
        if(caution.style.visibility == "visible"){
        caution.style.visibility = "hidden";
        }else{
            caution.style.visibility = "visible";
        }
        //  get date and inser it to startTime
        startTime = Date.now();
        // conduct coundDown
        countDown();
     });   
    }
})();