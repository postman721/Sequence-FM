
### Sequence FM 6.5 

![sfm65](https://user-images.githubusercontent.com/29865797/92326704-b276a980-f05c-11ea-84ad-bfe397449758.jpg)

Version 6.5 changes:

- Buttons to Gui

- New outlook.

- File/object location appears to statusbar when object is clicked.

License:

Sequence FM Copyright (c) 2017 JJ Posti

This program comes with ABSOLUTELY NO WARRANTY;

for details see: http://www.gnu.org/copyleft/gpl.html.

This is free software, and you are welcome to redistribute it under

GPL Version 2, June 1991″)


This filemanager is made with Python3 and QT5. It intends to be a simple and lightweight.

## Sequence FM new features (since 6.0)

New very important keys:

- Control (Ctrl), is now a key for selecting objects for copying/moving/deleting.
- ESC is now a buffer cleaner: Control adds files to the buffer (to wait for actions); ESC clears this buffer.
	 
New integrated features:

    - Delete key support
    - Delete multiple objects
    - Trash support added.(trash folder will be created inside user´s home directory)
    - Move multiple objects.
    - Copy multiple objects.
    - Statusbar added. 
    - Permanent delete support added.

#### Notice that if you move, copy or trash a file that already has an identically named counterpart on the upcoming location, you will end up loosing the older object (present before your actions counterpart) from the upcoming location.

Removed features:

- Direct terminal command support: This came out looking like a potential security issue. It was removed from the Gui but remains as a possibility within the code.
 
____________________________________________________________________________________________
Version 6.0: release posting is also available at: https://www.techtimejourney.net/sequence-fm-version-6-0-released/

## Features from earlier releases
### Currently functioning features include:

    Terminal command support in addressbar: You can, for example, type firefox and it will start after you press Enter and then press Control from your keyboard to execute.

    General addressbar funtionalities: Showing current location and navigating to current location via addressbar.

    Open file with application functionality.

    Make a new text file functionality.

    Make a new folder functionality.

    Object renaming is supported.

    Open archive, compress an object or extract an archive is supported via file-roller integration.

    Right-click menu: Almost all the above functionalities have been placed inside the right-click menu of Sequence FM.

    Preliminary shortkey support: Delete button of a keyboard will launch object deleting functionalities. Control button will 
    execute terminal command from addressbar – after first validated with Enter keypress.

    Error handling inside Sequence FM has been improved – to avoid accidental crashing.

To use Sequence FM you should have, at least, these installed (Debian base as an example):

sudo apt-get install python-pyqt5 python python3 file-roller

Default locations: You can place Sequence FM in any location. I recommend /usr/share/sfm.py

Executing:

If needed make python files executable: chmod +x filename.py

Run with: 


    python filename_location.py




