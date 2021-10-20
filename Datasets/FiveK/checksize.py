import os
from glob import glob
from PIL import Image
path = "./fivek80_split"
split_list = ["val",'test','train']
folder_lst = ["expert_A","expert_B","expert_C","expert_D","expert_E","input"]

mw,mh = 30000,30000# mh代表长边
for s in split_list:
    print(s)
    input_img_lst = glob(os.path.join(path,s,"input/*.jpg"))
    for p in input_img_lst:
        img = Image.open(p)
        w,h = img.size
        if (w<h and w<512):
            print("rm .\\fivek80_split\\*\\*\\%s"%p.split("\\")[-1])
            continue
        elif h<w and h<512:
            print("rm .\\fivek80_split\\*\\*\\%s"%p.split("\\")[-1])
            continue
        if w<h and mh>h:
            mh=h
            print("mh",mh,p)
        elif w>=h and mh>w:
            mh = w
            print("mh",mh,p)
        if w<h and mw>w:
            mw = w
            print("mw",mw,p)
        elif w>=h and mw>h:
            mw = h
            print("mw",mw,p)

print("长边,短边",mh,mw)

for s in split_list:
    print(s)
    input_img_lst = glob(os.path.join(path,s,"input/*.jpg"))
    input_img_lst.sort()
    img_name_lst = [[p.replace("input",x) for x in folder_lst] for p in input_img_lst]
    for x in img_name_lst:
        pa,pb,pc,pd,pe,pii = x
        a = Image.open(pa)
        wa,ha = a.size
        b = Image.open(pb)
        wb,hb = b.size
        c = Image.open(pc)
        wc,hc = c.size
        d = Image.open(pd)
        wd,hd = d.size
        e = Image.open(pe)
        we,he = e.size
        ii = Image.open(pii)
        wii,hii = ii.size
        if wa!=wb:
            print("w", pa,pb )
        elif wb!=wc:
            print("w", pb,pc )
        elif wc!=wd:
            print("w", pc,pd)
        elif wd!=we:
            print("w", pd,pii)
        elif we!=wii:
            print("w",pe,pii)
        
        if ha!=hb:
            print("h", pa,pb )
        elif hb!=hc:
            print("h", pb,pc )
        elif hc!=hd:
            print("h", pc,pd)
        elif hd!=he:
            print("h", pd,pii)
        elif he!=hii:
            print("h",pe,pii)





