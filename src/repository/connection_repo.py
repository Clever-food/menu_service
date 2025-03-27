from fastapi import WebSocket, WebSocketDisconnect

class ConnectionRepo:
    def __init__(self):
        self.active_connections = []

    async def add_connection(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def remove_connection(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message):
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except WebSocketDisconnect as e:
                print(f"Error sending message: {e}")
                disconnected.append(connection)
        for connection in disconnected:
            self.remove_connection(connection)