# Task-manager-killer
A tricky open source script to kill the Task manager.
## About
Task manager killer, is a Python script which uses a simple and funny trick to kill Microsoft Windows Task manager.
Task manager is a very popular tool to monitor all processes in Microsoft Windows.
It's used by almost all Windows users for different purposes such as view RAM usage, CPU usage and so on;
But when it comes to exploit developers, viruses, spywares, and trojans, it's a real badass enemy!
and since it's from Windows itself and located in system32, it's a bit hard to deal with,
it cannot be killed by another process even if it has admin privileges, and hiding your process in Task manager takes
much time and effort and it might not work properly in all Windows versions and computers.
## How does it work?
This simple script, first of all, prompts user to get admin privileges, since this trick is not possible without admin access.
The library to gain the admin access is included in the GitHub repository [here](https://github.com/Prx001/Task-manager-killer/blob/main/Lib/admin.py).
Note that it doesn't gain access silently since it's not possible in Windows, and the user must click on 'Yes' to give the access,
which the script has another trick to almost bypass this.
Then, thanks to 'win32gui' library, it waits for an event in a while loop. Whenever Task manager becomes the active window, it catches it!
Starts to calculate the position of × button of Task manager window, and moves the mouse cursor to it and clicks on it! That's all!
More in the [source code](https://github.com/Prx001/Task-manager-killer/blob/main/source/Task%20manager%20killer.py).
