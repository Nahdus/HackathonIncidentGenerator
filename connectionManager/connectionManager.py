from fastapi import  WebSocket
from threading import Lock
import logging

LOGGER = logging.getLogger(__file__)

class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):

        with cls._lock:
            if cls not in cls._instances:
                print(*args, **kwargs)
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class ConnectionManager(object, metaclass=SingletonMeta):
    def __init__(self):
        LOGGER.info(f"connection Initialized")
        self.active_connections  = {}

    async def connect(self, websocket: WebSocket,client_id:str):
        LOGGER.info(f"{client_id} has connected")
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id:str ):
        del self.active_connections[client_id]
        # self.active_connections.remove(websocket)
    
    async def send_personal_message(self, message: str, client_id:str):
        await self.active_connections[client_id].send_text(message)

    async def broadcast_messsage(self,message:str):
        for key in self.active_connections.keys():
            await self.active_connections[key].send_text(message)

connectionManager = ConnectionManager()