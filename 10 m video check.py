from glob import glob
import numpy as np
import cv2

root_path='images folder/videos/*'

ten_min_video_folder_list=[]

s_f_n_video_name={}

for file in glob(root_path):
    folder_wos_total_frame=0

    video_path=file+"/*.mp4"
    for each_folder in glob(video_path):
        cap=cv2.VideoCapture(each_folder)

        total_frame = int(cap.get(7))
        fps = int(cap.get(5))

        each_sec = total_frame / fps

        folder_wos_total_frame +=each_sec
        if folder_wos_total_frame >= 600:
            folder_nam=each_folder.split('/')[-2]
            ten_min_video_folder_list.append(folder_nam)
            break

path='images folder/videos/'

for folder_name in ten_min_video_folder_list:
    s_path =path+folder_name+'/*.mp4'
    for video_name in glob(s_path):
        f_n=video_name.split('/')[-2]
        v_n=video_name.split('/')[-1]

        if not f_n in s_f_n_video_name:
            s_f_n_video_name[f_n]=[]
        else:
            s_f_n_video_name[f_n].append(v_n)

print(s_f_n_video_name)
