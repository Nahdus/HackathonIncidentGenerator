from typing import Union
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, UUID4
from enum import Enum
from connectionManager import ConnectionManager
from ticketcreator import createTicket
from typing import Any,Dict,List
import json




manager = ConnectionManager()
class Action(str,Enum):
    reset = "reset"
    p1  = "p1"
    p2 = "p2"
    p3 = "p3"
    p4 = "p4"
    p5 = "p5"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class TicketPulse(BaseModel):
    nodeid:str
    action:Action

class Ticket(BaseModel):
    nodeid:str
    priority:Action
    description:str


# class NodeInfo(BaseModel):
#     pass

class NodeAttributes(BaseModel):
    health: int
    nodeType: str

class RequestModel(BaseModel):
    networkMap: Dict[UUID4, List[UUID4]]
    nodeCordinate: Dict[UUID4, List[float]]
    nodeAttributes: Dict[UUID4, NodeAttributes]


# class NetworkInfo(BaseModel):
#     networkMap:Dict[UUID4, List[UUID4]]
#     nodeCordinate:Dict[UUID4, List[float]]
#     nodeAttributes:Dict[UUID4, NodeAttributes]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.websocket("/ws/{clientId}")
async def connect(websocket:WebSocket,clientId:str):
    await manager.connect(websocket,clientId)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data,websocket}", client_id)
    except WebSocketDisconnect:
        manager.disconnect(clientId)


@app.post("/pulse/")
async def pulse(ticketPulse:TicketPulse):
    print(ticketPulse)
    if ticketPulse.action=="reset":
        pass
    else:
        ticket = createTicket(ticketPulse.nodeid,ticketPulse.action)
        await manager.broadcast_messsage(json.dumps(ticket))
    return True

@app.post("/heartbeat/")
async def heartBeat(networkInfo:RequestModel):
    await manager.broadcast_messsage((networkInfo.json()))
    return True