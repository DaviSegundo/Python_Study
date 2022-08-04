from iot.devices import Curtains, HueLight, SmartSpeaker
from iot.diagnostics import collect_diagnostics
from iot.message import Message, MessageType
from iot.service import IOTSService


def main() -> None:
    # create a IOT service
    service = IOTSService()

    # create and register a few devices
    hue_light = HueLight()
    speaker = SmartSpeaker()
    curtains = Curtains()

    hue_light_id = service.register_device(hue_light)
    speaker_id = service.register_device(speaker)
    curtains_id = service.register_device(curtains)

    # create a few programs
    wake_up_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, "MD Chefe - Rei Lacoste"),
        Message(curtains_id, MessageType.OPEN),
    ]

    sleep_program = [
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
        Message(curtains_id, MessageType.CLOSE),
    ]

    # run the programs
    service.run_program(wake_up_program)
    service.run_program(sleep_program)

    # collect some diagnostics
    collect_diagnostics(hue_light)


if __name__ == '__main__':
    main()