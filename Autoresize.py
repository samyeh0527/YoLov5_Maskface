#Autoresize
from numpy import right_shift
from screeninfo import get_monitors
def bboxautoresize():
    bbox = None
    for m in get_monitors():
        # print(str(m))
        # print(type(m))
        bbox = str(m)
    bbox = bbox.split(',')
    bboxwidth = bbox[2]
    bboxheight = bbox[3]
    bboxwidth = bboxwidth.replace('width=','')
    bboxheight = bboxheight.replace('height=','')
    bboxwidth , bboxheight = int(bboxwidth),int(bboxheight)
    left_x ,left_y= int(bboxwidth/2-400) , int(bboxheight/2-150)
    right_x , right_y = int(bboxwidth/2+250) ,int(bboxheight/2+50)
    return left_x,left_y,right_x,right_y
a ,a1,b,b1 = bboxautoresize()
