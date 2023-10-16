import cv2 as cv
import matplotlib as mat
import time
import numpy.random as rand


def gray_img(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (21,21), 0)
    edges = cv.Canny(gray, 10, 10)
    return gray

def show_frame(frame, name):
    cv.namedWindow(f'{name}', cv.WINDOW_KEEPRATIO)
    cv.imshow(f'{name}', frame)
    cv.resizeWindow(f'{name}', 1280, 800)

def draw_cnts(diff, colour, status):
    font = cv.FONT_HERSHEY_SIMPLEX
    ret, thresh = cv.threshold(diff, 3, 3, cv.THRESH_BINARY)
    thresh = cv.dilate(thresh, None, iterations = 2)
    cnts, hierarchy = cv.findContours(image=thresh.copy(), mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv.contourArea(contour) < 5000: 
            continue
        (x,y,w,h) = cv.boundingRect(contour)
        cv.rectangle(frame1, (x,y), (x+w, y+h), colour, 3)
    cv.putText(frame1, status, (1, 30), font, 1, (0,255,0), 2)
    show_frame(frame1, 'camera')

def change_st(t_start, t_end, change_clr, status, colour):
    if(t_end - t_start >= change_clr):
        if(colour == (0,255,0)):
            colour = (0,0,255)
            change_clr = rand.randint(1, 20)
            status = 'movements are prohibited'
            t_start = time.time()
        else:
            colour = (0,255,0)
            change_clr = rand.randint(1, 20)
            status = 'movements are allowed'
            t_start = time.time()
    return t_start, change_clr, status, colour



cap = cv.VideoCapture(0)
cap.set(3,1280)
t_start = time.time()
colour = (0,255,0)
change_clr = rand.randint(1, 20)
status = 'moving cathcing'
ret, frame1 = cap.read()
ret, frame2 = cap.read()
output = open("output.txt", 'w')
while ret:
    key = cv.waitKey(20) & 0xff
    gray1 = gray_img(frame1)
    gray2 = gray_img(frame2)
    diff = cv.absdiff(gray1, gray2)
    t_end = time.time()
    t_start, change_clr, status, colour = change_st(t_start, t_end, change_clr, status, colour)
    draw_cnts(diff, colour, status)
    if key == 27: # Esc
        break
    frame1 = frame2
    ret, frame2 = cap.read()
        
cv.destroyWindow('camera')
cap.release()