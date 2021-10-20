import os
from glob import glob
import random
import shutil

random.seed(10)
def copy_files(files_list,dest):
    os.makedirs(dest,exist_ok=True)
    # print('dest',dest)
    for i,p in enumerate(files_list):
        f = p.split("\\")[-1]
        # print('fuck:',f)
        # print(os.path.join(dest,f))
        shutil.copy(p,os.path.join(dest,f))
        # shutil.copy(p,dest+'/'+f)

datatype = 'input' # expert_C
path = './FiveK80/'+datatype
num_all = 5000
prop = [5,20,75] #proportion
# 转换
path_list = glob(path+'/*.jpg')
assert len(path_list)!=0,'path do not Exist:'+path+'/*.jpg'

path_list.sort()
random.shuffle(path_list)
s1,s2 = prop[0]/100.0,(prop[0]+prop[1])/100.0
val_list = path_list[:int(num_all*s1)]
test_list = path_list[int(num_all*s1):int(num_all*s2)]
train_list = path_list[int(num_all*s2):]
# print(val_list[0])
# 复制文件

dest_path_val = './fivek80_split/val/%s'%datatype
dest_path_test = './fivek80_split/test/%s'%datatype
dest_path_train = './fivek80_split/train/%s'%datatype

copy_files(val_list, dest_path_val)
copy_files(test_list, dest_path_test)
copy_files(train_list, dest_path_train)
