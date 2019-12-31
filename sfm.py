#Sequence FM v.6.0 Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#This program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")

#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, sys, subprocess, getpass,copy, shutil
from copy import deepcopy
class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
#Title		
        self.setWindowTitle("Sequence FM v.6.0")
        self.resize(700, 500)

#Layout & Address bar
        self.vertical = QVBoxLayout()
        self.address=QLineEdit()
        self.address.setText("/")
        self.address.setAlignment(Qt.AlignCenter)
        self.address.returnPressed.connect(self.navigate)

#Statusbar
        self.status=QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Press Ctrl, to select objects for actions.")

        
#Toolbar        
        self.toolbar=QToolBar()
        self.toolbar.addWidget(self.address)
        self.addToolBar(self.toolbar)

#Treeview setup        
        self.treeview = QTreeView(self)
        self.treeview.model = QFileSystemModel()
        self.path=self.address.text()
        self.path="/"
        self.treeview.model.setRootPath(self.path)

        self.treeview.setModel(self.treeview.model)
        self.treeview.setRootIndex(self.treeview.model.index(self.path))
        self.treeview.setColumnWidth(0, 200)     
        self.treeview.clicked.connect(self.on_treeview_clicked)
        path=self.treeview.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

#Multi-selection list
        self.indexToRemove=[]

################################
#Layout
################################          
        self.vertical.addWidget(self.treeview)

        self.setCentralWidget(self.treeview)

################################
#Colors
################################

        self.setStyleSheet("color:#ffffff; background-color:#353535;}")
        self.treeview.setStyleSheet("color:#ffffff; background-color:#28496b;font-size: 12px; padding-left: 8px; padding-right: 8px; padding-top: 8px; padding-bottom: 8px} }")

        self.setLayout(self.vertical)
        self.show()

################################
#Right-Click menu
################################

    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        
        self.menu.setStyleSheet("QMenu{color:#ffffff; background-color:#2f2e2d; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QMenu:selected{background-color:#125c8c;}") 
        
        self.open_me = self.menu.addAction('Open selected file with...')
        self.open_me.triggered.connect(self.opens_me)
        
        self.newdir1 = self.menu.addAction('Make a new directory')
        self.newdir1.triggered.connect(self.newdir)
        
        self.newfile1 = self.menu.addAction('Make a new text file')
        self.newfile1.triggered.connect(self.newfile)

        self.rename1 = self.menu.addAction('Rename object')
        self.rename1.triggered.connect(self.rename)
        
        self.move1 = self.menu.addAction('Move objects')
        self.move1.triggered.connect(self.move_object)
        
        self.copy1 = self.menu.addAction('Copy objects')
        self.copy1.triggered.connect(self.copy_object)

        self.sep1 = self.menu.addSeparator()
        
        self.for1 = self.menu.addAction('Delete objects')
        self.for1.triggered.connect(self.delete_object)
        
        self.for2 = self.menu.addAction('Permanently delete objects')
        self.for2.triggered.connect(self.permanent_delete_object)

        self.openar = self.menu.addAction('Open archive')
        self.openar.triggered.connect(self.rolleropen)

        self.compress = self.menu.addAction('Compress object')
        self.compress.triggered.connect(self.filecompress)
        
        self.extract = self.menu.addAction('Extract object')
        self.extract.triggered.connect(self.filextract)

        self.about1 = self.menu.addAction('About')
        self.about1.triggered.connect(self.about)        

#add other required actions
        self.menu.popup(QtGui.QCursor.pos())


####################
#Make trash folder
####################
    def maketrash(self):
        name=getpass.getuser()
        uhome="/home/"
        trash="/trash"
        combine1=uhome + name
        os.chdir(combine1)
        if os.path.exists("trash"):
            pass
        else:                
            makefolder=os.makedirs('trash')   

######################
#Move to trash folder
######################
    def move_trash(self):
        name=getpass.getuser()
        uhome="/home/"
        trash="/trash"
        combine1=uhome + name
        
################################
#About messagebox
################################
    def about(self):
        buttonReply = QMessageBox.question(self, 'Sequence FM v.5.0 Copyright(c)2017 JJ Posti <techtimejourney.net>', "Sequence FM is is a python file manager, which ports the features of Crosslinker FM series to QT5 - and adds many things along way.The program comes with ABSOLUTELY NO WARRANTY  for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991.", QMessageBox.Ok )
        if buttonReply == QMessageBox.Ok:
            print('Ok clicked, messagebox closed.')

           
################################
#Double left-click function
################################        
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeview_clicked(self, index):
        indexItem = self.treeview.model.index(index.row(), 0, index.parent())

# path or filename selected
        filename = self.treeview.model.fileName(indexItem)


################################
#Full path/filename selected
################################        
        global filepath
        try:
            filepath = self.treeview.model.filePath(indexItem)
            self.address.setText(filepath)
            print (filepath)
        except Exception as e:
            print (e)			                 

################################
#Navigation
################################
    def navigate(self):
        try:
            self.treeview.model = QFileSystemModel()
            self.path=self.address.text()
            self.treeview.model.setRootPath(self.path)
            self.treeview.setModel(self.treeview.model)
            self.treeview.setRootIndex(self.treeview.model.index(self.path))
            self.treeview.setColumnWidth(0, 200)
            return self.path
        except Exception as e:
            print (e)			

################################
#Terminal command support
################################
    def terminals(self):
        subprocess.Popen(self.path, shell=True, stdout=subprocess.PIPE)
	 
################################
#Rename in current path
################################
    def rename(self):
        text, ok = QInputDialog.getText(self, 'Rename an object', ' \n Remember to include the extension as well (file example:foo.txt - if in any doubt CANCEL NOW. ')
        if ok:
            print text
            print "Now:", filepath
            renamepath=os.path.dirname(filepath)
            print "Rename pathway:", renamepath
            new_entry= renamepath + '/' + text
            print "New object location after renaming is:", new_entry
            subprocess.Popen(['mv', filepath , new_entry])             

################################
#Open With program
################################
    def opens_me(self):
        text, ok = QInputDialog.getText(self, 'Open with a program', ' \n Type the name of the program, which you want to use. ')
        if ok:
            try:
                print text
                subprocess.Popen([text , filepath])                                                                        
            except Exception as e:
                print (e)				


################################
#Move an object
################################
    def move_object(self):
        if not self.indexToRemove:
            print ("Nothing to move.")
        else:    			
            buttonReply = QMessageBox.question(self, 'Move objects to current folder?', ' \n Press No now if you are not sure. ')
            if buttonReply == QMessageBox.Yes:
                try:
                    list_string=(self.indexToRemove)
                    for lines in list_string:
                        x=lines.encode('utf-8')
                        y=x.decode('unicode-escape')
                        print (y)
                        subprocess.Popen(["mv" , y, filepath])                        
                        print (self.indexToRemove)
                        self.status.showMessage("Moving done. Clear buffer with ESC.")
                except Exception as e:
                    print (e)
            if buttonReply == QMessageBox.No:
                print filepath
                del self.indexToRemove[:]
                print (self.indexToRemove)
                self.status.showMessage("Buffer is cleared.")   

################################
#Copy an object
################################
    def copy_object(self):
        if not self.indexToRemove:
            print ("Nothing to copy.")
        else:    			
            buttonReply = QMessageBox.question(self, 'Copy objects to current folder?', ' \n Press No now if you are not sure. ')
            if buttonReply == QMessageBox.Yes:
                try:
                    list_string=(self.indexToRemove)
                    for lines in list_string:
                        x=lines.encode('utf-8')
                        y=x.decode('unicode-escape')
                        print (y)
                        subprocess.Popen(["cp" , "-r" , y, filepath])
                        print (self.indexToRemove)
                        self.status.showMessage("Copying done. Clear buffer with ESC.")
                except Exception as e:
                    print (e)
            if buttonReply == QMessageBox.No:
                print filepath	
                del self.indexToRemove[:]
                print (self.indexToRemove)
                self.status.showMessage("Buffer is cleared.")   


################################
#Delete an object
################################
    def delete_object(self):
        self.maketrash()	
        if not self.indexToRemove:
            print ("Nothing to remove.")
        else:    			
            buttonReply = QMessageBox.question(self, 'Move objects to trash?', ' \n Press No now if you are not sure. ')
            if buttonReply == QMessageBox.Yes:
                try:
                    list_string=(self.indexToRemove)
                    for lines in list_string:
                        x=lines.encode('utf-8')
                        y=x.decode('unicode-escape')
                        print (y)
                        name=getpass.getuser()
                        uhome="/home/"
                        trash="/trash"
                        combine1=uhome + name + trash
                        subprocess.Popen(["mv" , y , combine1])
                        print (self.indexToRemove)
                        self.status.showMessage("Objects trashed. Clear buffer with ESC.")                                                                         			
                except Exception as e:
                    print (e)
            if buttonReply == QMessageBox.No:
                print filepath
                del self.indexToRemove[:]
                print (self.indexToRemove)
                self.status.showMessage("Buffer is cleared.")
                   			

################################
#Permanent delete an object
################################
    def permanent_delete_object(self):
        self.maketrash()	
        if not self.indexToRemove:
            print ("Nothing to remove.")
        else:    			
            buttonReply = QMessageBox.question(self, 'Permanently delete  objects?', ' \n Press No now if you are not sure. ')
            if buttonReply == QMessageBox.Yes:
                try:
                    list_string=(self.indexToRemove)
                    for lines in list_string:
                        x=lines.encode('utf-8')
                        y=x.decode('unicode-escape')
                        print (y)
                        subprocess.Popen(["rm" , "-r" , y])
                        self.status.showMessage("Objects permanently deleted. Clear buffer with ESC.")                                                                        			
                except Exception as e:
                    print (e)
            if buttonReply == QMessageBox.No:
                print filepath
                del self.indexToRemove[:]
                print (self.indexToRemove)
                self.status.showMessage("Buffer is cleared.")

    
###########################            				
#Keypress events
###########################        
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Delete:
            self.delete_object()
        if event.key()==Qt.Key_Control:
            self.indexToRemove.append(filepath)
            list_string=(self.indexToRemove)
            for lines in list_string:
                x=lines.encode('utf-8')
                y=x.decode('unicode-escape')
                print (y)
                self.status.showMessage("Added " + (y) + " to buffer.")
        if event.key()==Qt.Key_Escape:
            del self.indexToRemove[:]
            print (self.indexToRemove)
            self.status.showMessage("Buffer is cleared.")
            print ("Buffer is empty.")                  			                 			               
        else:
            pass 				

##############################
#CREATE OBJECT FUNCTIONS
#################################

#File-roller integrations
    def filextract(self,widget):
        try:
		    subprocess.Popen(['file-roller', filepath , '--extract']) 
        except Exception as e:
            print (e)			
		
    def filecompress(self,widget):
        try:
		    subprocess.Popen(['file-roller', '-d', '--add', filepath]) 
        except Exception as e:
            print (e)
            					
    def rolleropen(self,widget):
        try:		
		    subprocess.Popen(['file-roller', filepath]) 
        except Exception as e:
            print (e)
            
#Make new directory
    def newdir(self,widget):
        try:
            os.chdir(filepath)
            makefolder=os.makedirs('Newfolder')
            print os.getcwd()
            makefolder		           
        except Exception as e:
            print (e)
                    			
#Make new empty text file
    def newfile(self,widget):
        try:
            os.chdir(filepath)
            newtext=os.mknod('Newtext.txt')
            print os.getcwd()
            newtext
        except Exception as e:
            print (e)
            			        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show() 
    sys.exit(app.exec_())
