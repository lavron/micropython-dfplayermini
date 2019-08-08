from time import sleep
from machine import UART

class Player:
    def __init__(self, pin_TX, pin_RX):
        self._uart = UART(1, 9600, tx = pin_TX, rx = pin_RX)
        self._cmd(0x3F)

    def _cmd(self, command, parameter=0x00):
        query = bytes([0x7e, 0xFF, 0x06, command,
                            0x00, 0x00, parameter, 0xEF])
        self._uart.write(query)

    def play_track(self, track_id):
        self._cmd(0x03, track_id)
           
    def play_next(self):
        self._cmd(0x01)

    def play_previous(self):
        self._cmd(0x02)
        
    def pause(self):
        self._cmd(0x0E)
        
    def resume(self):
        self._cmd(0x0D)

    def stop(self):
        self._cmd(0x16)

    def loop_track(self, track_id):
        self._cmd(0x08, track_id)

    def loop(self):
        self._cmd(0x19)

    def loop_disable(self):
        self._cmd(0x19, 0x01)

    def volume_up(self):
        self._cmd(0x04)

    def volume_down(self):
        self._cmd(0x05)

    def set_volume(self, volume):
        self._cmd(0x06, volume)

    def module_sleep(self):
        self._cmd(0x0A)

    def module_wake(self):
        self._cmd(0x0B)

    def module_reset(self):
        self._cmd(0x0C)