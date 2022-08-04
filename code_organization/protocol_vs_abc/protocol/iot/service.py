import random
import string
from typing import Dict, List
from iot.device import Device
from iot.message import Message


def generate_id(length: int = 8):
    return "".join(random.choices(string.ascii_uppercase, k=length))


class IOTSService:

    def __init__(self) -> None:
        self.devices: Dict[str, Device] = {}

    def register_device(self, device: Device) -> str:
        device.connect()
        device_id = generate_id()
        self.devices[device_id] = device
        return device_id

    def unregister_device(self, device_id: str) -> None:
        self.devices[device_id].disconnet()
        del self.devices[device_id]

    def get_device(self, device_id: str) -> Device:
        return self.devices[device_id]

    def run_program(self, program: List[Message]) -> None:
        print("=====RUNNIG PROGRAM=====")
        for msg in program:
            self.devices[msg.device_id].send_message(msg.msg_type, msg.data)
        print("=====END OF PROGRAM=====")