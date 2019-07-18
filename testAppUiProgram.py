import sys, os
import pantilthat
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer

from PyQt5 import uic, QtCore, QtGui, QtWidgets
from testAppUi import Ui_MainWindow

# Decleration of global variables
anglePan = 0		# Angle of pantilt Pan servo, range: [-90,90]
angleTilt = 0		# Angle of pantilt Tilt servo, range: [-90,90]
alpha = 5			# Overlay balance of cameras, range: [0, 10]
checkWebcam = False	# Stores state if camera location has been checked

# Decleration of camera specs
RGB = [0,0] 		# Determined from inputs
IR = [160, 120] 	# Determined by user
GUI = [0,0]			# Determined from testAppUi.py

# Initialize pantilt modules
def setup():
	# Global variables to be used
	global anglePan
	global angleTilt

	# Enable the pantilt servos
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

# Definition of Warning and Exit dialog window
class exitDialog(QDialog):
    def __init__(self):
        super(exitDialog,self).__init__()
        uic.loadUi('exitDialog.ui',self)
        self.exitButton.clicked.connect(self.exitProgram)

    def exitProgram(self):
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) #restart
        # print("Program closed.")
        # exit()

# Definition of Servo Error dialog window
class servoErrorWindow(QDialog):
	def __init__(self):
		super(servoErrorWindow,self).__init__()
		uic.loadUi('servoErrorWindow.ui',self)

# Definition of Camera Wrror dialog window
class camErrorWindow(QDialog):
    def __init__(self):
        super(camErrorWindow,self).__init__()
        uic.loadUi('camErrorWindow.ui',self)

# Definition of primary app window functionality
class AppGUI(Ui_MainWindow):

	# Dialog button commands
	def __init__(self, dialog):
		Ui_MainWindow.__init__(self)
		self.setupUi(dialog)
 
    # Listeners enabling UI functionality

		# Implemention of pantilt controller's buttons
		self.upButton.clicked.connect(self.moveUp)
		self.downButton.clicked.connect(self.moveDown)
		self.leftButton.clicked.connect(self.moveLeft)
		self.rightButton.clicked.connect(self.moveRight)
		self.LEDSlider.valueChanged.connect(self.LEDBrightness)
		
		#Implementaion of pantilt error resolution dialogs
		self.servoerror.clicked.connect(self.servo_error)
		self.camerror.clicked.connect(self.cam_error)

		# Implementation of overlay balancer
		self.balancer.valueChanged.connect(self.opacityValue)

		# Enable camera functiality
		self.timer = QTimer()
		self.timer.timeout.connect(self.viewCam)
		self.startcamButton.clicked.connect(self.controlTimer)

    # UI Button command functions

	# Shows the Exit dialog when camera(s) is unplugged unexpectedly
	def warning(self):
		self.warn = exitDialog()
		self.warn.show()
	
	# Start RGB and IR camera overlay feed
	def viewCam(self):
		# Global variables to be used
		global checkWebcam
		global alpha
		global RGB
		global IR
		global GUI
		
		GUI[0] = self.camlabel.frameGeometry().width()
		GUI[1] = self.camlabel.frameGeometry().height()

		ratio = 1.1  # Ratio of camera's FOV

		# Determine which camera was attached first
		if checkWebcam == False: # IR camera was attached first
			RGB[0] = self.wcam2
			RGB[1] = self.hcam2
		elif checkWebcam == True: # RGB camera was attached first
			RGB[0] = self.wcam1
			RGB[1] = self.hcam1

		# Scaling factor for IR camera dimentions to GUI dimentions
		if int(GUI[0] / IR[0]) > int(GUI[1] / IR[1]):
			IRScale = GUI[1] / IR[1]
		else: 
			IRScale = GUI[0] / IR[0]

		# Scaling factor for RGB camera dimensions to GUI dimensions
		if int(GUI[0] / RGB[0]) > int(GUI[1] / RGB[1]):
			RGBScale = GUI[1] / RGB[1]
		else: 
			RGBScale = GUI[0] / RGB[0]

		# Calculations for adjusting RGB camera feed for difference of FOV, POV, and image size
		RGBCor = [0, 0, 0, 0, 0, 0]  # Array to store values for correcting RGB input

		RGBCor[0] = round(RGB[0] * RGBScale * ratio)	# Expand x dimention by FOV ratio
		RGBCor[1] = round(RGB[1] * RGBScale * ratio)	# Expand y dimention by FOV ratio
		RGBCor[2] = int((RGBCor[0] - GUI[0]) / 2)  		# Determine x crop start
		RGBCor[3] = int(RGBCor[0] - RGBCor[2])			# Determine x crop end
		RGBCor[4] = int((RGBCor[1] - GUI[1]) / 2)  		# Determine y crop start
		RGBCor[5] = int(RGBCor[1] - RGBCor[4])			# Determine y crop end

		# Calculations for adjusting IR camera feed for difference of POV and image size
		IRCor = [0, 0, 0, 0, 0, 0] # Array to store values for correcting RGB input

		IRCor[0] = round(IR[0] * IRScale)						# Expand x dimention by camera dimention ratio
		IRCor[1] = round(IR[1] * IRScale)						# Expand x dimention by camera dimention ratio
		IRCor[2] = int((IRCor[0] - IRCor[1]*(GUI[0]/GUI[1]))/2)	# Determine x crop start
		IRCor[3] = IRCor[0] - IRCor[2]							# Determine x crop end
		IRCor[4] = 0											# Determine y crop start
		IRCor[5] = IRCor[1]										# Determine y crop end

		# Define camera locations for future use
		ret, framecam1 = self.cam1.read()	# framecam1 assigned to first camera attached
		ret2, framecam2 = self.cam2.read()	# framecam2 assigned to second camera attached

		# Camera image correction loop
		try: 
			# Check two cameras are attached
			framecam1 = cv2.cvtColor(framecam1, cv2.COLOR_BGR2RGB)
			framecam2 = cv2.cvtColor(framecam2, cv2.COLOR_BGR2RGB)
		except:
			# Print error and launch dialoge box if less than two cameras are attached 
			print("warning: Camera is disconnected unexpectedly!")
			
			self.timer.stop()
			self.cam1.release()
			self.cam2.release()
			self.startcamButton.setText("Error. Please Restart and Try Again")
			self.warning()
		else:
			if checkWebcam == True:	# Complete loop if RGB camera is registered as first camera atached
				# Correct RGB feed for difference of FOV, POV, and image size
				resize_cam1 = cv2.resize(framecam1 , (RGBCor[0] , RGBCor[1]))
				cropped_cam1 = resize_cam1[RGBCor[4] : RGBCor[5] , RGBCor[2] : RGBCor[3]]
				
				# Correct IR feed for difference of FOV, POV, and image size
				resize_cam2 = cv2.resize(framecam2 , (IRCor[0] , IRCor[1]))
				cropped_cam2 = resize_cam2[IRCor[4] : IRCor[5] , IRCor[2] : IRCor[3]]

				# Overlay camera feeds and scale for GUI display
				beta = 10 - alpha	# Calculate opacity for IR camera
				image = cv2.addWeighted(cropped_cam1, (alpha*.1),cropped_cam2, (beta*.1), 0.0)	# Overlay camera feeds
				
			elif checkWebcam == False: # Complete loop if IR camera is registered as first camera attached
				# Correct IR feed for difference of FOV, POV, and image size
				resize_cam1 = cv2.resize(framecam1 , (IRCor[0] , IRCor[1]))
				cropped_cam1 = resize_cam1[IRCor[4] : IRCor[5] , IRCor[2] : IRCor[3]]
               
			    # Correct RGB feed for difference of FOV, POV, and image size
				resize_cam2 = cv2.resize(framecam2 , (RGBCor[0] , RGBCor[1]))
				cropped_cam2 = resize_cam2[RGBCor[4] : RGBCor[5] , RGBCor[2] : RGBCor[3]]

				# Overlay camera feeds and scale for GUI display
				beta = 10 - alpha	# Calculate opacity for IR camera
				image = cv2.addWeighted(cropped_cam2, (alpha*.1), cropped_cam1, (beta*.1), 0.0)	# Overlay camera feeds
				
			resizedimage = cv2.resize(image, (GUI[0], GUI[1]))	# Scale overlayed image for GUI

			# Store overlayed and scaled image dimetions for display use
			height, width, channel = resizedimage.shape
			step = channel * width

			# Create QImage from overlayed and scaled image
			qImg = QImage(resizedimage.data, width, height, step, QImage.Format_RGB888)

			# Display overlayed image in UI
			self.camlabel.setPixmap(QPixmap.fromImage(qImg))

	# Start/stop timer for RGB and IR camera overlay feed
	def controlTimer(self):
		# Global variables to be used
		global checkWebcam
		global RGB
		global IR

		# If cameras overlay feed is inactive
		if not self.timer.isActive():
			# Open IR and RGB cameras to check order attached
			self.cam1 = cv2.VideoCapture(0)
			self.cam2 = cv2.VideoCapture(1)

			# Check IR and RGB cameras could be opened
			if self.cam1.isOpened() and self.cam2.isOpened():
				self.wcam1 = int(self.cam1.get(3))	# Store cam1 width
				self.hcam1 = int(self.cam1.get(4))	# Store cam1 height
				self.wcam2 = int(self.cam2.get(3))	# Store cam2 width
				self.hcam2 = int(self.cam2.get(4))	# Store cam2 height
				
				# Compare input dimentions to expected dmentions to determine attachment order
				if self.wcam1 == IR[0] and self.hcam1 == IR[1]:
					checkWebcam = False # IR camera was attached first
					print("IR cam is received first")
				elif self.wcam2 == IR[0] and self.hcam2 == IR[1]:
					checkWebcam = True # RGB camera was attached first and RGB camera was attached second
					print("Webcam is received first")
				else: 
					print("One or more cameras are not of expected resolution")
			
			# Check if IR or RGB camera could not be opened
			if not self.cam1.isOpened() or not self.cam2.isOpened():
				# Release cameras to be checked and restarted
				self.cam_error()
				self.cam1.release()
				self.cam2.release()
			# If IR and RGB cameras could be opened
			else:
				# start timer
				self.timer.start(20)
                # update startcamButton text
				self.startcamButton.setText("Stop")
				print("Cameras opened successfully!")

		# If camera overlay feed is active
		else:
			# stop timer
			self.timer.stop()

            # release video capture
			self.cam1.release()
			self.cam2.release()

            # update startcamButton text
			self.startcamButton.setText("Start Camera")
			print("Cameras stopped!")

	# Pantilt controller tilt up
	def moveUp(self):
		# Global variables to be used
		global angleTilt

		if angleTilt > -90: 			# Move only if tilt angle is greater than servo lower bound
			angleTilt -= 10				# Adjust tilt angle by 10 degrees
			pantilthat.tilt(angleTilt)	# Update tilt servo position

	# Pantilt controller tilt down
	def moveDown(self):
		# Global variables to be used
		global angleTilt

		if angleTilt < 90:				# Move only if tilt angle is less than servo upper bound
			angleTilt += 10				# Adjust tilt angle by 10 degrees
			pantilthat.tilt(angleTilt)	# Update tilt servo position

	# Pantilt controller pan left
	def moveLeft(self):
		# Global variables to be used
		global anglePan

		if anglePan < 90:				# Move only if pan angle is less than servo upper bound
			anglePan += 10				# Adjust pan angle by 10 degrees
			pantilthat.pan(anglePan)	# Update pan servo postion

	# Pantilt controller pan right
	def moveRight(self):
		# Global variables to be used
		global anglePan

		if anglePan > -90:				# Move only if pan angle is greater than servo lower bound
			anglePan -= 10				# Adjust pan angle by 10 degrees
			pantilthat.pan(anglePan)	# Update pan servo position

	# Pantilt LED brigtness adjustment
	def LEDBrightness(self):
		sV = self.LEDSlider.value()		# Store value of slider, range [0,255]
		pantilthat.set_all(sV,sV,sV,sV)	# Set all LEDs to stored slider value
		pantilthat.show() 				# Update LED bar values		

	# Overlay opacity adjustment					
	def opacityValue(self):
		# Global variables to be used
		global alpha

		alpha = self.balancer.value()	# Set RGB and IR overlay to slider value, range [0,10]

	# Call dialog box for servo error
	def servo_error(self):
		self.servoerr = servoErrorWindow()	# Call servo error dialog box
		self.servoerr.show()				# Display servo error dialog box

	# Call dialof box for camera error
	def cam_error(self):
		self.camerr = camErrorWindow()	# Call camera error dialog box
		self.camerr.show()				# Display camera error dialog box

if __name__ == '__main__':
	# Create program application and dialog
	app = QtWidgets.QApplication(sys.argv)
	window = QMainWindow()
	
	# Initialize pantilt modules
	setup()
	
	# Create program GUI
	prog = AppGUI(window)
 
	# Show program GUI
	window.show()
	sys.exit(app.exec_())
