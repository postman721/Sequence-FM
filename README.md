
### Sequence FM 7.0 RC2

<b>Default outlook (Since 7.0 RC2)</b>

![default](https://user-images.githubusercontent.com/29865797/114307574-f77a2700-9ae8-11eb-815a-e863e3972372.png)


<b>Alternative themes (Since 7.0 RC2)</b> 

Notice that screenshots are from dev: Real functionality matches that of default as seen above. 

![alternatives-dev](https://user-images.githubusercontent.com/29865797/114307577-fba64480-9ae8-11eb-9483-a6799024ddb4.png)


<b>7.0 RC2 fixes and new features:</b>

- CSS theme support.
- 4 themes added.
- Dual panel mode is now default.

- Listview added as shortcut place.
- QList defaulted -> Changed from Treeview.
- File/object descriptors added.

- Multi-selection by holding CTRL and clicking objects is now possible.
- File-roller integration removed as an effort to reduce external dependencies -> Open external program functionality added as a replacement.
- Object buffer of previous releases removed and replaced with native Pyqt5 dialogs.


<b>7.0 RC1 fixes and new features:</b>
- Fixing Layout issues.
- Adding native imageviewer.
- Adding native text reader.
- Fixing functionality issues with CTRL key.
- Changing underlying code structure to a bit easier form.


# Older versions
Version 6.5 changes:

- Buttons to Gui

- New outlook.

- File/object location appears on the statusbar when the object is clicked.

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




