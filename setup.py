from cx_Freeze import setup, Executable
import sys

base = None
if (sys.platform == "win32"):
	base = "Win32GUI"

setup(
	name = 'Dota 2 inventory calculator',
	version = '0.1',
	description = 'Represents the sum of your inventory in Dota 2',
	executables = [Executable('main.py')]
)
