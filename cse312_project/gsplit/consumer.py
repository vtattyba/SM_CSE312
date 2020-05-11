# https://channels.readthedocs.io/en/latest/tutorial/part_2.html
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text_data_json['message'],
                'from': text_data_json['from']
            }
        )

    def chat_message(self, event):
        async_to_sync(self.send(text_data=json.dumps({
            'message': event['message'],
            'from': event['from']
        })))