from dfplayermini import Player

from time import sleep

music = Player(pin_TX=17, pin_RX=16)

print("set volume")
music.volume(20)

print("start play")
music.play(1)
sleep(2)

print("stop play with fadeout")
music.fadeout(2000)

music.play('next')
sleep(10)

music.pause()
sleep(3)

music.loop()
music.play(2)
sleep(20)

music.module_sleep()