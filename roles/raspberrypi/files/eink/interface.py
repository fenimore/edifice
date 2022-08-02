#!/usr/bin/python3
import sys
import argparse
import logging
from invoke import run
from inky import InkyWHAT

from button import Interface, pause

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Inky command")
    parser.add_argument("--filename", type=str)
    args = parser.parse_args()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO
    )

    inky_display = InkyWHAT("black")

    inky_display.set_border(inky_display.BLACK)

    logging.info("Button Interface")
    white = Interface(18, 4, 1)
    green= Interface(15, 14, 1)
    orange = Interface(None, 23, 1)

    def paint(device):
        logging.info("Painting")
        run("/opt/eink/venv/bin/python3 /opt/eink/eink/main.py --draw --filename /opt/eink/resources/promenade_des_anglais.jpg", hide=False)

    def refresh(device):
        logging.info("Refreshing")
        run("/opt/eink/venv/bin/python3 /opt/eink/eink/main.py --clear", hide=False)

    def f(device):
        print(dir(device))
        print(device)
        logging.info("Orange")

    green.dispatch(f)
    white.dispatch(paint)
    orange.dispatch(refresh)

    pause()
