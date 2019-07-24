#!/usr/bin/env python3
# Author: Karl Parks, 2018

from PyQt5 import QtCore, QtGui, uic
print('Successful import of uic') #often reinstallation of PyQt5 is required

from PyQt5.QtCore import (QCoreApplication, QThread, QThreadPool, pyqtSignal, pyqtSlot, Qt, QTimer, QDateTime)
from PyQt5.QtGui import (QImage, QPixmap, QTextCursor)
from PyQt5.QtWidgets import (QWidget, QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QGridLayout, QSizePolicy, QMessageBox, QFileDialog, QSlider, QComboBox, QProgressDialog)
from PyQt5.QtWidgets import QInputDialog, QDialog, QLineEdit
import sys
import os.path

import cv2
from tifffile import imsave
import numpy as np
import h5py
import time
import psutil
from uvctypesParabilis_v2 import *
from multiprocessing  import Queue
import threading
import pantilthat
from subprocess import call

from postFunctions import *
from ir_v11 import Ui_MainWindow
from servoErrorWindow import Ui_servoErrorWindow
from camErrorWindow import Ui_camerrorwindow

print('Loaded Packages and Starting IR Data...')

# qtCreatorFile = "ir_v11.ui"  # Enter file here.
postScriptFileName = "PostProcessIR_v11.py"

# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Global variable decleration
anglePan = 0        # Angle of pantilt Pan servo, range [-90,90]
angleTilt = 0       # Angle of pantilt Titlt servo, range [-90,90]

BUF_SIZE = 2        # Maximum size of Queue used for threading
q = Queue(BUF_SIZE) # Constructor of Queue q

# Initialize pantilt modules
def pantiltSetup():
    # Global varables to be used
    global anglePan
    global angleTilt

    # Enable pantilt servos
    pantilthat.servo_enable(1, True)
    pantilthat.servo_enable(2, True)

    # Center pantilt camera
    pantilthat.pan(anglePan)
    pantilthat.tilt(angleTilt)

    # Set up pantilt LED
    pantilthat.light_type(pantilthat.RGBW)
    pantilthat.light_mode(pantilthat.WS2812)
    pantilthat.set_all(0,0,0,0)
    pantilthat.show()

# Definition of Servo Error dialog window
class servoErrorWindow(QDialog):
    def __init__(self):
        super(servoErrorWindow, self).__init__()
        # uic.loadUi('servoErrorWindow.ui', self)
        self.ui = Ui_servoErrorWindow()
        self.ui.setupUi(self)

# Definition of Camera Error dialog window
class camErrorWindow(QDialog):
    def __init__(self):
        super(camErrorWindow, self).__init__()
        # uic.loadUi('camErrorWindow.ui', self)
        self.ui = Ui_camerrorwindow()
        self.ui.setupUi(self)

# Function for frame storage
def py_frame_callback(frame, userptr):
    array_pointer = cast(frame.contents.data, POINTER(c_uint16 * (frame.contents.width * frame.contents.height)))
    data = np.frombuffer(
        array_pointer.contents, dtype=np.dtype(np.uint16)).reshape(frame.contents.height, frame.contents.width)
    if frame.contents.data_bytes != (2 * frame.contents.width * frame.contents.height):
        return
    if not q.full():
        q.put(data)

# Call of stored frames
PTR_PY_FRAME_CALLBACK = CFUNCTYPE(None, POINTER(uvc_frame), c_void_p)(py_frame_callback)

# Function that finds and opens the thermal camera using libuvc
def startStream():
    global devh
    # Pointers usef to initialization of VC service context
    ctx = POINTER(uvc_context)()
    dev = POINTER(uvc_device)()
    devh = POINTER(uvc_device_handle)()
    ctrl = uvc_stream_ctrl()

    # Initialize a UVC service context
    res = libuvc.uvc_init(byref(ctx), 0)
    if res < 0:
        print("uvc_init error")
    # Attempt to locate thermal camera
    try:
        res = libuvc.uvc_find_device(ctx, byref(dev), PT_USB_VID, PT_USB_PID, 0)
        if res < 0:
            print("uvc_find_device error")
            exit(1)
        # Attempt to open thermal camera
        try:
            res = libuvc.uvc_open(dev, byref(devh))
            if res < 0:
                print("uvc_open error")
                exit(1)

            print("device opened!")

            print_device_info(devh)
            print_device_formats(devh)

            # Format frame with expected format
            frame_formats = uvc_get_frame_formats_by_guid(devh, VS_FMT_GUID_Y16)
            # Insure themal camera supports correct format
            if len(frame_formats) == 0:
                print("device does not support Y16")
                exit(1)

            # Retrieve and format thermal camera stream
            libuvc.uvc_get_stream_ctrl_format_size(devh, byref(ctrl), UVC_FRAME_FORMAT_Y16,
                frame_formats[0].wWidth, frame_formats[0].wHeight, int(1e7 / frame_formats[0].dwDefaultFrameInterval)
            )

            # Begin streaming from thermal camera
            res = libuvc.uvc_start_streaming(devh, byref(ctrl), PTR_PY_FRAME_CALLBACK, None, 0)
            if res < 0:
                print("uvc_start_streaming failed: {0}".format(res))
                exit(1)

            print("done")
            print_shutter_info(devh)

        # When thermal camera cannot be opened print message
        except:
            print('Failed to Open Device')
    # When thermal camera cannot be found print message and exit
    except:
        print('Failed to Find Device')
        exit(1)

# Displayed temperature unit
toggleUnitState = 'F'

# Kelvin to Ferinheight conversion
def ktof(val):
    return round(((1.8 * ktoc(val) + 32.0)), 2)

# Kelvin to Celsius conversion
def ktoc(val):
    return round(((val - 27315) / 100.0), 2)

# Function to display tempurature in Kelvin - I don't think this is actually being used
def display_temperatureK(img, val_k, loc, color):
    val = ktof(val_k)                                                                           # Convert given temp value to 
    cv2.putText(img,"{0:.1f} degF".format(val), loc, cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)  # Place text
    x, y = loc                                                                                  # x and y location of display temperature                                                                                  
    cv2.line(img, (x - 2, y), (x + 2, y), color, 1)                                             # location of first drawn line
    cv2.line(img, (x, y - 2), (x, y + 2), color, 1)                                             # location of second drawn line

# Function to display tempurature in Celsius - I don't think this is actually being used
def display_temperatureC(img, val_k, loc, color):
    val = ktof(val_c)                                                                           # Convert given temp value to celsius
    cv2.putText(img,"{0:.1f} degC".format(val), loc, cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)  # Place text
    x, y = loc                                                                                  # x and y location of display temperature
    cv2.line(img, (x - 2, y), (x + 2, y), color, 1)                                             # location of first drawn line
    cv2.line(img, (x, y - 2), (x, y + 2), color, 1)                                             # location of second drawn line
    print("running")

# Convert raw image format to 8bit image format
def raw_to_8bit(data):
    cv2.normalize(data, data, 0, 65535, cv2.NORM_MINMAX)    # Normalise data to facilitate conversion
    np.right_shift(data, 8, data)                           # Shifts data for conversion
    return cv2.cvtColor(np.uint8(data), cv2.COLOR_GRAY2RGB) # Return image converted from gray scale to RGB

# Secondary global variable declaration
camState = 'not_recording'  # Camera recording state storage
tiff_frame = 1              # Frame key storage
maxVal = 0                  # Maximum temperature visable in frame              
minVal = 0                  # Minimum temperature visable in frame

# Functions that starts recording and identifies the file path 
@pyqtSlot(QImage)
def startRec():
    global camState
    global saveFilePath
    
    # Check if camera is recording already
    if camState == 'recording':
        print('Already Recording')
    # Setting up file path and file name when not recording yet
    else:
        file_nameH = str(('Lepton HDF5 Vid ' + QDateTime.currentDateTime().toString()))
        file_nameH = file_nameH.replace(" ", "_")
        file_nameH = str(file_nameH.replace(":", "-"))
    # Starts recording and writing the recorded filename
    try:
        filePathAndName = str(saveFilePath + '/' + file_nameH)
        startRec.hdf5_file = h5py.File(filePathAndName, mode='w')
        camState = 'recording'
        print('Started Recording')
    # If the above fails
    except:
        print('Incorrect File Path')
        camState = 'not_recording'
        print('Did Not Begin Recording')

# Functions that converts a frame's data into an image
def getFrame():
    global tiff_frame
    global camState
    global maxVal
    global minVal
    data = q.get(True, 500) # Data format for dataset
    if data is None:
        print('No Data')
    # If recording is active
    if camState == 'recording':
        # Gets the data of each frame
        startRec.hdf5_file.create_dataset(('image'+str(tiff_frame)), data=data)
        tiff_frame += 1
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(data)
    # Generates the frame into an image and return it
    img = cv2.LUT(raw_to_8bit(data), generate_colour_map(0))
    return img 

# Reads temperature returns the correct value
def readTemp(unit, state):
    # Reads the maximum temperature
    if state == 'max':
        if unit == 'F':
            return (str(ktof(maxVal)) + ' ' + unit)
        elif unit == 'C':
            return (str(ktoc(maxVal)) + ' ' + unit)
        else:
            print('What are you asking for?')
    # Reads the minimum temperature
    elif state == 'min':
        if unit == 'F':
            return (str(ktof(minVal)) + ' ' + unit)
        elif unit == 'C':
            return (str(ktoc(minVal)) + ' ' + unit)
        else:
            print('What are you asking for?')
    # Reads the temperature at the cursor's location
    elif state == 'none':
        if unit == 'F':
            return (str(ktof(cursorVal)) + ' ' + unit)
        elif unit == 'C':
            return (str(ktoc(cursorVal)) + ' ' + unit)
        else:
            print('What are you asking for?')
    else:
        print('What are you asking for?')

# Changes Fahrenheit label to Celsius label
def updateMaxTempLabel():
    if toggleUnitState == 'F':
        return ktof(maxVal)
    elif toggleUnitState == 'C':
        return ktoc(maxVal)
    else:
        print('No Units Selected')

# Initializes variables for the overlay process
# Determined to be changed later
alpha = 5   # RGB Camera opacity
beta = 5    # IR Camera opacity

# Class that includes the streaming functionality
class MyThread(QThread):
    changePixmap = pyqtSignal(QImage)
    def run(self):
        global alpha
        global beta

        print('Start Stream')
        
        # Trying to open the webcam
        onWebcam = False
        print("Trying to open webcam ...")

        webCamPort = 0          # Default webcam port
        webCamFound = False     # Storage of webcam located state

        # Locate webcam from ports 0-5
        while webCamFound == False and webCamPort <= 5:
            self.cam = cv2.VideoCapture(webCamPort)
            # If webcam is not located at current port relase that port and check next
            if not self.cam.isOpened():
                self.cam.release()
                webCamPort += 1
            # Exit loop when cam is found or ports 0-5 are checked
            else:
                webCamFound = True

        # Checking if the webcam is connected
        if not self.cam.isOpened():
            self.cam.release()
            print("Cannot open webcam")
            # If webcam isn't opened, will show the thermal camera only
            print("Showing the thermal camera only ...")
            onWebcam = False

        else:
            print("Webcam opened!")
            print("Showing both cameras ...")
            onWebcam = True

        # While camera stream is running overlay cameras
        while True:
            frame = getFrame() # Getting the thermal camera frame
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Converts the thermal frame into an image
            resizedIR = cv2.resize(rgbImage, (640, 480)) # Resize so that they have the same size
            rows,cols,c = resizedIR.shape
            # If the webcam is on, shows the overlay
            if onWebcam == True:
                framecam = self.getWebcamFrame() # Getting the webcam's frame
                camImage = cv2.cvtColor(framecam, cv2.COLOR_BGR2RGB) # Converts the webcam frame into an image
                rotatedCam = cv2.flip(camImage, -1) # Flip the webcam image
                resizedCam = cv2.resize(rotatedCam, (640, 480)) # Resizes webcam image
                # resizedCam.set(cv2.CAP_PROP_FPS, 9)
                M = np.float32([[1,0,30],[0,1,-5]])
                dst = cv2.warpAffine(resizedIR,M,(cols,rows))
                # Creates overlay image
                image = cv2.addWeighted(resizedCam, (alpha*.1), dst, (beta*.1), 0.0)	# Overlay camera feeds

                # Getting the overlay image info
                h, w, channel = image.shape
                step = channel * w
                # Uses the info above to convert the image into the Qt format
                convertToQtFormat = QImage(image.data, image.shape[1], image.shape[0], step, QImage.Format_RGB888)
            
            # If the webcam is not on, shows the resized IR camera
            elif onWebcam == False: 
                convertToQtFormat = QImage(resizedIR.data, resizedIR.shape[1], resizedIR.shape[0], QImage.Format_RGB888)

            self.changePixmap.emit(convertToQtFormat) # Emits the image in Qt format

        self.cam.release() # WHen the application is done, release the webcam
    
    # Getting webcam frame
    def getWebcamFrame(self):
        ret, frameread = self.cam.read() # Reads each frame info and returns
        return frameread
        
thread = "unactive"
saveFilePath = ""
fileNamingFull = ""
bFile = ""
class App(QMainWindow, Ui_MainWindow):
    # Setting up the UI of the main window
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()
        print('Always Run This Script as ADMIN')

    # Putting the "image" (the overlay image of two webcams) into the UI frame
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.displayFrame.setPixmap(QPixmap.fromImage(image))

    # Setting up the UI components
    def initUI(self):
        # Using global keyword to modify the following variables that were created outside of the function
        global fileNamingFull   
        global anglePan
        global angleTilt

        # Connecting the buttons to their assigned functions
        self.startRec.clicked.connect(self.startRec2)
        self.stopRec.clicked.connect(self.stopRecAndSave)
        self.startRec.clicked.connect(self.displayRec)
        self.stopRec.clicked.connect(self.displayNotRec)
        self.displayC.clicked.connect(self.dispCDef)
        self.displayF.clicked.connect(self.dispFDef)
        self.runPost.clicked.connect(self.runPostScript)
        self.startStreamBut.clicked.connect(self.startThread)
        self.displayFrame.mousePressEvent = self.on_press

        self.w = QWidget()
        self.filePathBut.clicked.connect(self.getFiles)

        # time display
        self.timer = QTimer(self)
        self.timerFast = QTimer(self)
        self.timer.setInterval(1000)
        self.timerFast.setInterval(10)
        self.timer.timeout.connect(self.displayTime)
        self.timer.timeout.connect(self.displayStorage)
        self.timerFast.timeout.connect(self.displayTempValues)
        self.timer.start()
        self.timerFast.start()

        # Naming video file
        defaultName = 'IR_HDF5'
        fileNamingFull = defaultName

        # Allowing user to name the video
        self.lineEdit.setText(defaultName)
        self.lineEdit.textChanged.connect(self.fileNaming)

        # FFC Mode and Set Gain State
        self.ffcBut.clicked.connect(self.ffcFunction)
        self.comboGain.currentTextChanged.connect(self.gainFunction)
        self.comboFFCmode.currentTextChanged.connect(self.FFCmodeFunction)

        # Implementation of pantilt controller's buttons
        # _state = 0
        self.upButton.clicked.connect(self.moveUp)
        self.downButton.clicked.connect(self.moveDown)
        self.leftButton.clicked.connect(self.moveLeft)
        self.rightButton.clicked.connect(self.moveRight)
        self.LEDSlider.valueChanged.connect(self.LEDBrightness)

        # Implementation of overlay balancer
        self.balancer.valueChanged.connect(self.opacityValue)

        # Implementation of pantilt error resolution dialogs
        self.servoerror.clicked.connect(self.servo_error)
        self.camerror.clicked.connect(self.cam_error)

    # Overlay opacity adjustment					
    def opacityValue(self):
        # Global variables to be used
        global alpha
        global beta
        alpha = self.balancer.value()
        beta = 10 - alpha

    # Function for the Set Gain State button
    def gainFunction(self):
        global devh
        global thread
        if thread == 'active':
            if (self.comboGain.currentText() == 'LOW'):
                set_gain_low(devh)
            elif (self.comboGain.currentText() == 'HIGH'):
                set_gain_high(devh)
                #print('Cannot set to back to HIGH yet')
            else:
                set_gain_auto(devh)
                #print('Cannot set to AUTO')

    # Setting text and functionality of the FFC Mode
    def FFCmodeFunction(self):
        global devh
        global thread
        if thread == 'active':
            if (self.comboFFCmode.currentText() == 'MANUAL'):
                set_manual_ffc(devh)
            elif (self.comboFFCmode.currentText() == 'EXTERNAL'):
                set_external_ffc(devh)
            else:
                set_auto_ffc(devh)
                #print('Cannot set to back to AUTO yet. Unplug USB from Raspberry Pi to reset lepton.')
        print_shutter_info(devh)

    # Enable the FFC Mode
    def ffcFunction(self):
        global devh
        global thread
        if thread == 'active':
            perform_manual_ffc(devh)

    # Setting up how the video will be saved and its filename
    def startRec2(self):
        global thread
        global camState
        global saveFilePath
        global fileNamingFull
        # Saving the video happens only when the thread is active
        if thread == 'active':
            if camState == 'recording': # No action needed when recording
                print('Already Recording') 
            else:
                # If the video's name is empty
                if fileNamingFull != "":
                    # Setting up file's path and ready to be named
                    dateAndTime = str(QDateTime.currentDateTime().toString())
                    dateAndTime = dateAndTime.replace(" ", "_")
                    dateAndTime = dateAndTime.replace(":", "-")
                    filePathAndName = str(fileNamingFull + '_' + dateAndTime + '.HDF5')
                    print(filePathAndName)
                    self.filePathDisp.setText(filePathAndName)

                    # Starts generating the filename when being recorded based on the current time
                    try:
                        # Specifying a filepath for the video when starting to record
                        startRec.hdf5_file = h5py.File(filePathAndName, mode='w')
                        camState = 'recording'
                        print('Started Recording')
                        if saveFilePath == "":
                            self.history.insertPlainText('Saved ' + str(filePathAndName) + ' to ' + os.path.dirname(os.path.abspath(__file__)) + '\n')
                            self.history.moveCursor(QTextCursor.End)
                        else:
                            self.history.insertPlainText('Saved to ' + str(filePathAndName) + '\n')
                            self.history.moveCursor(QTextCursor.End)

                    # If the file path is invalid, the recording fails
                    except:
                        print('Incorrect File Path')
                        camState = 'not_recording'
                        print('Did Not Begin Recording')

                # The video is not named if not recording
                else:
                    print('No FileName Specified')
        # If the thread is not active, user will need to open camera in order to record
        else:
            print('Remember to Start Stream')
            self.history.insertPlainText('Remember to Start Stream\n')
            self.history.moveCursor(QTextCursor.End)

    # Saving file after recording
    def stopRecAndSave(self):
    	global tiff_frame
    	global camState
    	if tiff_frame > 1:
    		print('Ended Recording')
    		camState = 'not_recording'
    		try:
                # Ending the recording
    		    startRec.hdf5_file.close()
    		    print('Saved Content to File Directory')
    		except:
    		    print('Save Failed')
    		tiff_frame = 1
    	else:
            # Reminding user to start recording to save the video
    		camState = 'not_recording'
    		print('Dont Forget to Start Recording')
    		self.history.insertPlainText('Dont Forget to Start Recording\n')
    		self.history.moveCursor(QTextCursor.End)

    # Naming the file
    def fileNaming(self):
    	global fileNamingFull
    	bFile = str(self.lineEdit.text())
    	if saveFilePath == "":
    		fileNamingFull = bFile
    		self.filePathDisp.setText('/' + bFile + ' ... Date & Time Will Append at Recording Start')
    	elif saveFilePath != "":
    		fileNamingFull = saveFilePath + '/' + bFile
    		self.filePathDisp.setText(saveFilePath + '/' + bFile + ' ... Date & Time Will Append at Recording Start')
    	else:
    		print('I am Confused')

    # Starts streaming the cameras
    def startThread(self):
        global thread
        try:
            # if cameras are not on
            if thread == "unactive":
                # Tries opening the cameras and streaming
                try:
                    startStream()                                   # Finding and opening the thermal camera
                    self.th = MyThread()                            # Calling the MyThread class which opens the webcam and puts the two cameras' frames into images
                    self.th.changePixmap.connect(self.setImage)     # Putting the overlay image into the UI frame by connecting it with the setImage function
                    self.th.start()                                 # Starts showing the image
                    thread = "active"                               # Thread status changed
                    print('Starting Thread')
                # If cannot open device, streaming fails
                except:
                    print('Failed!!!!')
                    exit(1)
            else:
                print('Already Started Camera')
    	# If cannot open cameras, show a message box informing the unavailability
        except:
            msgBox = QMessageBox()
            reply = msgBox.question(self, 'Message', "Error Starting Camera - Plug or Re-Plug Camera into Computer, Wait at Least 10 Seconds, then Click Ok and Try Again.", QMessageBox.Ok)
            print('Message Box Displayed') 
            # If user clicks ok confirming
            if reply == QMessageBox.Ok:
                print('Ok Clicked')
            else:
                event.ignore()

    # Running the Post Process file
    def runPostScript(self):
    	try:
    		def thread_second():
    	    		call(["python3", postScriptFileName])
    		processThread = threading.Thread(target=thread_second)  # <- note extra ','
    		processThread.start()
    	except:
    		print('Post Processing Script Error - Most Likely Referencing Incorrect File Name')

    # Displaying the temperature in Celsius
    def dispCDef(self):
    	global toggleUnitState
    	toggleUnitState = 'C'
    	self.history.insertPlainText('Display ' + str(toggleUnitState) + '\n')
    	self.history.moveCursor(QTextCursor.End)

    # Displaying the temperature in Fahrenheit
    def dispFDef(self):
    	global toggleUnitState
    	toggleUnitState = 'F'
    	self.history.insertPlainText('Display ' + str(toggleUnitState) + '\n')
    	self.history.moveCursor(QTextCursor.End)

    # Displaying the maximum temperature and the minimum temperature
    def displayTempValues(self):
        global toggleUnitState
        self.maxTempLabel.setText('Current Max Temp: ' + readTemp(toggleUnitState, 'max'))
        self.minTempLabel.setText('Current Min Temp: ' + readTemp(toggleUnitState, 'min'))

    # Displaying the current date and time
    def displayTime(self):
        self.timeStatus.setText(QDateTime.currentDateTime().toString())

    # Grabbing the current temperature at the cursor's location
    def grabTempValue(self):
        # Getting the frames and cursor's location
        global xMouse
        global yMouse
        global thread
        # If the cameras are on and streamming is active
        if thread == 'active':
            data = q.get(True, 500) 
            data = cv2.resize(data[:,:], (640, 480))    # Putting the data in frame 640 by 480
            return data[yMouse, xMouse]                 # Returns the temperature value at the cursor's location
        else:
            self.history.insertPlainText('ERROR: Please Start IR Camera Feed First\n')
            self.history.moveCursor(QTextCursor.End)

    # Displaying the temperature on mouse click
    def on_press(self, event):
        global xMouse
        global yMouse
        global cursorVal
        try:
            xMouse = event.pos().x()            # Receiving the x coordination of the cursor
            yMouse = event.pos().y()            # Receiving the y coordination of the cursor
            cursorVal = self.grabTempValue()    # Assigning the current temperature at the cusor to cursorVal
            self.cursorTempLabel.setText('Cursor Temp (On Mouse Click): ' + readTemp(toggleUnitState, 'none'))
        # If cannot get the temperature value at the cursor
        except:
            self.history.insertPlainText('ERROR: Please Start IR Camera Feed First\n')
            self.history.moveCursor(QTextCursor.End)

    # Displaying the recording time allowed / storage
    def displayStorage(self):
        usage = psutil.disk_usage('/')
        oneMinVid = 20000000
        timeAvail = usage.free/oneMinVid
        self.storageLabel.setText('Recording Time Left: ' + str(round(timeAvail, 2)) + ' Minutes')

    # Displaying the start recording status
    def displayRec(self):
    	if camState == 'recording':
            	self.recLabel.setText('Recording')
    	else:
    	   self.recLabel.setText('Not Recording')

    # Displaying the stop recording status
    def displayNotRec(self):
        if camState == 'not_recording':
            self.recLabel.setText('Not Recording')
        else:
            self.recLabel.setText('Recording')

    # Setting up the file path
    def getFiles(self):
    	global saveFilePath
    	saveFilePath = QFileDialog.getExistingDirectory(self.w, 'Open File Directory', '/')
    	self.filePathDisp.setText(saveFilePath)
    	self.fileNaming()

    # Setting up the function for when closing the application
    def closeEvent(self, event):
        print("Close Event Called")

        # If user closes the application when recording
        if camState == 'recording':
            # A message box shows up, asking if they want to close
            reply = QMessageBox.question(self, 'Message',
                                         "Recording still in progress. Are you sure you want to quit?", QMessageBox.Yes, QMessageBox.No)
            print('Message Box Displayed')
            # If they confirm yes, the closing event is accepted
            if reply == QMessageBox.Yes:
                print('Exited Application, May Have Lost Raw Data')
                event.accept()
            # Else the closing event is ignored and the application will stay opened
            else:
                event.ignore()
        # If the application is not recording, the closing event is accepted and the application exits 
        else:
            print('Exited Application')
            event.accept()

    # Call dialog box for servo error
    def servo_error(self):
        self.servoerr = servoErrorWindow()  # Call servo error dialog box
        self.servoerr.show()                # Display servo error dialog box

    # Call dialog box for camera error
    def cam_error(self):
        self.camerr = camErrorWindow()  # Call camera error dialog box
        self.camerr.show()              # Display camera error dialog box

    # Pantilt controller tilt up
    def moveUp(self):
       # Global variable to be used
        global angleTilt

        if self.upButton.isEnabled():       # Check if button is currently held down
            if angleTilt > -90:             # Move only if current position is greater than servo lower bound
                angleTilt -= 10             # Adjust tilt angle by 10 degrees
                pantilthat.tilt(angleTilt)  # Update tilt servo position
      
    # Pantilt controller tilt down
    def moveDown(self):
        # Global variable to be used
        global angleTilt

        if self.downButton.isEnabled():     # Check if button is currently held down
            if angleTilt < 90:              # Move only if current position is less than servo upper bound
                angleTilt += 10             # Adjust tilt angle by 10 degrees
                pantilthat.tilt(angleTilt)  # Update tilt servo positon

    # Pantilt controller pan left
    def moveLeft(self):
        # Global variable to be used
        global anglePan

        if self.leftButton.isEnabled():     # Check if button is currently held down
            if anglePan < 90:               # Move only if current position is less than servo upper bound
                anglePan += 10              # Adjust pan angle by 10 degrees
                pantilthat.pan(anglePan)    # Update pan servo position

    # Pantilt controller pan right
    def moveRight(self):
        # Global variable to be used
        global anglePan

        if self.rightButton.isEnabled():    # Check if button is currently held down
            if anglePan > -90:              # Move only if current position is greater than servo upper bound
                anglePan -= 10              # Adjust pan angle by 10 degrees
                pantilthat.pan(anglePan)    # Update pan servo position

    # Pantilt LED brightness adjustment
    def LEDBrightness(self):
        sV = self.LEDSlider.value()         # Store value of slider, range [0,255]
        pantilthat.set_all(sV, sV, sV, sV)  # Set all LEDs to stored slider value
        pantilthat.show()                   # Update LED bar values

def main():
    app = QApplication(sys.argv)
    pantiltSetup()                  # Initialize pantilt modules
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
