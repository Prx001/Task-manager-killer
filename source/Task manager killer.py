"""
MIT License

Copyright (c) 2021 Prx001

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
GitHub repository: https://github.com/Prx001/Task-manager-killer
"""



import ctypes
# The line below is used to hide the console.
# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
# I commented it to give a way to close the program, otherwise there won't be any known way to close the process.
import threading
import win32gui
import pygetwindow as gw
from pynput.mouse import Controller, Button
import time
# The 'admin' library is included in the repository.
# You must put it in the Python directory; Python/Python[version]/Lib/site-packages/{admin.py}
import admin


# This loop is used to grant admin permissions.
# It's in while True loop to keep asking for admin permission if the user denies the access.
# Note that killing the Task manager is not possible without admin privileges.
if not admin.isUserAdmin():
	while True:
		try:
			admin.runAsAdmin()
			break
		except:
			continue

while True:
    # The if statement below notices whenever 'Task manager' becomes the active window.
	if str(win32gui.GetWindowText(win32gui.GetForegroundWindow())) == "Task Manager":
        # Gain some informations about the active window which is Task Manager.
		x = int(gw.getActiveWindow().left)
		y = int(gw.getActiveWindow().top)
		z = int(gw.getActiveWindow().width)
		mouse = Controller()
        # Control the mouse cursor and move it on the × button.
		mouse.position = (x + z - 20, y + 10)
        # Click to close the window
		mouse.click(Button.left, 1)
        # You can also use the code below to close the window, but using mouse is more relieble.
        # window = gw.getActiveWindow()
		# window.close()
    # This time delay (sleep) is used to control the while True to avoid using much CPU
	time.sleep(1)
# You can also put the process in a separated thread:
# def thread():
#     while True:
#     	if str(win32gui.GetWindowText(win32gui.GetForegroundWindow())) == "Task Manager":
#     		# window = gw.getActiveWindow()
#     		# window.close()
#     		x = int(gw.getActiveWindow().left)
#     		y = int(gw.getActiveWindow().top)
#     		z = int(gw.getActiveWindow().width)
#     		mouse = Controller()
#     		mouse.position = (x + z - 20, y + 10)
#     		mouse.press(Button.left)
#     		mouse.release(Button.left)
#     		mouse.click(Button.left, 1)
#     	time.sleep(1)
#
#
# killer_thread = threading.Thread(target=thread)
# killer_thread.start()
# The rest of your code here
