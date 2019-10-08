from dfplayermini import Player

from time import sleep

music = Player(pin_TX=17, pin_RX=16)

music.volume(20)

music.play_track(1)
sleep(10)

music.stop(fadeout_ms = 2000)

music.play_next()
sleep(10)

music.pause()
sleep(3)

music.loop()
music.play_track(2)
sleep(20)

music.module_sleep()