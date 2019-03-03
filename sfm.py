#Sequence FM v.5.0 Beta Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#This program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")

#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, sys, subprocess, getpass,copy
from copy import deepcopy
class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
#Title		
        self.setWindowTitle("Sequence FM v.5.0 Beta")
        self.resize(700, 500)

#Layout & Address bar
        self.vertical = QVBoxLayout()
        self.address=QLineEdit()
        self.address.setText("/")
        self.address.setAlignment(Qt.AlignCenter)
        self.address.returnPressed.connect(self.navigate)
        self.address.returnPressed.connect(self.terminals)

#Toolbar        
        self.toolbar=QToolBar()
        self.toolbar.addWidget(self.address)
        self.addToolBar(self.toolbar)
        self.toolbar.setLayout(self.vertical)        

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

        self.sep1 = self.menu.addSeparator()
        self.for1 = self.menu.addAction('Delete object')
        self.for1.triggered.connect(self.delete_object)

######################################################## COPY

        self.for2 = self.menu.addAction('Copy object')
        self.for3 = self.menu.addAction('Paste object')

        self.for2.triggered.connect(self.copy_object)
        self.for3.triggered.connect(self.paste_object)

        self.openar = self.menu.addAction('Open archive')
        self.openar.triggered.connect(self.rolleropen)

        self.compress = self.menu.addAction('Compress object')
        self.compress.triggered.connect(self.filecompress)
        
        self.extract = self.menu.addAction('Extract object')
        self.extract.triggered.connect(self.filextract)
#################################################################################ABOUT DIALOG
        self.about1 = self.menu.addAction('About')
        self.about1.triggered.connect(self.about)        

#add other required actions
        self.menu.popup(QtGui.QCursor.pos())

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
#Delete an object
################################
    def delete_object(self):
        buttonReply = QMessageBox.question(self, 'Delete object permanently?', ' \n Press No now if you are not sure. ')
        if buttonReply == QMessageBox.Yes:
            try:
                print filepath
                subprocess.Popen(["rm" , "-r", filepath])                                                                        			
            except Exception as e:
                print (e)
        if buttonReply == QMessageBox.No:
            print filepath
            pass   			
            
##############################
#Copy & Paste functions
###############################           			                                                                                 			
    def copy_object(self):
        try:
            global old_destination
            old_destination=copy.deepcopy(filepath)
            object_names.append(old_destination)
            print(old_destination)
        except Exception as e:
            print(e)			    					

#Paste object 
    def paste_object(self):
        buttonReply = QMessageBox.question(self, 'Paste the object to this location? It will override the existing object with the same name', ' \n Press No now if you are not sure. ')
        if buttonReply == QMessageBox.Yes:
            try:
                print (old_destination)
                print (filepath)
                subprocess.Popen(["cp" , "-r", old_destination, filepath])                                                                        			
            except Exception as e:
                print (e)
        if buttonReply == QMessageBox.No:
            pass			
#################################################################               
            				
#Keypress events        
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Delete:
            self.delete_object()			                 			            
        elif event.key()==Qt.Key_Escape:
            app.quit()
            print "Program ends."    
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
