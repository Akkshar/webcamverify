import dropbox
import random
import time
import cv2
import pydrive

starttime = time.time()

def snapshot():
    number = random.randint(0,100)
    capture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = capture.read()
        imagename = "img"+str(number)+".png"
        cv2.imwrite(imagename, frame)
        starttime = time.time()
        result = False
    
    return imagename
    print("snapshot taken")
    capture.release()
    cv2.destroyAllWindows()
    
def uploadfiles(imagename):
        access_token = 'ZP8Jp8XxHdkAAAAAAAAAASUOaBlJV5WvwOQObkUcbGZTtagXQJfdCVMRykCPTM26'
        file = imagename
        file_to = "/testfolder"+(imagename)
        drbox = dropbox.Dropbox(access_token)
        f = open(file, 'rb')
        drbox.files_upload(f.read(),file_to, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")
    
def name():
    result = True
        while(result):
            if(time.time()-starttime>=5):
                candy = snapshot()
                uploadfiles(candy)
                result = False

name()
