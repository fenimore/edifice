from typing import Callable
import argparse
from dataclasses import dataclass
import time

from gpiozero import LED, Button
from signal import pause


if __name__ == "__main__":
    b14 = Button(14)
    b23 = Button(23)
    b24 = Button(24)

    while True:
        if b24.is_pressed:
            print(f"24! {b14.is_pressed} {b23.is_pressed} {b24.is_pressed}")
            b24.wait_for_release()

        if b23.is_pressed:
            print(f"23! {b14.is_pressed} {b24.is_pressed}")
            b23.wait_for_release()


        time.sleep(1)



@dataclass
class Interface:
    led_pin: int
    button_pin: int
    hold_time: int

    def dispatch(self, func: Callable):
        led = LED(self.led_pin) if self.led_pin else None
        button = Button(self.button_pin, hold_time=self.hold_time)
        if led:
            button.when_pressed = led.on
            button.when_released = led.off
        button.when_held = func


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Buttons")
    parser.add_argument("--clear", action="store_true", default=False)
    args = parser.parse_args()
    logger = logging.getLogger("buttons")
    logger.setLevel("INFO")

    white = Interface(18, 17, 2)
    green = Interface(15, 14, 2)

    def disp(param):
        print(param)
        print("yup")

    green.assign(disp)
    white.assign(disp)

    pause()
