# Sequence-FM
This repository hosts Sequence FM (Python+QT5) file manager and related add-ons

![screenshot](https://user-images.githubusercontent.com/29865797/28461483-7baa3056-6e1f-11e7-8063-b3dc414a31fb.jpg)

#Sequence FM v.4 Copyright (c) 2017 JJ Posti <techtimejourney.net>

#This program comes with ABSOLUTELY NO WARRANTY;

#for details see: http://www.gnu.org/copyleft/gpl.html.

#This is free software, and you are welcome to redistribute it under

#GPL Version 2, June 1991″)
_________________________________________

<b>Sequence FM v.4.1:</b>

To use Sequence FM you should have, at least, these installed (Debian base as an example):

sudo apt-get install python-pyqt5 python python3 file-roller

Sequence FM features include, for example:

-Terminal command support. If you write: firefox, albix, vlc (or some other program name) to the address bar and press enter then the program will open up. You can also use other terminal commands like rm -r to remove files or folders. Be cautious with terminal commands and use them only if you know what you are doing.

-Right-click menu.

-Menus, which have functionalities separated to their own sections clearly.

-Navigation bar (with terminal command support, as mentioned above).

-Open archive, compress object, extract object functionality(via file-roller integration).

-Open file with program functionality.

Default location: You can place Sequence FM in any location. I recommend /usr/share/sfm.py
_____________________________

<b>Add-Ons:</b>


#Gtk-Tools Copyright (c) 2017 JJ Posti <techtimejourney.net>

#Crosslinker is a python file manager.The program comes with ABSOLUTELY NO WARRANTY;

#for details see: http://www.gnu.org/copyleft/gpl.html.

#This is free software, and you are welcome to redistribute it under

#GPL Version 2, June 1991″)
________________________________________


Note. Gtk-Tools is a very minimized  version of  my older file manager Crosslinker FM - hence the Crosslinker line in the copyright above.

Gtk-Tools hosts copy, paste, move and delete functionalities. You can launch Gtk-Tools from Sequence FM <b>Actions</b> menu. 

Dependencies:python python3 python3-gi python-gi

Gtk-Tools default location: Sequence FM tries to find Gtk-Tools from /usr/share/tools.py

If you wish to change the default of Gtk-Tools then change the pathway within sfm.py around the line 123 to something else. Default of this line reads: subprocess.Popen(“/usr/share/tools.py”)

Executing:

If needed make python files executable: chmod +x filename.py

Run with: python filename_location.py

___________________________________

<b>Considerations</b>

You can show hidden objects with Gtk-Tools and manipulate them from there. The most secure way to handle hidden files is to open them via text editor. In the case of folders I recommend using command line. In any case, be cautious when handling hidden files - since mismanagement might cause some stability issues to your operation system. More about terminal commands: http://www.techtimejourney.net/essential-terminal-tricks-you-should-know/ 

_________________________________
Original post is at:
http://www.techtimejourney.net/sequence-fm-v-4-gtk-tools-v-1/
