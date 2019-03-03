### Sequence FM 5.0 beta


License:

Sequence FM Copyright (c) 2017 JJ Posti <techtimejourney.net>

This program comes with ABSOLUTELY NO WARRANTY;

for details see: http://www.gnu.org/copyleft/gpl.html.

This is free software, and you are welcome to redistribute it under

GPL Version 2, June 1991″)


Sequence FM 5.0 beta arrives. This filemanager is made with Python3 and QT5. It intends to be a simple and lightweight.

Currently functioning features include for example:

- Terminal command support in addressbar: You can, for example, type firefox and it will start.

- General addressbar funtionalities: Showing current location and navigating to current location via addressbar.

- One file or folder copy,paste, move functionalities.

- Open file with application functionality.

- Make a new text file functionality.

- Make a new folder functionality.

- Object renaming is supported.

- Open archive, compress an object or extract an archive is supported via file-roller integration.

- Right-click menu: Almost all the above functionalities have been placed inside the right-click menu of Sequence FM.

- Preliminary shortkey support: Delete button of a keyboard will launch object deleting functionalities. Escape button in keyboard will instantly quit the filemanager.

- There is also a simple manual page added (for the man command).

Error handling inside Sequence FM has been improved - to avoid accidental crashing-


Notice that this filemanager is still in beta and does not currently support trashcan functionality. Trash support may be added in the future. 


To use Sequence FM you should have, at least, these installed (Debian base as an example):

sudo apt-get install python-pyqt5 python python3 file-roller


Default locations: You can place Sequence FM in any location. I recommend /usr/share/sfm.py


Executing:

If needed make python files executable: chmod +x filename.py

Run with: python filename_location.py
