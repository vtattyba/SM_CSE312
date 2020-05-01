function myFunction() {
   document.getElementById('fuck').classList.toggle("fas");
}
function tg(x) {
   var c1 = document.getElementById(x.id)
   c1.classList.toggle("fas");
}

function like(x, liked) {
   var likes = document.getElementById(x);
   if (liked == 'False'){
      likes.innerText++;
   }else{
      likes.innerText--;
   }
   document.getElementById(x).innerText = likes.innerText;
}
