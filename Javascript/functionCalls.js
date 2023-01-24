const ages = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30];
function checkAge(ages, range){
    var leese = Array();
    for (let i = 0; i <= ages.length ; i++) {
        if(ages[i]<=range){
            leese.push(ages[i]);
        }
    }
    return leese;
}
function myFunction(){
    var range = prompt("Enter the upper limit of ages to be displayed: ");
    // console.log(ages.find(checkAge));
    document.getElementById("demo1").innerHTML = checkAge(ages, range);
}

// find() -> returns the value of the first element in the array that satisfies the provided testing function. Otherwise undefined is returned.

function playaudio(){
    var audio = document.getElementById("audio");
    audio.play();
}

let playaudio2 = () => new Audio('https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3').play();

// function Video(src, append) {
//     var v = document.createElement("video");
//     if (src != "") {
//       v.src = src;
//     }
//     if (append == true) {
//       document.body.appendChild(v);
//     }
//     return v;
//   }

// var video = new Video('https://www.youtube.com/watch?v=LKP-vZvjbh8','true');
// video.controls = "controls";
// video.play();

function playVideo(){
    const video = document.createElement('video');
    video.src ='https://archive.org/download/C.E.PriceCatWalksTowardCamera/cat_walks_toward_camera_512kb.mp4';    
    video.controls = true;
    video.muted = false;
    video.height = 240; // in px
    video.width = 320; // in px
    const box = document.getElementById('videoButton');
    // Include in HTML as child of #box
    box.appendChild(video);
    document.getElementById('videoButton1').remove();
}

$('.trigger').on('click', function () {
    $(".video")[0].src += "&autoplay=1";
});