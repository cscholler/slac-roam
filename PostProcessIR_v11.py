#!/usr/bin/env python3
# Author: Karl Parks, 2018
# Python 3 and PyQt5 Implementation

import sys
print(sys.version)

from PyQt5 import QtCore, QtGui, uic
print('Successful import of uic') #often reinstallation of PyQt5 is required

from PyQt5.QtCore import (QCoreApplication, QThread, QThreadPool, pyqtSignal, pyqtSlot, Qt, QTimer, QDateTime)
from PyQt5.QtGui import (QImage, QPixmap, QTextCursor)
from PyQt5.QtWidgets import (QWidget, QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QGridLayout, QSizePolicy, QMessageBox, QFileDialog, QSlider, QComboBox, QProgressDialog)
import numpy as np
import cv2
import h5py
from tifffile import imsave
import time
import re
print('Successful import of all libraries')
from ir_post_v2 import Ui_MainWindow

# qtCreatorFile = "ir_post_v2.ui"  # Enter UI file here.

# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import TimedAnimation
import matplotlib.animation as animation
from matplotlib import cm
import matplotlib as mpl
from matplotlib.contour import ContourSet
from matplotlib import image
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

import random
colorMapType = 0

import warnings 
warnings.filterwarnings("ignore")

from postFunctions import *

toggleUnitState = 'F' # Default unit of temperature

#Takes two inputs, 
#Checks the state to see if the max or the min is needed
#Checks the units to see if what type of unit, either Celsius or Fahrenheit, is needed
def readTemp(unit, state):
    if state == 'max': 
        if unit == 'F': 
            return (str(ktof(maxVal)) + ' ' + unit) #Returns the max temperature in Fahrenheit as a String
        elif unit == 'C': 
            return (str(ktoc(maxVal)) + ' ' + unit) #Returns the max temperature in Celsius as a String
        else:
            display('What are you asking for?') #If errors, display error message
    elif state == 'min': 
        if unit == 'F': 
            return (str(ktof(minVal)) + ' ' + unit) #Returns the min temperature in Fahrenheit as a String
        elif unit == 'C': 
            return (str(ktoc(minVal)) + ' ' + unit) #Returns the min temperature in Celsius as  a String
        else:
            display('What are you asking for?') #If errors, display error message
    elif state == 'none': 
        if unit == 'F': 
            return (str(ktof(cursorVal)) + ' ' + unit) #Returns the cursor temperature in Fahrenheit as a String
        elif unit == 'C': 
            return (str(ktoc(cursorVal)) + ' ' + unit) #Returns the cursor temperature in Celsius as  a String
        else:
            display('What are you asking for?') #If errors, display error message
    else:
        display('What are you asking for?') #If errors, display error message

#Same as readTemp but returns an int
def readTempInt(unit, state):
    if state == 'max':
        if unit == 'F':
            return ktof(maxVal)  #Returns the max temperature in Fahrenheit as a int
        elif unit == 'C':
            return ktoc(maxVal) #Returns the max temperature in Celsius as a int
        else:
            display('What are you asking for?') #If errors, display error message
    elif state == 'min':
        if unit == 'F':
            return ktof(minVal) #Returns the min temperature in Fahrenheit as a int
        elif unit == 'C':
            return ktoc(minVal) #Returns the min temperature in Celsius as a int
        else:
            display('What are you asking for?') #If errors, display error message
    elif state == 'none':
        if unit == 'F':
            return ktof(cursorVal) #Returns the cursor temperature in Fahrenheit as a int
        elif unit == 'C':
            return ktoc(cursorVal) #Returns the cursor temperature in Celsius as a int
        else:
            display('What are you asking for?') #If errors, display error message
    else:
        display('What are you asking for?') #If errors, display error message

frame = 1 # The first frame
videoState = 'notPlay'
framerate = 1 #(1/9 frames per second), do not adjust
timerHz = 115 #ms 1/8.7 = 0.1149 sec, decrease to increase speed
fileSelected = ""
usedOnce = 1

class Window(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.initUI()

	def initUI(self):
		print('Starting user interface...') 
		self.w = QWidget()

		# a figure instance to plot on
		self.figure = Figure()

		# this is the Canvas Widget that displays the `figure`
		# it takes the `figure` instance as a parameter to __init__
		self.canvas = FigureCanvas(self.figure)

		# this is the Navigation widget
		# it takes the Canvas widget and a parent
		self.toolbar = NavigationToolbar(self.canvas, self)

		# set the layout for the main window
		self.dispLayout.addWidget(self.toolbar)
		self.dispLayout.addWidget(self.canvas)

		#buttons
		self.nextFrame.clicked.connect(self.dispNextImg)
		self.prevFrame.clicked.connect(self.dispPrevImg)
		self.selectFileBut.clicked.connect(self.getFile)
		self.playVidBut.clicked.connect(self.play)
		self.makeTiffBut.clicked.connect(self.makeTiff2)
		self.displayC.clicked.connect(self.dispCDef)
		self.displayC.clicked.connect(self.displayTempValues)
		self.displayF.clicked.connect(self.dispFDef)
		self.displayF.clicked.connect(self.displayTempValues)
		self.sl.valueChanged.connect(self.slValueChange)
		self.saveCvImageBut.clicked.connect(self.saveCvImage)


		self.saveAsVideoSS.clicked.connect(self.saveVideoSS)
		self.pauseVidBut.clicked.connect(self.pauseVideo)

		# Color changing buttons
		self.cmIronBut.clicked.connect(self.cmIronFunc)
		self.cmGrayBut.clicked.connect(self.cmGrayFunc)
		self.cmRainBut.clicked.connect(self.cmRainFunc)
		self.tempScaleBut.clicked.connect(self.colorBarDisplay)


		self.timer = QTimer(self)
		self.timer.setInterval(timerHz)
		self.timer.timeout.connect(self.playVid5)
		self.timer.start()

		if (len(sys.argv) > 1):
			self.getFile()

	#cmIronFunc changes the Color of the video to ironblack
	def cmIronFunc(self):
		global colorMapType
		colorMapType = 0 #default 
		self.dispNextImg() #Goes through the next frames and changes their color
		self.dispPrevImg() #Goes through the prevous frames and changes their color
		self.history.insertPlainText('Changed Color Map\n') #Tells the user the color has been changed
		self.history.moveCursor(QTextCursor.End) #Ends something
		
	#cmRainFunc changes the Color of the video to rainbow
	def cmRainFunc(self):
		global colorMapType
		colorMapType = 1 #rainbow
		self.dispNextImg()
		self.dispPrevImg()
		self.history.insertPlainText('Changed Color Map\n')
		self.history.moveCursor(QTextCursor.End)

	#cmGrayFunc changes the Color of the video to grayscale
	def cmGrayFunc(self):
		global colorMapType
		colorMapType = 2 #grayscale
		self.dispNextImg()
		self.dispPrevImg()
		self.history.insertPlainText('Changed Color Map\n')
		self.history.moveCursor(QTextCursor.End)

	#Uses toggleUnitState to change the display temperature to Celsius
	def dispCDef(self):
		global toggleUnitState #Gets Default
		toggleUnitState = 'C' #Changes toggleUnitState to C Which changes unit to Celsius
		self.history.insertPlainText('Display ' + str(toggleUnitState) + '\n') #tells user the unit of temperature is now Celsius
		self.history.moveCursor(QTextCursor.End) #Ends something

	#Uses toggleUnitState to change the display of temperature to Fahrenheit
	def dispFDef(self):
		global toggleUnitState
		toggleUnitState = 'F'
		self.history.insertPlainText('Display ' + str(toggleUnitState) + '\n')
		self.history.moveCursor(QTextCursor.End)

	#Moves frames with the slider
	def slValueChange(self):
		global frame #Gets the default
		frame = self.sl.value() #Sets frame to slider value
		self.dispImg() # Gets the new 
		self.canvas.draw() # Redraws to the screen

	#Setups the slider
	def setSlider(self):
		global lastFrame # Set lastFrame as a variable
		self.sl.setEnabled(True) #Enable the slider
		self.sl.setMinimum(1) #Sets the min value
		self.sl.setMaximum(lastFrame) #Sets the max value
		self.sl.setValue(1) #Sets default value
		self.sl.setTickPosition(QSlider.TicksBelow) 
		self.sl.setTickInterval(9) 
		self.slStartF.setText('First Frame: 1') #Displays the below the slider the first frame of 1
		self.slMidF.setText('Mid Frame: ' + str(round(lastFrame/2))) #Displays the below the middle of the slider to whatever the middle frame is
		self.slEndF.setText('Last Frame: ' + str(lastFrame)) #Displays the below the end of the slider to whatever the last frame is
		self.slStartT.setText('0 Seconds') #Display 0 seconds in the beginning of the video
		self.slMidT.setText(str(round(lastFrame/(2*9),1)) + ' Seconds') #Display half way through the video
		self.slEndT.setText(str(round(lastFrame/9,1)) + ' Seconds') #Display how many seconds are in the whole video 

	#Saves the HDF5 video to an avi video
	def saveVideoSS(self):
		global frame # Gets frame
		global editLastFrame # Gets last frame
		global videoState # Gets the default videoState
		global fileSelected # Gets the default fileSelected which should be nothing
		videoState = 'pause' 
		if fileSelected != "": # Checks to see if a file was selected
			frame = int(self.startEdit.text()) #Sets beginning of the video 
			editLastFrame = int(self.stopEdit.text()) #Sets the end of the video
			fileNameVid = "" 
			dlgVid = QFileDialog() 
			dlgVid.setDefaultSuffix('.avi') #Adds the .avi at the end of the file making it a video file
			fileNameVid, filter = dlgVid.getSaveFileName(self.w, 'Navigate to Directory and Choose a File Name to Save To', fileSelected + '_f' + str(frame) + '-' + str(editLastFrame) + '_VIDEO.avi', 'AVI Video (*.avi)') #Changes the name of the file
			fileNameVid = str(fileNameVid) #Makes sure that fileName is a string
			fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
			if fileNameVid != "": #Checks to see if Video 
				try:
					out = cv2.VideoWriter(fileNameVid, fourcc, 8.7, (640,480), True) #
					print('past out')

					initialFrame = frame #gets the first frame
					rangeVid = editLastFrame - initialFrame #Gets the range of the frames
					pd = QProgressDialog("Operation in progress.", "Cancel", 0, 100, self); 
					pd.setWindowTitle("Creating AVI Video...") 
					pd.setWindowModality(Qt.WindowModal) 
					pd.resize(400,100) #Resizes the video size
					pd.show() 
					pd.setValue(0)
					time.sleep(0.25) #Quick pause

					for i in range(frame, editLastFrame):
						print('frame' + str(i)) #prints what frame is being captured

						percentageComplete = ((i - initialFrame)/rangeVid)*100 #Get the percentage of completion of making the video
						pd.setValue(percentageComplete) # Sets the value to the percentage of completion
						if pd.wasCanceled():#If video making is stoped everything stops
							break;

						frameForVid = self.grabDataFrame() # Grabs a frame of the video
						out.write(frameForVid) # Adds frame to the .avi video
						if frame <= editLastFrame:
							frame += framerate
						else:
							print('You are at Last Frame')
					out.release() # Once done, ends the writing of the video
					print('out release') 
					print('Saved Video As ' + str(fileNameVid)) # prints the that the video is done
					self.history.insertPlainText('SUCCESS: Saved Video\n') #Tell the user the video has been created
					self.history.moveCursor(QTextCursor.End) 

					pd.setValue(100)
					time.sleep(1)
					pd.close()

				except: # If anything fails
					self.history.insertPlainText('No AVI Video Generated\n Did Not Specify Proper FileName\n')
					self.history.moveCursor(QTextCursor.End)
					print('Did Not Specify Proper FileName')
					print('No AVI Video Generated')
			else: #No file was given a proper name
				self.history.insertPlainText('No AVI Video Generated\n Did Not Specify Proper FileName\n')
				self.history.moveCursor(QTextCursor.End)
				print('Did Not Specify Proper FileName')
				print('No AVI Video Generated')

	#Saves the frame being viewed as a png image
	def saveCvImage(self):
		global fileSelected
		global videoState
		videoState = 'pause'
		if fileSelected != "":
			dlg = QFileDialog() 
			dlg.setDefaultSuffix('.png') #Adds the .png at the end of the file making it a image file
			fileNameImage, filter = dlg.getSaveFileName(self.w, 'Navigate to Directory and Choose a File Name to Save To', fileSelected + '_f' + str(frame) + '_PNG.png', 'PNG Image (*.png)')
			if fileNameImage != "":
				try:
					print(fileNameImage)
					cv2.imwrite(str(fileNameImage),self.grabDataFrame()) # Gets the frame currently being viewed
					print('Saved frame ' + str(frame) + ' as .png')# prints that the image is done
					self.history.insertPlainText('SUCCESS: Saved Frame: ' + str(frame) + ' as PNG\n')# Tells the user the image was created
					self.history.moveCursor(QTextCursor.End)
				except: #IF anything fails 
					self.history.insertPlainText('No PNG Image Generated\n Did Not Specify Proper FileName\n')
					self.history.moveCursor(QTextCursor.End)
					print('Did Not Specify Proper FileName')
					print('No PNG Image Generated')
			else: #file was given a proper name
				self.history.insertPlainText('No PNG Image Generated\n Did Not Specify Proper FileName\n')
				self.history.moveCursor(QTextCursor.End)
				print('Did Not Specify Proper FileName')
				print('No PNG Image Generated')

	#Makes a tiff file
	def makeTiff2(self):
		global lastFrame
		global fileSelected
		global videoState
		videoState = 'pause'
		if fileSelected != "":
			dlgTiff = QFileDialog()
			dlgTiff.setDefaultSuffix('.tiff') #Adds the .tiff at the end of the file making it a tiff file
			fileNameTiff, filter = dlgTiff.getSaveFileName(self.w, 'Navigate to Directory and Choose a File Name to Save To', fileSelected + '_TIFF.tiff', 'TIFF File (*.tiff)')
			print(fileNameTiff)
			if fileNameTiff != "":
				self.history.insertPlainText('File Name Selected\n')
				self.history.moveCursor(QTextCursor.End)
				print('Collecting Data Frames...')

				initialFrame = 1 #first frame is 1
				rangeVid = lastFrame - initialFrame # gets the frame range
				pd = QProgressDialog("Operation in progress.", "Cancel", 0, 100, self);
				pd.setWindowTitle("Creating TIFF File...")
				pd.setWindowModality(Qt.WindowModal)
				pd.resize(400,100) #resizes image
				pd.show()
				pd.setValue(0)
				time.sleep(0.25)#Quick pause

				for i in range(1,lastFrame):
					print('Frame to Tiff: ' + str(i)) #Prints what frame is in the process of being add to the .tiff file

					percentageComplete = ((i - initialFrame)/rangeVid)*100 #Get the percentage of completion of making the video
					pd.setValue(percentageComplete) # Sets the value to the percentage of completion
					if pd.wasCanceled():
						break

					data = self.f_read[('image'+str(i))][:] #Gets the frame
					if i == 1:
						dataCollection = data #adds frame
					else:
						dataCollection = np.dstack((dataCollection,data)) #adds frame
					i += 1
					if i == lastFrame/2: 
						print('Half Way Through File...') # prints that the tiff file is halfway done
				print('Completed Collecting All Data Frames')
				try: #trys to save the .tiff file
					imsave((str(fileNameTiff)), dataCollection)
					print('Saved Tiff As ' + str(fileNameTiff))
					self.history.insertPlainText(' Saved Tiff\n')
					self.history.moveCursor(QTextCursor.End)
				except: #If anything fails
					self.history.insertPlainText('No Tiff File Generated\n Did Not Specify Proper FileName\n')
					self.history.moveCursor(QTextCursor.End)
					print('Did Not Specify Proper FileName')
					print('No Tiff File Generated')
				pd.setValue(100)
				time.sleep(1)
				pd.close()
			else: #file was given a proper name
				self.history.insertPlainText('No Tiff File Generated\n Did Not Specify Proper FileName\n')
				self.history.moveCursor(QTextCursor.End)
				print('Did Not Specify Proper FileName')
				print('No Tiff File Generated')
	#Gets the temperature from the location of the mouse and returns it
	def grabTempValue(self):
		global frame
		global lastFrame
		global fileSelected
		global xMouse
		global yMouse
		data = self.f_read[('image'+str(frame))][:] # Reads what frame currently being view and its temperature
		data = cv2.resize(data[:,:], (640, 480)) # Resizes the frame
		return data[yMouse, xMouse] # returns the temperature at the mouse's location

	#Displays the temperature from grabTempValue and checks if the mouse is on the screen
	def hover(self, event):
		global xMouse
		global yMouse
		global cursorVal
		if event.xdata != None:
			xMouse = int(round(event.xdata)) # Gets the mouse's x location
			yMouse = int(round(event.ydata)) # Gets the mouse's y location
			cursorVal = int(round(self.grabTempValue())) #Gets the temperature of where the mouse is
			self.cursorTempLabel.setText('Cursor Temp: ' + readTemp(toggleUnitState, 'none')) # Displays the new cursor temperature
		else:
			self.cursorTempLabel.setText('Cursor Temp: MOVE CURSOR OVER IMAGE') # mouse is not on screen 

	#Changes the displayed max and min temperature and its location on the image
	def displayTempValues(self):
		global fileSelected
		global toggleUnitState
		if fileSelected != "":
			self.maxTempLabel.setText('Current Max Temp: ' + readTemp(toggleUnitState, 'max'))# Displays the current max temperature
			self.maxTempLocLabel.setText('Max Temp Loc: ' + str(maxLoc))# Displays the max location
			self.minTempLabel.setText('Current Min Temp: ' + readTemp(toggleUnitState, 'min'))# Displays the current min temperature
			self.minTempLocLabel.setText('Min Temp Loc: ' + str(minLoc))# Displays the min location

	#Gets the Frame that is currently being view and returns it
	def grabDataFrame(self):
		global frame
		global lastFrame
		global fileSelected
		global colorMapType
		data = self.f_read[('image'+str(frame))][:] #Grabs the frame
		data = cv2.resize(data[:,:], (640, 480)) # Resizes the frame
		img = cv2.LUT(raw_to_8bit(data), generate_colour_map(colorMapType)) #Changes it color 
		img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
		rgbImage = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) 
		return(rgbImage) # Returns the frame

	#Starts the video 
	def play(self):
		global frame
		global editLastFrame
		global fileSelected
		global videoState
		self.history.insertPlainText('Play Video\n')
		self.history.moveCursor(QTextCursor.End)
		if self.startEdit.isModified(): #
			frame = int(self.startEdit.text()) # 
			print('Starting at Frame: ' + self.startEdit.text()) # 
		if self.stopEdit.isModified(): 
			editLastFrame = int(self.stopEdit.text()) # Stops if you react the last frame
		if fileSelected != "": # Starts the video 
			self.timer.start() #
			videoState = 'play'  

	#Pauses the video
	def pauseVideo(self):
		global videoState
		self.history.insertPlainText('Paused Video\n')
		self.history.moveCursor(QTextCursor.End)
		videoState = 'pause'

	#Checks to see where you are in the video
	def playVid5(self):
		global videoState
		global frame
		global lastFrame
		global editLastFrame
		if videoState == 'play':
			if editLastFrame <= lastFrame:
				if frame <= editLastFrame:
					self.sl.setValue(frame)
					if frame != lastFrame:
						frame += 1
				else:
					print('You are at Stop Frame')
					videoState = 'pause'
			else:
				print('You are at Last Frame')
				videoState = 'pause'

	#Shows the new frame in the video
	def dispNextImg(self):
		global frame
		global lastFrame
		global framerate
		global fileSelected
		global videoState
		videoState = 'pause'
		self.history.insertPlainText('Next Frame: ' + str(frame) + '\n')
		self.history.moveCursor(QTextCursor.End)
		if fileSelected != "":
			if lastFrame > frame:
				frame += framerate
			else:
				print('You are at Last Frame')
			self.sl.setValue(frame)

	#Goes back to the previous frame
	def dispPrevImg(self):
		global frame
		global fileSelected
		global videoState
		self.history.insertPlainText('Previous Frame: ' + str(frame) + '\n')
		self.history.moveCursor(QTextCursor.End)
		videoState = 'pause'
		if fileSelected != "":
			if frame > 1:
				frame -= 1
			else:
				print('You are at First Frame')
			self.sl.setValue(frame)

	#Displays the current frame of video
	def dispImg(self):
		global frame
		global lastFrame
		global fileSelected
		global maxVal
		global minVal
		global maxLoc
		global minLoc
		global colorMapType
		#if frame > 1:
			#self.cb.remove()
		#print('Display Image at Frame: ' + str(frame))
		self.currentFrameDisp.setText('Current Frame: ' + str(frame))
		data = self.f_read[('image'+str(frame))][:]
		data = cv2.resize(data[:,:], (640, 480))
		minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(data)
		img = cv2.LUT(raw_to_8bit(data), generate_colour_map(colorMapType))
		rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		#rgbImage = img #blue is hot
		self.ax = self.figure.add_subplot(111)
		self.ax.clear()
		if frame == 1:
			self.figure.tight_layout()
		self.cax = self.ax.imshow(rgbImage)
		#self.cb = self.figure.colorbar(self.cax)
		lastFrame = len(self.f_read)
		self.sl.setValue(frame)
		self.displayTempValues()
		self.currentTimeLabel.setText('Current Time: ' + str(round(((frame-1)/9.00),2)))
		cid = self.canvas.mpl_connect('motion_notify_event', self.hover)

	#Changes the Color of the Video to the color that is set
	def colorBarDisplay(self):
		global toggleUnitState
		global frame
		global colorMapType
		rgbImage = self.grabDataFrame()
		rgbImage = cv2.cvtColor(rgbImage, cv2.COLOR_BGR2RGB)
		C = generate_colour_map(colorMapType)
		C = np.squeeze(C)
		C = C[...,::-1]
		C2 = C/255.0
		ccm = ListedColormap(C2)
		fig = plt.figure()
		plt.title('Frame: ' + str(frame) + '   Max Temp: ' + readTemp(toggleUnitState, 'max'))
		bounds = [0, 50, 100]
		im = plt.imshow(rgbImage, cmap=ccm, clim=(readTempInt(toggleUnitState, 'min'), readTempInt(toggleUnitState, 'max')))
		cbar = fig.colorbar(im);
		cbar.ax.minorticks_on()
		limits = cbar.get_clim()
		cbar.set_label('     [$^\circ$' + toggleUnitState + ']', rotation=0) #270
		plt.show()

	#enables the buttons and other elements of the gui
	def enableThings(self):
		self.playVidBut.setEnabled(True)
		self.pauseVidBut.setEnabled(True)
		self.nextFrame.setEnabled(True)
		self.prevFrame.setEnabled(True)
		self.startEdit.setEnabled(True)
		self.stopEdit.setEnabled(True)
		self.saveAsVideoSS.setEnabled(True)
		self.saveCvImageBut.setEnabled(True)
		self.makeTiffBut.setEnabled(True)
		self.displayC.setEnabled(True)
		self.displayF.setEnabled(True)
		self.tempScaleBut.setEnabled(True)

	#Gets and Checks the HDF5 video file
	def getFile(self):
		global frame
		global fileSelected
		global editLastFrame
		global lastFrame
		global usedOnce
		if (len(sys.argv) > 1) and (usedOnce == 1):
			print("First file specified from command line")
			fileSelected = sys.argv[1]
			usedOnce = 0
		else:
			lastFileSelected = ""
			if fileSelected != "":
				lastFileSelected = fileSelected
			fileSelected = ""
			dlg = QFileDialog()
			dlg.setDefaultSuffix( '.HDF5' )
			fileSelected, filter = dlg.getOpenFileName(self, 'Open File', lastFileSelected, 'HDF5 (*.HDF5);; All Files (*)')
			print(fileSelected)
			self.dispSelectedFile.setText(fileSelected)
		if fileSelected != "":
			try:
				self.dispSelectedFile.setText(fileSelected)
				self.f_read = h5py.File(str(fileSelected), 'r')
				frame = 1
				self.dispImg()
				self.enableThings()
				self.setSlider()
				editLastFrame = lastFrame
				self.startEdit.setText(str(frame))
				self.stopEdit.setText(str(lastFrame))
				self.history.insertPlainText('Selected File and Displayed First Frame\n')
				self.history.moveCursor(QTextCursor.End)
				print('Selected File and Displayed First Frame')
				self.canvas.draw()
			except:
				self.history.insertPlainText('ERROR: Incorrect File Type Selected\n Please select .HDF5 File\n')
				self.history.moveCursor(QTextCursor.End)
				print('Incorrect File Type Selected. Please select .HDF5 File.')
		else:
			self.history.insertPlainText('ERROR: Incorrect File Type Selected\n Please select .HDF5 File\n')
			self.history.moveCursor(QTextCursor.End)
			print('Incorrect File Type Selected. Please select .HDF5 File.')

def main():
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
