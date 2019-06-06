#importing all libraries

from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
import time
import cv2
import numpy as np
import os


#making window and intialising the mixer lib
root= Tk()
mixer.init()
root.title("sujeet")
root.iconbitmap(r'C:\\Users\\sujeet boran\\Desktop\\11.ico')
photo=PhotoImage(file='C:\\Users\\sujeet boran\\Desktop\\play.png')