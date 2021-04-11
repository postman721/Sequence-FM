#Sequence FM v.7.0 RC2. Copyright (c) 2017 JJ Posti <techtimejourney.net> This program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html.  This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991")
#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, sys, subprocess, getpass,copy, shutil, time
from copy import deepcopy
#SFM Modules
from theme import *
class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)        
#Window Definitions		
        self.title= ("Sequence FM v.7.0 RC2")
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        self.resize(900,600)
        self.setMaximumSize(1050,600)
        self.theme()
#################################
#Theme from theme.py
################################
    def theme(self):
        if theme == "default":
            with open("./themes/blue.css","r") as style:
                self.setStyleSheet(style.read())
        if theme == "midnight":
            with open("./themes/midnight.css","r") as style:
                self.setStyleSheet(style.read())
        if theme == "old":
            with open("./themes/default.css","r") as style:
                self.setStyleSheet(style.read())
        if theme == "yellow":
            with open("./themes/yellow.css","r") as style:
                self.setStyleSheet(style.read())                              
#List
        self.list = QListWidget()
        self.list.setStyleSheet("QListWidget {border: none;} QListWidget::item { margin-top:10px; margin-bottom:10px  }")
        self.list.addItem("Home")
        self.list.addItem("Trash")
        self.list.addItem("Root")
        self.list.currentItemChanged.connect(self.clicked)
       
#Address bar
        self.address=QLineEdit()
        self.name=getpass.getuser()
        self.home="/home/"
        self.combine=self.home + self.name 
        self.address.setText(self.combine)
        self.address.setAlignment(Qt.AlignCenter)
        self.address.returnPressed.connect(self.navigate)
         
#Statusbar
        self.status=QStatusBar()

#Buttons
        self.open_with_button = QPushButton('Open with', self)
        self.open_with_button.setToolTip('Open with')
        self.open_with_button.clicked.connect(self.open_with_clicked)
        
        self.read_button = QPushButton('Read a text file', self)
        self.read_button.setToolTip('Read a text file')
        self.read_button.clicked.connect(self.readme)

        self.image_button = QPushButton('Open an image', self)
        self.image_button.setCheckable(True)
        self.image_button.setToolTip('Open an image')
        self.image_button.clicked.connect(self.images)             
#Toolbars        
        self.toolbar=QToolBar()
        self.toolbar.addWidget(self.open_with_button)
        self.toolbar.addWidget(self.address)
        self.toolbar.addWidget(self.read_button)
        self.toolbar.addWidget(self.image_button)

        self.toolbar2=QToolBar()
        self.toolbar2.hide()
                        
#Treeview setup folders       
        self.treeview = QListView(self)
        self.treeview.model = QFileSystemModel()
        self.treeview.setFixedSize(240, 600)
        self.treeview.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.path=self.address.text()
        self.name=getpass.getuser()
        self.home="/home/"
        self.path=self.home + self.name
        self.treeview.model.setRootPath(self.path)

        self.treeview.setModel(self.treeview.model)
        self.treeview.setRootIndex(self.treeview.model.index(self.path))
        self.treeview.clicked[QModelIndex].connect(self.on_treeview_clicked)

#Treeview setup files       
        self.treeview2 = QTreeView(self)
        self.treeview2.model = QFileSystemModel()
        self.treeview2.model.setFilter(QDir.NoDotAndDotDot | QDir.Dirs | QDir.NoDot | QDir.NoDotDot | QDir.Files)
        
#Size attributes
        self.treeview2.setFixedSize(440, 600)
        
                                     
#Finalizations
        self.path=self.address.text()
        self.name=getpass.getuser()
        self.home="/home/"
        self.path=self.home + self.name
        self.treeview2.model.setRootPath(self.path)
        self.treeview2.setModel(self.treeview2.model)
        self.treeview2.setRootIndex(self.treeview2.model.index(self.path))
        self.treeview2.clicked[QModelIndex].connect(self.on_treeview2_clicked)
        self.treeview2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treeview2.hideColumn(1)
        self.treeview2.hideColumn(2)
        self.treeview2.hideColumn(3)


#Read files
        self.read = QTextEdit()
        self.read.resize(640, 480)
        self.read.setReadOnly(True)
                
#Open images
        self.image = QLabel(self)
        self.image_button.clicked.connect(self.images)                              
################################
#Layouts
################################          
        self.setCentralWidget(QWidget(self))
        self.vertical = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        self.horizontal.addWidget(self.list)
        self.vertical.addWidget(self.toolbar)
        self.vertical.addWidget(self.toolbar2)

        self.horizontal.addWidget(self.treeview)
        self.horizontal.addWidget(self.treeview2)
        self.vertical.addLayout(self.horizontal)
        self.vertical.addWidget(self.image)

        self.vertical.addWidget(self.status)
        self.centralWidget().setLayout(self.vertical)
        self.status.showMessage("Select objects for actions from the right side.")                                           			                 			                  
##############
#List function
###############
    def clicked(self,current,previous):        
        current=self.list.currentItem().text()
        if current == "Home":
            self.name=getpass.getuser()
            self.home="/home/"
            self.path=self.home + self.name
            self.treeview.model.setRootPath(self.path)
            self.treeview.setRootIndex(self.treeview.model.index(self.path))
            self.treeview2.model.setRootPath(self.path)
            self.treeview2.setRootIndex(self.treeview2.model.index(self.path))

            self.address.setText(self.path)
            self.treeview.model.setRootPath(self.path)
            self.treeview.setModel(self.treeview.model)
            self.treeview.setRootIndex(self.treeview.model.index(self.path))
            self.status.showMessage("/home/" + self.name)

        elif current == "Trash":
            self.maketrash()
            self.name=getpass.getuser()
            self.home="/home/"
            self.trash="/trash"
            self.path=self.home + self.name + self.trash
            self.treeview.model.setRootPath(self.path)
            self.treeview.setRootIndex(self.treeview.model.index(self.path))
            self.treeview2.model.setRootPath(self.path)
            self.treeview2.setRootIndex(self.treeview2.model.index(self.path))

            self.address.setText(self.path)
            self.treeview.model.setRootPath(self.path)
            self.treeview.setModel(self.treeview.model)
            self.treeview.setRootIndex(self.treeview.model.index(self.path))
            self.status.showMessage(self.path)
            
        elif current == "Root":
            self.maketrash()
            self.root="/"
            self.treeview.model.setRootPath(self.root)
            self.treeview.setRootIndex(self.treeview.model.index(self.root))
            self.treeview2.model.setRootPath(self.path)
            self.treeview2.setRootIndex(self.treeview2.model.index(self.path))

            self.address.setText(self.root)
            self.treeview.model.setRootPath(self.root)
            self.treeview.setModel(self.treeview.model)
            self.treeview.setRootIndex(self.treeview.model.index(self.root))
            self.status.showMessage("/")                         
#################################
#Button connectors
################################		      		            
    @pyqtSlot()
    def open_with_clicked(self):
        try:
            self.opens_me()
        except Exception as e:
            print (e)			            	
################################
#Right-Click menu
################################
    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
       
        self.open_me = self.menu.addAction('Open selected file with...')
        self.open_me.triggered.connect(self.opens_me)
        
        self.open_me2 = self.menu.addAction('Open external program')
        self.open_me2.triggered.connect(self.opens_me2)
        
        self.newdir1 = self.menu.addAction('Make a new directory')
        self.newdir1.triggered.connect(self.newdir)
        
        self.newfile1 = self.menu.addAction('Make a new text file')
        self.newfile1.triggered.connect(self.newfile)

        self.sepa = self.menu.addSeparator()

        self.rename1 = self.menu.addAction('Rename object')
        self.rename1.triggered.connect(self.rename_object)
                        
        self.paste = self.menu.addAction('Copy to...')
        self.paste.triggered.connect(self.paste_copy)
        self.sep1 = self.menu.addSeparator()

        self.sep2q = self.menu.addSeparator()

        self.move3 = self.menu.addAction('Move to...')
        self.move3.triggered.connect(self.move_final)
        
        self.sep2 = self.menu.addSeparator()
        
        self.for1 = self.menu.addAction('Delete objects')
        self.for1.triggered.connect(self.delete_objects)
                
        self.for2 = self.menu.addAction('Permanently delete objects')
        self.for2.triggered.connect(self.permanent_delete_objects)

        self.sepx = self.menu.addSeparator()

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
##################
#Read text files            
##################
    def readme(self):
        try:
            self.read.setHidden(not self.read.isHidden())
            read=open(filepath2).read()            
        except Exception as e:
            print ("Nothing to read.")
            self.read.hide()
        else:
            self.read.setPlainText(read)
            self.read.setPlainText(read)
            self.status.showMessage("Press Read a text file again to hide the reader.")            
############
#Open images
#############
    def images(self):
        if self.image_button.isChecked():
            try:
                self.treeview.hide()
                self.treeview2.hide()
                self.list.hide()
                self.image.setPixmap(QPixmap(filepath2))
                self.image.show()
                self.toolbar.hide()
                self.toolbar2.addWidget(self.image_button)
                self.toolbar2.show()
                self.status.showMessage("Press Open an image button to hide.")            
            except Exception as e:
                print("No image selected")
                self.image_button.setChecked(False)
        else:
            self.image.hide()
            self.resize(900,600)
            self.toolbar.addWidget(self.image_button)
            self.toolbar.show()
            self.toolbar2.hide()
            self.treeview.setFixedSize(200, 600)
            self.list.show()
            self.treeview.show()
            self.treeview2.setFixedSize(750, 600)
            self.treeview2.show()
            self.status.showMessage("Select objects for actions from the right side.")                                           			                 			                  
################################
#About messagebox
################################
    def about(self):
        buttonReply = QMessageBox.question(self, 'Sequence FM v.7.0 Copyright(c)2017 JJ Posti <techtimejourney.net>', "Sequence FM is is a python file manager, which ports the features of Crosslinker FM series to QT5 - and adds many things along way.The program comes with ABSOLUTELY NO WARRANTY  for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991.", QMessageBox.Ok )
        if buttonReply == QMessageBox.Ok:
            print('Ok clicked, messagebox closed.')           
################################
#Double left-click function
################################        
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeview_clicked(self, index):
        indexItem = self.treeview.model.index(index.row(), 0, index.parent())        
################################
#Treeviews.
################################        
        global filepath
        try:
            filepath = self.treeview.model.filePath(indexItem)
            self.address.setText(filepath)
            print (filepath)
            #Folder info
            self.info = os.stat(filepath) 
            modified=(os.path.getmtime(filepath))
            local_time =(str(time.ctime(modified)))
            self.status.showMessage(str( filepath +  "  Last modifed:  " + local_time))  

            self.treeview2.model.setRootPath(filepath)
            self.treeview2.setRootIndex(self.treeview2.model.index(filepath)) 
        except Exception as e:
            print (e)
                        
    def on_treeview2_clicked(self, index):
        global filepath2		
        indexItem = self.treeview2.model.index(index.row(), 0, index.parent())
        filepath2 = self.treeview2.model.filePath(indexItem)
        self.address.setText(filepath2)
        #File info
        self.info = os.stat(filepath2) 
        size_mb=(str(self.info.st_size / (1024 * 1024)))
        size_kb=(str("%.2f" % round(self.info.st_size / (1024.0))))
        modified=(os.path.getmtime(filepath2))
        local_time =(str(time.ctime(modified)))
        self.status.showMessage(str( filepath2 + "  Size on mb: " + size_mb + "  Size on kb:  " + size_kb + "  Last modifed:  " + local_time))  
################################
#Navigation
################################
    def navigate(self):
        try:
            self.path=self.address.text()
            if os.path.isdir(self.path):           
                self.treeview.model.setRootPath(self.path)
                self.treeview.setRootIndex(self.treeview.model.index(self.path))
                self.treeview2.model.setRootPath(self.path)
                self.treeview2.setRootIndex(self.treeview2.model.index(self.path))
                self.status.showMessage(self.path)
            else:    	
                self.status.showMessage("Not a folder path.")
            return self.path
        except Exception as e:
            print (e)			                                   
################################
#Open With program
################################
    def opens_me(self):
        text, ok = QInputDialog.getText(self, 'Open with a program', ' \n Type the name of the program, which you want to use. ')
        if ok:
            try:
                print (text)
                subprocess.Popen([text,  filepath2])                                                                        
            except Exception as e:
                print (e)                
################################
#Open external program
################################
    def opens_me2(self):
        text, ok = QInputDialog.getText(self, 'Open an external program', ' \n Type the name of the program, which you want to use. ')
        if ok:
            try:
                print (text)
                subprocess.Popen([text])                                                                        
            except Exception as e:
                print (e)	                				
################################
#Move an object 
################################            
    def move_final(self):
        try:
            list_string=(self.treeview2.selectedIndexes())
            text2, ok = QInputDialog.getText(self, 'Move to', ' \n Type the location. ')
            if ok:
                print (text2)                
            for lines in list_string:
                text = lines.data(Qt.DisplayRole)
                dir_path = os.path.dirname(os.path.realpath(filepath2))
                line='/' 
                final=dir_path + line + text
                if os.path.exists(text2):                    					
                    subprocess.Popen(["mv", final, text2])
                    self.status.showMessage(str( " Moved to: " + text2 ))                   			    		                                                                                               			                 			                        			             			    			    		
        except Exception as e:
            print ( self.status.showMessage("Moving failed."))      
################################
#Copy objects
################################            
    def paste_copy(self):
        try:
            list_string=(self.treeview2.selectedIndexes())
            text2, ok = QInputDialog.getText(self, 'Copy to', ' \n Type the location. ')
            if ok:
                print (text2)
                
            for lines in list_string:
                text = lines.data(Qt.DisplayRole)
                dir_path = os.path.dirname(os.path.realpath(filepath2))
                line='/' 
                final=dir_path + line + text
                subprocess.Popen(["cp", "-r" , final, text2])
                self.status.showMessage(str( " Copied to: " + text2 ))                   			    		                                                                                               			                 			                        			             			    			    		
        except Exception as e:
            print ( self.status.showMessage("Copying failed."))          	                        
###################
#Delete objects 
####################            
    def delete_objects(self):
        self.maketrash()			
        buttonReply = QMessageBox.question(self, 'Move objects to trash?', ' \n Press No now if you are not sure. ')
        if buttonReply == QMessageBox.Yes:
            try:
                list_string=(self.treeview2.selectedIndexes())
                for lines in list_string:
                    text = lines.data(Qt.DisplayRole)
                    dir_path = os.path.dirname(os.path.realpath(filepath2))
                    line='/' 
                    final=dir_path + line + text
                    name=getpass.getuser()
                    uhome="/home/"
                    trash="/trash"
                    combine1=uhome + name + trash
                    subprocess.Popen(["mv" , final , combine1])
                    self.status.showMessage("Objects trashed.")
            except Exception as e:
                print (e)
        if buttonReply == QMessageBox.No:
             pass                                   
################################
#Permanent delete 
################################
    def permanent_delete_objects(self):
        self.maketrash()	        			
        buttonReply = QMessageBox.question(self, 'Permanently delete  objects?', ' \n Press No now if you are not sure. ')
        if buttonReply == QMessageBox.Yes:
            try:
                list_string=(self.treeview2.selectedIndexes())
                for lines in list_string:
                    text = lines.data(Qt.DisplayRole)
                    dir_path = os.path.dirname(os.path.realpath(filepath2))
                    line='/' 
                    final=dir_path + line + text
                    subprocess.Popen(["rm" , "-r" , final])
                    self.status.showMessage("Objects permanently deleted.")                                                                        			
            except Exception as e:
                print (e)
        if buttonReply == QMessageBox.No:
            pass
###########################            				
#Keypress events
###########################        
    def keyPressEvent(self, event):
        try:
            if event.key()==Qt.Key_Delete:
                self.delete_objects()                              			                 			               
            else:
                pass
        except Exception as e:
            print ("Nothing is selected.")
################################
#Rename functions
################################                
    def rename_object(self):
        text, ok = QInputDialog.getText(self, 'Rename an object', ' \n Remember to include the extension as well - if not a folder - if in any doubt CANCEL NOW. ')
        if ok:
            try:			
                print (text)
                print ("Now:", filepath2)
                renamepath=os.path.dirname(filepath2)
                print ("Rename pathway:", renamepath)
                new_entry= renamepath + '/' + text
                print ("New object location after renaming is:", new_entry)
                subprocess.Popen(['mv', filepath2 , new_entry])
            except Exception as e:
                print("Error occured.")                                       				         
#Make new directory
    def newdir(self,widget):
        try:
            os.chdir(filepath2)
            makefolder=os.makedirs('Newfolder')
            print (os.getcwd())
            makefolder		           
        except Exception as e:
            print (e)                    			
#Make new empty text file
    def newfile(self,widget):
        try:
            os.chdir(filepath2)
            newtext=os.mknod('Newtext.txt')
            print (os.getcwd())
            newtext
        except Exception as e:
            print (e)            			        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show() 
    sys.exit(app.exec_())
