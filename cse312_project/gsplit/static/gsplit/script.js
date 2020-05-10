console.log("loaded")

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

$(document).ready(()=>{

   let csrfToken = $("input[name=csrfmiddlewaretoken]").val();

   $("#submit-comment").click(function(){
   console.log("working")
     let post_pk = $(this).data('id');
     let serializedData = "comment="+$("input[data-id="+post_pk+"]").val()+"&data_id="+$(this).data('id')

     console.log(serializedData)


   })
 })

// document.querySelector('#room-name-input').focus();
// document.querySelector('#room-name-input').onkeyup = function(e) {
//     if (e.keyCode === 13) {  // enter, return
//         document.querySelector('#room-name-submit').click();
//     }
// };
//
// document.querySelector('#room-name-submit').onclick = function(e) {
//     var roomName = document.querySelector('#room-name-input').value;
//     window.location.pathname = '/chat/' + roomName + '/';
};

const roomName = JSON.parse(document.getElementById('room-name').textContent);

        const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/chat/'
            + roomName
            + '/'
        );

        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            document.querySelector('#chat-log').value += (data.message + '\n');
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

        document.querySelector('#chat-message-input').focus();
        document.querySelector('#chat-message-input').onkeyup = function(e) {
            if (e.keyCode === 13) {  // enter, return
                document.querySelector('#chat-message-submit').click();
            }
        };

        document.querySelector('#chat-message-submit').onclick = function(e) {
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInputDom.value = '';
        };