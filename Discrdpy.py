# coded by loh1na
try:
	import sys, Settings, os
	from pypresence import *
except ImportError:
	print("required module not found, trying to install...")
	os.system('pip install pypresence')
	print("module installed, maybe...")


def Main():
	print("Welcome to Discord Rich Presence editor\nplease paste a ClientID from your discord developer portal to Settings.py")
	try:
		while True:
			drp = Presence(Settings.Clientid)
			print("starting and creating Rich Presence...")
			drp.connect()
			drp.update(state = Settings.large_text, large_image = Settings.image_large)
			try:
				if Settings.usebutton == True:
					drp.update(state = Settings.large_text, large_image = Settings.image_large, buttons = [{"label":f"{Settings.buttontext}", "url":f"{Settings.buttonurl}"}])
				elif Settings.UseSmallText == True:
					drp.update(state = Settings.large_text, large_image = Settings.image_large, details = Settings.small_text)
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

if __name__ == '__main__':
	Main()


