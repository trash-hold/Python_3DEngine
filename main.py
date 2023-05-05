import engine as e
from gui.gui import GUI

def setup(win_x: int=60, win_y: int=60) -> GUI:
	'''
	Creates GUI with placeholder object
	'''
	#Setting up the engine
	window = e.Window(60,60)
	obj = e.Donut([300, 100])
	window.update_obj(obj.__obj__)

	#Creating gui
	return GUI(window)


if __name__ == "__main__":
	sample_app = setup()
	
	#Place for your code :)

	"""
	settings:
	Window - resolution
	res lock - on/off?
	dark theme - meme

	graphics:
		frame_size - 
		window_size - make cap depending on res???
		camera settings on/off:
			adjust
			center
			z-depth
	"""
