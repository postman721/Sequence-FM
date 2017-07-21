#Sequence FM v.4.1 Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#This program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")
#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, sys, subprocess, getpass
class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
#Title		
        self.setWindowTitle("Sequence FM v.4.1")
        self.resize(600, 480)
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
#Menu
        self.menu1 = self.menuBar().addMenu('File')
        self.menu2 = self.menuBar().addMenu('Actions')        
        self.menu4 = self.menuBar().addMenu('Archiving')        
        self.menu5 = self.menuBar().addMenu('About')        
#Menu actions 
#########################################################NEW DIR/FILE               
        self.open_me = self.menu1.addAction('Open selected file with...')
        self.open_me.triggered.connect(self.opens_me)
        
        self.newdir1 = self.menu1.addAction('Make a new directory')
        self.newdir1.triggered.connect(self.newdir)
        
        self.newfile1 = self.menu1.addAction('Make a new text file')
        self.newfile1.triggered.connect(self.newfile)

        self.rename1 = self.menu1.addAction('Rename object')
        self.rename1.triggered.connect(self.rename)
            
########################################################PERMANENT DELETE
        self.for2 = self.menu2.addAction('Copy/Paste/Move/Delete')
        self.for2.triggered.connect(self.permanent)                
##########################################################################
        self.openar = self.menu4.addAction('Open archive')
        self.openar.triggered.connect(self.rolleropen)

        self.compress = self.menu4.addAction('Compress object')
        self.compress.triggered.connect(self.filecompress)
        
        self.extract = self.menu4.addAction('Extract object')
        self.extract.triggered.connect(self.filextract)
#################################################################################ABOUT DIALOG
        self.about1 = self.menu5.addAction('About')
        self.about1.triggered.connect(self.about)
#Layout                    
        self.vertical.addWidget(self.treeview)    
        self.setCentralWidget(self.treeview)

        self.setLayout(self.vertical)
        self.show()
#Right-Click menu
    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        
        self.open_me = self.menu.addAction('Open selected file with...')
        self.open_me.triggered.connect(self.opens_me)
        
        self.newdir1 = self.menu.addAction('Make a new directory')
        self.newdir1.triggered.connect(self.newdir)
        
        self.newfile1 = self.menu.addAction('Make a new text file')
        self.newfile1.triggered.connect(self.newfile)

        self.rename1 = self.menu.addAction('Rename object')
        self.rename1.triggered.connect(self.rename)

        self.sep1 = self.menu.addSeparator()
######################################################## DELETE
        self.for1 = self.menu.addAction('Copy/Paste/Move/Delete')
        self.for1.triggered.connect(self.permanent)
        
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
#About messagebox
    def about(self):
        buttonReply = QMessageBox.question(self, 'Sequence FM v.4.1 Copyright(c)2017 JJ Posti <techtimejourney.net>', "Sequence FM is is a python file manager, which ports the features of Crosslinker FM series to QT5 - and adds many things along way.The program comes with ABSOLUTELY NO WARRANTY  for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991.", QMessageBox.Ok )
        if buttonReply == QMessageBox.Ok:
            print('Ok clicked, messagebox closed.')
#Calling Gtk-Tools            
    def permanent(self):
        subprocess.Popen("/usr/share/tools.py")            
###########################################            
###Double left-click function        
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeview_clicked(self, index):
        indexItem = self.treeview.model.index(index.row(), 0, index.parent())
# path or filename selected
        filename = self.treeview.model.fileName(indexItem)
# full path/filename selected        
        global filepath
        filepath = self.treeview.model.filePath(indexItem)
        self.address.setText(filepath)             
#Navigation
    def navigate(self):
        self.treeview.model = QFileSystemModel()
        self.path=self.address.text()
        self.treeview.model.setRootPath(self.path)
        self.treeview.setModel(self.treeview.model)
        self.treeview.setRootIndex(self.treeview.model.index(self.path))
        self.treeview.setColumnWidth(0, 200)
        return self.path
#Terminal command support
    def terminals(self):
        subprocess.Popen(self.path, shell=True, stdout=subprocess.PIPE)
	 
#######################################################################                        
#Rename in current path
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
#Open With program...
    def opens_me(self):
        text, ok = QInputDialog.getText(self, 'Open with a program', ' \n Type the name of the program, which you want to use. ')
        if ok:
            print text
            subprocess.Popen([text , filepath])                                                                        
##############################
#CREATE OBJECT FUNCTIONS
#################################
#File-roller integrations
    def filextract(self,widget):
		subprocess.Popen(['file-roller', filepath , '--extract']) 
		
    def filecompress(self,widget):
		subprocess.Popen(['file-roller', '-d', '--add', filepath]) 
				
    def rolleropen(self,widget):
		subprocess.Popen(['file-roller', filepath]) 
#Make new directory
    def newdir(self,widget):
		os.chdir(filepath)
		makefolder=os.makedirs('Newfolder')
		print os.getcwd()
		makefolder		           
#Make new empty text file
    def newfile(self,widget):
        os.chdir(filepath)
        newtext=os.mknod('Newtext.txt')
        print os.getcwd()
        newtext        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show() 
    sys.exit(app.exec_())
