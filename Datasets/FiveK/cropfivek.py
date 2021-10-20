from PIL import Image
from glob import glob
import numpy as np
import random
import os

#from numpy.lib.npyio import save

def crop_across_same_image(path,crop_size,path_replace,save_path_replace):
    # abcdei
    # 打开
    folder_lst = ["input","expert_A","expert_B","expert_C","expert_D","expert_E"]
    input_img_lst = glob(os.path.join(path,'input','*.jpg'))
    input_img_lst.sort()
    print(len(input_img_lst))
    img_name_lst = [[p.replace("input",x) for x in folder_lst] for p in input_img_lst]
    cnt = 0
    not_processed_lst = []
    for name_lst in img_name_lst:
        for name in name_lst:
            img = Image.open(name)
            # crop
            w,h = img.size
            if h/w<1:
                # print("h/w<1")
                if h<crop_size:
                    print("[ ! ] h<crop_size %s"%name,h,w)
                    cnt += 1
                    not_processed_lst.append(name)
                    continue
                else:
                    c_h = round(h/2.0)
                    s_h,e_h = c_h-crop_size/2,c_h+crop_size/2
                if w > 2*crop_size:
                    q_w = round(w/4.0)
                    s_w1,e_w1 = q_w-crop_size/2,q_w+crop_size/2
                    s_w2,e_w2 = q_w*3-crop_size/2,q_w*3+crop_size/2
                else:# w <= 2*crop_size:
                    s_w1,e_w1 = 0,crop_size
                    s_w2,e_w2 = w-crop_size,w
                # print("img1:",h,w,"--",(s_w1,s_h,e_w1,e_h))
                # print("img2:",h,w,"--",(s_w2,s_h,e_w2,e_h))
                img1 = img.crop((s_w1,s_h,e_w1,e_h))
                img2 = img.crop((s_w2,s_h,e_w2,e_h))
            if h/w >= 1:
                # print("h/w >= 1")
                if w<crop_size:
                    print("[ ! ] w<crop_size %s"%name,h,w)
                    not_processed_lst.append(name)
                    cnt += 1
                    continue
                else:
                    c_w = round(w/2.0)
                    s_w,e_w = c_w-crop_size/2,c_w+crop_size/2
                if h>2*crop_size:
                    q_h = round(h/4.0)
                    s_h1,e_h1 = q_h-crop_size/2,q_h+crop_size/2
                    s_h2,e_h2 = q_h*3-crop_size/2,q_h*3+crop_size/2
                else: # h <= 2*crop_size
                    s_h1,e_h1 = 0,crop_size
                    s_h2,e_h2 = h-crop_size,h
                # print("img1:",h,w,"--",(s_w,s_h1,e_w,e_h1))
                # print("img2:",h,w,"--",(s_w,s_h2,e_w,e_h2))
                img1 = img.crop((s_w,s_h1,e_w,e_h1))
                img2 = img.crop((s_w,s_h2,e_w,e_h2))
            os.makedirs(os.path.dirname(name.replace(path_replace,save_path_replace)),exist_ok=True)
            img1.save(name.replace(path_replace,save_path_replace).replace(".jpg","_a.jpg"))
            img2.save(name.replace(path_replace,save_path_replace).replace(".jpg","_b.jpg"))
    print(cnt)
    [print(x) for x in not_processed_lst]

if __name__=="__main__":
    path ='./fivek80_split'
    save_path = './fivek80_split_corpped'
    os.makedirs(save_path,exist_ok=True)
    crop_size = 512
    lst = ["val","train","test"]
    for x in lst:
        p = os.path.join(path,x)
        crop_across_same_image(path=p,
                            crop_size=crop_size,
                            path_replace=path.split("/")[-1],
                            save_path_replace=save_path.split("/")[-1]
                            )



