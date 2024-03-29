from iot.device import Device
from iot.message import MessageType


class HueLight(Device):

    def connect(self) -> None:
        print("Connecting to Hue Light.")

    def disconnet(self) -> None:
        print("Disconneting Hue Light.")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(f"Hue Light handling message of type {message_type} with data [{data}]")

    def status_update(self) -> str:
        return "hue_light_status_ok"


class SmartSpeaker(Device):

    def connect(self) -> None:
        print("Connecting to Smart Speaker.")

    def disconnet(self) -> None:
        print("Disconneting Smart Speaker.")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(f"Smart Speaker handling message of type {message_type} with data [{data}]")

    def status_update(self) -> str:
        return "smart_speaker_status_ok"


class Curtains(Device):

    def connect(self) -> None:
        print("Connecting to Curtains.")

    def disconnet(self) -> None:
        print("Disconneting Curtains.")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(f"Curtains handling message of type {message_type} with data [{data}]")

    def status_update(self) -> str:
        return "curtains_status_ok"