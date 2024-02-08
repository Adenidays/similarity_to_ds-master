import asyncio
import websockets
import json

async def send_message(uri, room_name, message):
    async with websockets.connect(uri + f"/ws/chat/{room_name}/") as websocket:
        data = {'message': message}
        await websocket.send(json.dumps(data))
        response = await websocket.recv()
        print(f"Received response: {response}")


server_uri = "ws://127.0.0.1:8001"

room_name = "example_room"
message_to_send = "Hello, this is a test message!"

asyncio.get_event_loop().run_until_complete(send_message(server_uri, room_name, message_to_send))
