#Autoresize
def bboxautoresize(y=0 ,x=0):
    bboxheight = y
    bboxwidth = x
    
    bboxwidth , bboxheight = int(bboxwidth),int(bboxheight)
    left_x ,left_y= int(bboxwidth/2-50) , int(bboxheight/2-150)
    right_x , right_y = int(bboxwidth/2+50) ,int(bboxheight/2+150)
    return left_x,left_y,right_x,right_y


# video_size1,video_size2 = 1080,1920
# left_x,left_y,right_x,right_y = bboxautoresize(video_size1,video_size2 )

# print(left_x,left_y,right_x,right_y)