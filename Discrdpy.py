# coded by loh1na
import sys, Settings
from pypresence import *

def Main():
	print("Welcome to Discord Rich Presence editor\nplease paste a ClientID from your discord developer portal to Settings.py")
	try:
		while True:
			drp = Presence(Settings.Clientid)
			print("starting and creating Rich Presence...")
			drp.connect()
			drp.update(large_text = Settings.large_text, small_text = Settings.small_text, large_image = Settings.image_large)
		
	except DiscordError:
		print("no ClientID found, aborting...")
		sys.exit()

	except KeyboardInterrupt:
		print("ctrl + c pressed, aborting...")
		sys.exit()

if __name__ == '__main__':
	Main()