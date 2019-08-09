from mpg123 import Mpg123, Out123


### Configs ###
COIN_SOUND = 'coin'
BRICK_SOUND = 'brick'
COIN_SOUND_PATH = 'resources/mp3/coin.mp3'
BRICK_SOUND_PATH = 'resources/mp3/brick.mp3'

coin_sound = Mpg123(COIN_SOUND_PATH)
brick_sound = Mpg123(BRICK_SOUND_PATH)
sound_interface = Out123()


def play_sound(sound_type):
	## Choice to use mpg123 os library, or pip library
    # e.g. `os.system('mpg123 -q resources/mp3/coin.mp3 &')`
    if sound_type == COIN_SOUND:
    	sound = coin_sound
    elif sound_type == BRICK_SOUND:
    	sound = brick_sound
    	
	for frame in sound.iter_frames(sound_interface.start):
		sound_interface.play(frame)
