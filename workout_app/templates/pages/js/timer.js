var counter = 0;
var timeLeft = 10;
var timerActive = false;
var timer;

var timeOfWorkout;
var totalTime = 0;

var setNum = 1;

workoutStarted = false;

function convertSeconds(s) {
    var min = floor(s / 60);
    var sec = s % 60;
    return nf(min, 2) + ":" + nf(sec, 2);
}

function resetTimer() {
    counter = 0;
    timerActive = false;
    setNum = 1;
    timer.html("<span>S" + setNum + "</span> " + convertSeconds(timeLeft - counter));
}

function nextSet() {
    counter = 0;
    timerActive = false;
    setNum = setNum + 1;
    timer.html("<span>S" + setNum + "</span> " + convertSeconds(timeLeft - counter));
    document.getElementById('timer_end').play();
}

function setup() {
    noCanvas();

    timer = select('#timer');
    timer.html("<span>S" + setNum + "</span> " + convertSeconds(timeLeft - counter))

    function timeIt() {

        if (counter == timeLeft) { nextSet(); }

        if (timerActive) {
            counter++;
            timer.html("<span>S" + setNum + "</span> " + convertSeconds(timeLeft - counter))
        }
    }
    setInterval(timeIt, 1000);

    timeOfWorkout = select('#timeOfWorkout');
    timeOfWorkout.html(convertSeconds(totalTime));

    function totalTimeCalc() {
        if (workoutStarted) {
            totalTime++;
            timeOfWorkout.html(convertSeconds(totalTime));
        }
    }
    setInterval(totalTimeCalc, 1000);
}

function keyPressed() {
    if (keyCode === 32) {
        timerActive = !timerActive;
        workoutStarted = true;
    }
    if (keyCode === 82) {
        resetTimer();
    }
}