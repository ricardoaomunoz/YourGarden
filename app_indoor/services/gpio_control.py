from gpiozero import LED, Button


class Gpio_controller():
    def __init__(self):
        self.LIGHT_PIN = LED(17)
    def turn_on(self):
        self.LIGHT_PIN.on()
    def turn_off(self):
        self.LIGHT_PIN.off()
    
