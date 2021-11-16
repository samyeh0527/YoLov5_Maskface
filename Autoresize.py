#Autoresize
def bboxautoresize(centery=0 ,centerx=0,x1=50,y1=150,x2=50,y2=150):
    #寬
    bboxwidth = centerx
    #高
    bboxheight = centery
    
    bboxwidth , bboxheight = int(bboxwidth),int(bboxheight)
    left_x ,left_y= int(bboxwidth/2-abs(x1)) , int(bboxheight/2-abs(y1))
    right_x , right_y = int(bboxwidth/2+x2) ,int(bboxheight/2+y2)
    return left_x,left_y,right_x,right_y

