# coded by loh1na
import sys, Settings, os
from pypresence import *


def Main():
	print("Welcome to Discord Rich Presence editor\nplease paste a ClientID from your discord developer portal to Settings.py")
	try:
		while True:
			drp = Presence(Settings.Clientid)
			print("starting and creating Rich Presence...")
			drp.connect()
			drp.update(state = Settings.large_text, details = Settings.small_text, large_image = Settings.image_large)
			try:
				if Settings.usebutton == True:
					drp.update(buttons = [{"label":f"{Settings.buttontext}", "url":f"{Settings.buttonurl}"}])
			except ServerError:
				print(f"can't found {Settings.buttonurl}, try do add to begin of url https://")
		
	except DiscordError:
		print("\ncan't found ClientID, aborting...")
		sys.exit()

	except KeyboardInterrupt:
		print("\nctrl + c pressed, aborting...")
		sys.exit()

	except DiscordNotFound:
		print("\ncan't find discord on this pc, aborting...")
		sys.exit()
try:
	if __name__ == '__main__':
		Main()
except ImportError:
	print("needed module not found, trying to install needed module")
	os.system('pip install pypresence')
	print("module installed, maybe...")
	if __name__ == '__main__':
		Main()

