import utime
from machine import UART, Timer

IDLE = 0
PAUSED = 1
PLAYING = 2


class Player:
    def __init__(self, pin_TX, pin_RX):
        self.uart = UART(1, 9600, tx=pin_TX, rx=pin_RX)
        self.cmd(0x3F)
        self._fadeout_timer = Timer(-1)

        self._volume = 30
        self._fadeout_speed  = 0
        
    def cmd(self, command, parameter=0x00):
        query = bytes([0x7e, 0xFF, 0x06, command,
                       0x00, 0x00, parameter, 0xEF])
        self.uart.write(query)
        
    def _fade_out_process(self):
        new_volume = self._volume - self._fadeout_speed
        if new_volume <=0:
            new_volume = 0
            self._fadeout_timer.deinit()
            self.stop()
        self.volume(new_volume)   
        
    #playback

    def play_track(self, track_id):
        self.cmd(0x03, track_id)

    def play_next(self):
        self.cmd(0x01)

    def play_previous(self):
        self.cmd(0x02)

    def pause(self):
        self.cmd(0x0E)

    def resume(self):
        self.cmd(0x0D)

    def stop(self, *fadeout_ms):
        if fadeout_ms:
            fadeout_ms = int(sorted([500, volume, 3000])[1]) # more than 500ms and less than 3000ms
            fade_out_step_ms = 100
            self._fadeout_speed = self._volume * fade_out_step_ms / fadeout_ms # ten steps per second 
            self._fadeout_timer.init(period=fade_out_step_ms, callback = self._fade_out_process) 
        self.cmd(0x16)

    def loop_track(self, track_id):
        self.cmd(0x08, track_id)

    def loop(self):
        self.cmd(0x19)

    def loop_disable(self):
        self.cmd(0x19, 0x01)
        
    #volume control

    def volume_up(self):
        self._volume += 1
        self.cmd(0x04)

    def volume_down(self):
        self._volume -= 1
        self.cmd(0x05)

    def volume(self, *volume):
        if volume:
            self._volume = int(sorted([0, volume, 30])[1])
            self.cmd(0x06, volume)
        return self._volume

    
    # hardware

    def module_sleep(self):
        self.cmd(0x0A)

    def module_wake(self):
        self.cmd(0x0B)

    def module_reset(self):
        self.cmd(0x0C)
