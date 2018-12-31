(function(){
    'use strict';
 
    // include timer start, and caution to js from HTML
    var timer = document.getElementById('timer');
    var start = document.getElementById('start');
    var caution = document.getElementById('caution')

    // definition of valuables
    var startTime;
    var timeLeft;
    var timeToCountDown = 5 * 1000;
    var timerId;

    // caution is the ID of "waiting for pushing button". first, you need to expose it. so set visible

    caution.style.visibility = "visible";

    // define updateTimer function that insert count-timer on the format
    function updateTimer(t) {
        // get date with Date-method
        var d = new Date(t);
        // m is a valuable to strage "minutes"
        var m = d.getMinutes();
        // s is a valuable to strage "seconds"       
        var s = d.getSeconds();
        
        // overwrite countdown-timer 
        timer.textContent = s+1;
    }

    // define countDown function that calculate time and return the value
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