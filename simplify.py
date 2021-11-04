"""Run inference with a YOLOv5 model on images, videos, directories, streams

Usage:
    $ python path/to/detect.py --source path/to/img.jpg --weights yolov5s.pt --img 640
"""
import textwrap 
import argparse
import sys
import time 
from pathlib import Path
import random
import cv2
from numpy import empty
import torch
import torch.backends.cudnn as cudnn
import multiprocessing as mp
FILE = Path(__file__).absolute()
sys.path.append(FILE.parents[0].as_posix())  # add yolov5/ to path
from MCU_1 import Temperature_detect
from Music import music
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, colorstr, non_max_suppression, \
    apply_classifier, scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path, save_one_box
from utils.plots import colors, plot_one_box
from utils.torch_utils import select_device, load_classifier, time_sync
import argparse
import time
from Autoresize import *

soundlock =False



@torch.no_grad()
def run(weights='yolov5s.pt',  # model.pt path(s)
        source='data/images',  # file/dir/URL/glob, 0 for webcam
        imgsz=640,  # inference size (pixels)
        conf_thres=0.25,  # confidence threshold
        iou_thres=0.45,  # NMS IOU threshold
        max_det=1000,  # maximum detections per image
        device='0',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
        view_img=False,  # show results
        save_txt=True,  # save results to *.txt
        save_conf=False,  # save confidences in --save-txt labels
        save_crop=False,  # save cropped prediction boxes
        nosave=False,  # do not save images/videos
        classes=None,  # filter by class: --class 0, or --class 0 2 3
        agnostic_nms=False,  # class-agnostic NMS
        augment=False,  # augmented inference
        visualize=False,  # visualize features
        update=False,  # update all models
        project='runs/detect',  # save results to project/name
        name='exp',  # save results to project/name
        exist_ok=False,  # existing project/name ok, do not increment
        line_thickness=3,  # bounding box thickness (pixels)
        hide_labels=False,  # hide labels
        hide_conf=False,  # hide confidences
        half=False,  # use FP16 half-precision inference
        noise=0.05,
        Run_buffer = None,
        main_buffer_golab =None,
        locks=None,
        sound_bools=None
        ):
    save_img = not nosave and not source.endswith('.txt')  # save inference images
    webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
        ('rtsp://', 'rtmp://', 'http://', 'https://'))

    # Directories
    save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

    # Initialize
    set_logging()
    device = select_device(device)
    half &= device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    w = weights[0] if isinstance(weights, list) else weights
    classify, pt, onnx = False, w.endswith('.pt'), w.endswith('.onnx')  # inference type
    stride, names = 64, [f'class{i}' for i in range(1000)]  # assign defaults
    if pt:
        model = attempt_load(weights, map_location=device)  # load FP32 model
        stride = int(model.stride.max())  # model stride
        names = model.module.names if hasattr(model, 'module') else model.names  # get class names
        if half:
            model.half()  # to FP16
        if classify:  # second-stage classifier
            modelc = load_classifier(name='resnet50', n=2)  # initialize
            modelc.load_state_dict(torch.load('resnet50.pt', map_location=device)['model']).to(device).eval()
    elif onnx:
        check_requirements(('onnx', 'onnxruntime'))
        import onnxruntime
        session = onnxruntime.InferenceSession(w, None)
    imgsz = check_img_size(imgsz, s=stride)  # check image size

    # Dataloader
    if webcam:
        view_img = check_imshow()
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz, stride=stride)
        bs = len(dataset)  # batch_size
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride)
        bs = 1  # batch_size
    vid_path, vid_writer = [None] * bs, [None] * bs

    # Run inference
    if pt and device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
    t0 = time.time()
    
    TemperatureWork = None
    Run_buffer = 0
    for path, img, im0s, vid_cap ,timestamp in dataset:       
        if pt:
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            print()
        elif onnx:
            img = img.astype('float32')
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if len(img.shape) == 3:
            img = img[None]  # expand for batch dim

        # Inference
        t1 = time_sync()
        if pt:
            visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if visualize else False
            pred = model(img, augment=augment, visualize=visualize)[0]
            

        elif onnx:
            pred = torch.tensor(session.run([session.get_outputs()[0].name], {session.get_inputs()[0].name: img}))

        # NMS
        pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)
        t2 = time_sync()

        # Second-stage classifier (optional)
        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Process predictions
        for i, det in enumerate(pred):  # detections per image
            if webcam:  # batch_size >= 1
                p, s, im0, frame = path[i], f'{i}: ', im0s[i].copy(), dataset.count
                showcls= f''
            else:
                p, s, im0, frame = path, '', im0s.copy(), getattr(dataset, 'frame', 0)
                showcls= f''
            p = Path(p)  # to Path
            save_path = str(save_dir / p.name)  # img.jpg
            txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')  # img.txt
            s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            imc = im0.copy() if save_crop else im0  # for save_crop
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string
                    showcls += f" {names[int(c)]} {n}"
                    wrapped_text = textwrap.wrap(showcls, width=17)
                # Write results
                for *xyxy, conf, cls in reversed(det):        
                    if save_txt:  # Write to file
                        c1, c2 = (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3]))

                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        
                        line = (cls, *xywh, conf) if save_conf else (cls, *xywh)  # label format
                        classnumber = ('%g ' * len(line)).rstrip() % line
                        classnumber = classnumber.split(' ')
                        c1, c2 = list(c1),list(c2)
                        with open(txt_path + '.txt', 'a') as f:
                            #f.write(('%g ' * len(line)).rstrip() % line + '\n')
                            f.write(classnumber[0]+' '+ classnumber[1] +' '+ str(c1[0]) +' '+ str(c1[1]) +' '+ str(c2[0]) +' ' + str(c2[1]) + '\n')                    
                    if save_img or save_crop or view_img:  # Add bbox to image
                        Run_buffer+=1
                        #c1 = xy left top ,c2 = xy2 right bottom
                        c1, c2 = (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3]))
                        print(imc.shape[0],imc.shape[1])
                        x_1 , y_1 ,x_2,y_2= bboxautoresize(y = imc.shape[0],x = imc.shape[1])
                        bboxCenter = [x_1, y_1, x_2, y_2]
                        bbox_2 = [c1[0], c1[1], (c2[0]-c1[0]), (c2[1]-c1[1])]
                        bbox_1 = [x_1, y_1, (x_2-x_1), (y_2-y_1)]
                        #calculator iou 
                        iou = get_iou(bbox_1, bbox_2)
                        
                        # main_buffer_golab
                        if main_buffer_golab != None :
                            if len(main_buffer_golab) > 100 and Run_buffer >100 :
                                    main_buffer_golab[:-15] = []
                                    Run_buffer = 0
                                    print('clean buffer and buffer running count ')
                                #detece the people in the box and main_buffer_golab is not empty with Run_buffer Remainder of division 25 is 0
                            elif iou >= 0.9 and Run_buffer == 25 or iou >= 0.9 and Run_buffer % 25 == 0:
                                    TemperatureWork = '{:.2f}'.format(main_buffer_golab.pop())
                                    print('update temperature')            
                                    Run_buffer = 0
                                #detece the people in the box and main_buffer_golab is empty both Run_buffer of 25
                            elif iou >= 0.3 and not main_buffer_golab and Run_buffer == 25:
                                    Run_buffer = 0
                                    print('warring ...!!')
                                    continue
                                #Make noise
                            elif int(cls) != 0  :
                                    locks.value = 0
                                    sound_bools.append(True)
                                    
                                #detect the people but didn't in the box
                            elif iou >= noise and int(cls) != 0  :
                                    locks.value = 0
                                    sound_bools.append(True)
                                    
                        c = int(cls)  # integer class
                        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                        #set center location
                        c1, c2 = (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3]))
                        cv2.rectangle(im0, (bboxCenter[0], bboxCenter[1]), (bboxCenter[2], bboxCenter[3]), (0, 255, 0), 2) 
                        plot_one_box(xyxy, im0, label=label, color=colors(c, True), line_thickness=line_thickness,TemperatureWork=TemperatureWork)
                        #left top write text 
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        font_size = 1
                        font_thickness = 2
                        for i_local, line in enumerate(wrapped_text):
                            textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]
                            gap = textsize[1] + 10
                            y = 30+ i_local * gap
                            cv2.putText(im0, line, (3, y), font,
                                        font_size, 
                                        (0,0,255), 
                                        font_thickness, 
                                        lineType = cv2.LINE_AA)
                        if save_crop:
                            save_one_box(xyxy, imc, file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)

            # Print time (inference + NMS)
            print(f'{s}Done.. ({t2 - t1:.3f}s)')

            # Stream results
            if view_img:
                cv2.namedWindow(str(p), cv2.WINDOW_NORMAL)
                cv2.imshow(str(p), im0)
                cv2.waitKey(1)  # 1 millisecond

            # Save results (image with detections)
            if save_img:
                if dataset.mode == 'image':
                    cv2.imwrite(save_path, im0)
                else:  # 'video' or 'stream'
                    if vid_path[i] != save_path:  # new video
                        vid_path[i] = save_path
                        if isinstance(vid_writer[i], cv2.VideoWriter):
                            vid_writer[i].release()  # release previous video writer
                        if vid_cap:  # video
                            fps = vid_cap.get(cv2.CAP_PROP_FPS)
                            w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                            h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        else:  # stream
                            fps, w, h = 30, im0.shape[1], im0.shape[0]
                            save_path += '.mp4'
                        vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                    vid_writer[i].write(im0)
                    
    if save_txt or save_img:
        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
        print(f"Results saved to {colorstr('bold', save_dir)}{s}")

    if update:
        strip_optimizer(weights)  # update model (to fix SourceChangeWarning)
    
    print(f'Done. ({time.time() - t0:.3f}s)')


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='./best.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='https://www.youtube.com/watch?v=R2iMq5LKXco', help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--imgsz', '--img', '--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
    # parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')

    opt = parser.parse_args()
    return opt


#HC add
def get_iou(bbox_ai, bbox_gt):
    iou_x = max(bbox_ai[0], bbox_gt[0]) # x
    iou_y = max(bbox_ai[1], bbox_gt[1]) # y
    iou_w = min(bbox_ai[2]+bbox_ai[0], bbox_gt[2]+bbox_gt[0]) - iou_x # w
    iou_w = max(iou_w, 0)
    iou_h = min(bbox_ai[3]+bbox_ai[1], bbox_gt[3]+bbox_gt[1]) - iou_y # h
    iou_h = max(iou_h, 0)

    iou_area = iou_w * iou_h
    all_area = bbox_ai[2]*bbox_ai[3] + bbox_gt[2]*bbox_gt[3] - iou_area
    IoU = max(iou_area/all_area, 0)

    return IoU


#HC add
def Daemon_buffer(queue_,main_buffer_golab):
    
    while True:
        # getTemp = Temperature_detect(7).Temperature_get()
        getTemp =  random.randint(36,38)
        queue_.put(getTemp)
        main_buffer_golab.append(queue_.get())
        if len(main_buffer_golab) >= 3500 : 
            main_buffer_golab[:1500]=[]
        time.sleep(1)
    
def sound_deamon(queue_,sound_bools,locks):
    while True:

        if locks.value == 1 and not sound_bools:
            sound_bools.append(False)
        elif locks.value == 0 and sound_bools is not empty : 
            sound_bool = sound_bools.pop()
            music(sound_bool).withoutmask()  
            locks.value = 1
        elif len(sound_bools) > 3:
            sound_bools[:1] = []


def main(opt,Temperature_lock,noise_lock):
    if Temperature_lock and noise_lock is True: 
        print(colorstr('detect: ') + ', '.join(f'{k}={v}' for k, v in vars(opt).items()))
        check_requirements(exclude=('tensorboard', 'thop'))
        run(**vars(opt))


if __name__ == "__main__":
    # pass
    # # Process
    # manager = mp.Manager()
    # queue_ = mp.Queue()  
    # #Process share format list 
    # main_buffer_golab = manager.list()
    # sound_bools = manager.list()
    # locks = manager.Value('d',1)
    # #Default Bools 
    # sound_bools.append(False)  
    # # Set Process1 Process2  
    # process_1 = mp.Process(target=Daemon_buffer , args=(queue_,main_buffer_golab),daemon=True)
    # process_2 = mp.Process(target=sound_deamon , args=(queue_,sound_bools,locks),daemon=True)
 
    # # # Run
    # opt = parse_opt()
    # main(opt)

    pass