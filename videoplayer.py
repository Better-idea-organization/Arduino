import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)


movie1 = ("/home/pi/myMedia/movie1.mp4")
movie2 = ("/home/pi/myMedia/movie2.mp4")
movie3 = ("/home/pi/myMedia/movie3.mp4")
movie4 = ("/home/pi/myMedia/movie4.mp4")
#movie5 = ("/home/pi/myMedia/movie5.mp4")
#movie6 = ("/home/pi/myMedia/movie6.mp4")
#agenda = ("/home/pi/myMedia/agenda.pdf")
slide = ("/home/pi/myMedia/ventilator.odp")

#last_state1 = True
#last_state2 = True

input_state1 = True
input_state2 = True
input_state3 = True
input_state4 = True
input_state5 = True
input_state6 = True
input_state7 = True
input_state8 = True
input_state9 = True


#os.system("loffice --impress /home/pi/Desktop/ventilator.pptx")
#os.system("e")
while True:
    
    #Read states of inputs
    input_state1 = GPIO.input(21)
    input_state2 = GPIO.input(26)
    input_state3 = GPIO.input(19)
    input_state4 = GPIO.input(5)
    input_state5 = GPIO.input(6)
    input_state6 = GPIO.input(13)
    input_state7 = GPIO.input(12)
    input_state8 = GPIO.input(20)
    input_state9 = GPIO.input(16)
    
    if not input_state1:
        os.system('killall omxplayer.bin')
        #os.system('omxplayer -b' + movie1)
        omxc = Popen(['omxplayer','--adev','hdmi','-b',movie1])
        #os.system('pkill vlc')
        #os.system('vlc --fullscreen '+movie1)
        
        sleep(1)
    if not input_state2:
        os.system('killall omxplayer.bin')
        omxc = Popen(['omxplayer','--adev','hdmi','-b',movie2])
        #os.system('omxplayer -b' + movie2)
        #omxc = Popen(['omxplayer','-b',movie2])
        sleep(1)
    if not input_state3 :
        os.system('killall omxplayer.bin')
        omxc = Popen(['omxplayer','--adev','hdmi','-b',movie3])
        sleep(1)
    if not input_state4 :
        os.system('killall omxplayer.bin')
        omxc = Popen(['omxplayer','--adev','hdmi','-b',movie4])
        sleep(1)
    if not input_state5 :
        os.system('killall omxplayer.bin')
        omxc = Popen(['loffice','--impress',slide])
        #os.system('loffice --impress /home/pi/myMedia/ventilator.pptx')
        sleep(1)
    if not input_state6 :
        os.system('killall omxplayer.bin')
        os.system('xdotool key Page_Down')
        sleep(1)
    if not input_state7 :
        os.system('killall omxplayer.bin')
        os.system('xdotool key Page_Up')
        sleep(1)
    if not input_state8 :
        os.system('killall omxplayer.bin')
        sleep(1)
    if not input_state9 :
        os.system('killall omxplayer.bin')
        sleep(1)

  