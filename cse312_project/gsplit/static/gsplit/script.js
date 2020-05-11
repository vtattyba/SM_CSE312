function like(x, liked) {
   var likes = document.getElementById(x);
   if (liked == 'False'){
      likes.innerText++;
   }else{
      likes.innerText--;
   }
   document.getElementById(x).innerText = likes.innerText;
}

$(document).ready(()=>{
   let csrfToken = $("input[name=csrfmiddlewaretoken]").val();
   $("#submit-comment").click(function(){
   console.log("working")
     let post_pk = $(this).data('id');
     let serializedData = "comment="+$("input[data-id="+post_pk+"]").val()+"&data_id="+$(this).data('id')
     console.log(serializedData)

   })
 })
