
### Sequence FM 5.0 

![screen](https://user-images.githubusercontent.com/29865797/53697710-09e2ec00-3dcc-11e9-8f9e-011f6e417323.jpg)

License:

Sequence FM Copyright (c) 2017 JJ Posti

This program comes with ABSOLUTELY NO WARRANTY;

for details see: http://www.gnu.org/copyleft/gpl.html.

This is free software, and you are welcome to redistribute it under

GPL Version 2, June 1991″)


This filemanager is made with Python3 and QT5. It intends to be a simple and lightweight.

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


### About delete, copy and moving functionalities.

I decided to keep this filemanager as unix like as possible. As I prefer terminal commands, I left out move,copy or removal commands. I believe those are best served via terminal client. See here for more: https://www.techtimejourney.net/essential-terminal-tricks-you-should-know/

