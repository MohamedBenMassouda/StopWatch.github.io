let startTime = 0;
let count_min = 0;
let count_hour = 0;
let start = document.getElementById("start");
let reset = document.getElementById("reset");
let stop = document.getElementById("stop");
let sec = document.getElementById("sec")
let min = document.getElementById("min")
let hour = document.getElementById("hour")

start.addEventListener('click', function () {
    timer = setInterval(function(){
        startTime++;
        if (startTime < 10){
            sec.innerHTML = "0" + startTime
        } else{
            sec.innerHTML = startTime
        }
            
        if (sec.innerHTML > "59"){
            sec.innerHTML = "00";
            startTime = 0;
            count_min++;
            if (count_min < 10){
                min.innerHTML = "0" + count_min
            } else{
                min.innerHTML = count_min
            }
        }
        if (min.innerHTML >"59"){
            min.innerHTML = "00";
            count_min = 0;
            count_hour++;
            if (count_hour < 10){
                hour.innerHTML = "0" + count_hour
            } else{
                hour.innerHTML = count_hour
            }
        }
        if (hour.innerHTML > "23"){
            sec.innerHTML = "00";
            min.innerHTML = "00";
            hour.innerHTML =  "00"
        }
    }, 1000)
})

stop.addEventListener('click', function() {
    clearInterval(timer);
  });

reset.addEventListener("click", () => {
    clearInterval(timer);
    startTime = 0;
    sec.innerHTML = "00"
    min.innerHTML = "00"
    hour.innerHTML = "00";
})



