from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    
    def turn_on(self):
        print("LightBulb: turned on...")
    
    def turn_off(self):
        print("LightBulb: turned off...")


class Fan(Switchable):
    
    def turn_on(self):
        print("Fan: turned on...")
    
    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:

    def __init__(self, l: Switchable) -> None:
        self.client = l
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


if __name__ == '__main__':
    light_bulb = LightBulb()
    fan = Fan()

    switch1 = ElectricPowerSwitch(l=light_bulb)
    switch1.press()
    switch1.press()

    switch2 = ElectricPowerSwitch(l=fan)
    switch2.press()
    switch2.press()