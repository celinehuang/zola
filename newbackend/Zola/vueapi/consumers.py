from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Profile, Message
import json
from .serializers import MessageSerializer

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = 'zola'
        self.room_group_name = 'chatroom_' + self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        json_data = json.loads(text_data)
        await self.commands[json_data['command']](self, json_data)


    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))

    async def fetch_messages(self, data):
        messages = Message.objects.order_by('-date').all()[:20]
        messages_list = []
        for message in messages:
            messages_list.append({
                'id' : str(message.id),
                'user' : message.user.username,
                'content' : message.content,
                'date' : str(message.datedata)
            })
        content = {
            'command' : 'get_all_messages',
            'messages' : messages_list
        }
        print(content)
        await self.send(text_data=json.dumps(content))

    async def new_message(self, data):
        username = data['username']
        userInstance = Profile.objects.get(username=username)
        if userInstance != None:
            serializer = MessageSerializer(data=data)
            if serializer.is_valid():
                print("yea aight")
                serializer.save(user = userInstance)
            content = {
                'command' : 'new_message',
                'messages' : serializer.data
            }
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type' : 'chat_message',
                    'message' : content
                }
            )

    commands = {
        'fetch_messages' : fetch_messages,
        'new_messages' : new_message
    }