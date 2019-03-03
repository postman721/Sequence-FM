###################################################
#Gtk-Tools is depricated since Sequnce FM 5.0 Beta
####################################################

#!/usr/bin/env python
#Gtk-Tools Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#Crosslinker is a python file manager.The program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")

#IMPORTING MODULES
from gi.repository import Gtk, Gdk, GObject, GLib, Gio

import os, sys, subprocess, shutil, errno, sys, getpass
from os.path import basename

class Tools(Gtk.Window):
  	     		                   								                          
######################
#MOVE FUNCTION
######################
#Move+Select (files+folders)+copy for files
    def movesource(self,widget):
        global sourcemove2
        sourcemove2=self.filea.get_filenames()

#Moving for files and folders		
    def movedestination(self, widget, data=None):
        msg=("If an object with the same name is found on the move destination it will be overwritten. Are you sure you want to continue?")
        
        destroy_dialog = Gtk.MessageDialog (None, 0, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, msg)
        destroy_dialog.set_title("Move object(s)?")
        response = destroy_dialog.run()
        destroy_dialog.destroy()                            
        if response == Gtk.ResponseType.OK:			
		    movedest=self.filea.get_current_folder()
		    os.chdir(movedest)
		    for files in sourcemove2:
				shutil.move(files,movedest)
		    return False # returning False and make destroy-event

        else:
            return True # returning True and avoid "destroy-event" 

#########################
#TRASH FUNCTIONS
#############################
    def maketrash(self,widget):
        name=getpass.getuser()
        uhome="/home/"
        trash="/trash"
        combine1=uhome + name
        os.chdir(combine1)            
        makefolder=os.makedirs('trash')

#Multiple objects to trash	
    def trash(self, widget, data=None):
        msg=("If an object with the same name is found within the trash it will be overwritten. Make sure you have created the trash folder before trying to delete anything. Are you sure you want to continue?")
        
        destroy_dialog = Gtk.MessageDialog (None, 0, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, msg)
        destroy_dialog.set_title("Trash an object?")
        response = destroy_dialog.run()
        destroy_dialog.destroy()                            
        if response == Gtk.ResponseType.OK:			
            name=getpass.getuser()
            uhome="/home/"
            trash="/trash"
            combine1=uhome + name 
            os.chdir(combine1)            
            combinex=uhome + name + trash
            sourcemovex=(self.filea.get_filenames())
            for files in sourcemovex:
				shutil.move(files, combinex)
            return False # returning False and make destroy-event

        else:
            return True # returning True and avoid "destroy-event" 

##################################
#PASTE FUNCTION
##########################
    def copydestination(self, widget, data=None):
        msg=("If an object with the same name is found on the paste destination it will be overwritten. Are you sure you want to continue?")
        destroy_dialog = Gtk.MessageDialog (None, 0, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, msg)
        destroy_dialog.set_title("Paste an object or objects?")
        response = destroy_dialog.run()
        destroy_dialog.destroy()                            
        if response == Gtk.ResponseType.OK:
            try:
                copydest=self.filea.get_current_folder()
                os.chdir(copydest)
                for folders in sourcemove2:
                    subprocess.Popen(['cp', '-r', folders , copydest])
            except OSError as e:
                if e.errno == errno.ENOTDIR:		
                    copydest=self.filea.get_current_folder()
                    os.chdir(copydest)
                    for files in sourcemove2:
                        shutil.copy(files,copydest)
                    return False # returning False and make destroy-event
            else:
                   return True # returning True and avoid "destroy-event"                       			              

####################
#DELETE FUNCTIONS
##########################
#Destroy/Delete function  
    def foreverdelete (self, widget, data=None):
        msg=("Delete THIS PERMANENTLY?")
        destroy_dialog = Gtk.MessageDialog (None, 0, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, msg)
        destroy_dialog.set_title("DELETE CONTENT PERMANENTLY?")
        response = destroy_dialog.run()
        destroy_dialog.destroy()                            
        if response == Gtk.ResponseType.OK:
            try:
                foldername=self.filea.get_filename()
                shutil.rmtree(foldername)
            except OSError as e:
                if e.errno == errno.ENOTDIR:
                    filename=self.filea.get_filename()
                    os.remove(filename)
            return False # returning False and make destroy-event

        else:
            return True # returning True and avoid "destroy-event"

###########################################################
#GENERAL FUNCTIONS
#####################################
#Close function
    def destroy (self, widget, data=None):
        Gtk.main_quit()

#About dialog function
    def about1 (self, widget):
        about1 = Gtk.AboutDialog()
        about1.set_program_name("Gtk-Tools")
        about1.set_version("V.1")
        about1.set_copyright(" Copyright (c) 2017 JJ Posti <techtimejourney.net>")
        about1.set_comments("GTK-Tools is a program for copying, pasting and deleting files. GTk-Tools is an adaptation of  Crosslinker FM code. The program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991. \n \n_____________________________________________________________________________________________________________________________________________________________ \n \n Tips: Via right-click menu you can view hidden files by checking the entry in question. If you want to copy a location path to clipboard select 'Copy Location' from the right-click menu. With the 'Copy Location' you can easily pass object locations back to Sequence FM so that you can use  and open them.")
        about1.run()
        about1.destroy()            	                        		              
####################################
#STARTING WINDOW DEFINITIONS
#################################
#GENERAL STUFF
#################################    
    def __init__(self):    
    # Create THE WINDOW
        self.window1=Gtk.Window()
        self.window1.set_position(Gtk.WindowPosition.CENTER)
        self.window1.set_title("Gtk-Tools")
#Toolbars
        self.toolbar2=Gtk.Toolbar()
###############################
#FILE MANAGER
#################################       
# Create a new file selection widget        
        self.filea = Gtk.FileChooserWidget()

#Additional features
        name=getpass.getuser()
        uhome="/home/"
        combine=uhome + name
        self.filea.set_current_folder (combine)
        self.filea.set_select_multiple(True)
#######################################################
#About button
        self.about1_button=Gtk.ToolButton(Gtk.STOCK_INFO)
        self.about1_button.connect("clicked", self.about1)
        self.about1_button.set_label("Info")
        self.about1_button.set_tooltip_text ("Info")                         
        self.toolbar2.insert(self.about1_button, -1)

#Copy/Select for moving
        self.copy_button=Gtk.ToolButton(Gtk.STOCK_COPY)
        self.copy_button.connect("clicked", self.movesource)
        self.copy_button.set_label("Copy/Select for moving")
        self.toolbar2.insert(self.copy_button, -1)
# Paste
        self.paste_button=Gtk.ToolButton(Gtk.STOCK_PASTE)
        self.paste_button.connect("clicked", self.copydestination)
        self.toolbar2.insert(self.paste_button, -1)
#Move        
        self.move_button=Gtk.ToolButton(Gtk.STOCK_REFRESH)
        self.move_button.connect("clicked", self.movedestination)
        self.move_button.set_label("Move to location")
        self.toolbar2.insert(self.move_button, -1)        
#Separator
        self.separator2=Gtk.SeparatorToolItem()
        self.toolbar2.insert(self.separator2, -1)

#Trash buttons

        self.maketrash_button=Gtk.ToolButton(Gtk.STOCK_OK)
        self.maketrash_button.connect("clicked", self.maketrash)
        self.maketrash_button.set_label("Make trashcan")
        self.toolbar2.insert(self.maketrash_button, -1)       

        self.trash_button=Gtk.ToolButton(Gtk.STOCK_DELETE)
        self.trash_button.connect("clicked", self.trash)
        self.trash_button.set_label("Move to trash?")
        self.toolbar2.insert(self.trash_button, -1)        
        
#Separators
        self.separator3=Gtk.SeparatorToolItem()
        self.toolbar2.insert(self.separator3, -1)

#Delete permanently button
        self.delete2_button=Gtk.ToolButton(Gtk.STOCK_DIALOG_WARNING)
        self.delete2_button.connect("clicked", self.foreverdelete)
        self.delete2_button.set_label("Delete permanently")
        self.toolbar2.insert(self.delete2_button, -1)

                        
#Copy/Move and Paste
        self.paste_button.set_tooltip_text ("Paste a copy or copies to a location")
        self.copy_button.set_tooltip_text ("Select object(s) for moving or copying")
        self.move_button.set_tooltip_text ("Move object(s) to the location")

#Delete Permanently tooltip
        self.delete2_button.set_tooltip_text ("Delete content permanently")

#Trash
        self.trash_button.set_tooltip_text ("Move item(s) to trash")
        self.maketrash_button.set_tooltip_text ("Make trashcan")
################################################################################
###########################
#BOX CONTAINERS 
############################
        self.hbox=Gtk.HBox()
        self.hbox.pack_start(self.toolbar2,False, False, False)
     
# Vertical box2 for toolbar2      
        self.vbox=Gtk.VBox(False)
        self.vbox.pack_start(self.hbox, False, False, False)
        self.vbox.pack_end(self.filea, True, True, True)                 
#Show everything		
        self.window1.add(self.vbox)
        self.window1.show_all()         
#Making window resizable and enabling the close window connector        
        self.window1.set_resizable(True)
        self.window1.connect("destroy", Gtk.main_quit)
                       
def main():
    Gtk.main()
    return 0

if __name__ == "__main__":
    Tools()    
    main()
