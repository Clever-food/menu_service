

from fastapi import WebSocket
from src.repository.connection_repo import ConnectionRepo

class ConnectionService:
    def __init__(self, repository: ConnectionRepo):
        self.repository = repository

    async def connect(self, websocket: WebSocket):
        await self.repository.add_connection(websocket)

    def disconnect(self, websocket: WebSocket):
        self.repository.remove_connection(websocket)

    async def broadcast(self, message):
        await self.repository.broadcast(message)