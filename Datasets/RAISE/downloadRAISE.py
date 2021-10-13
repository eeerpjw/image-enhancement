# python 3
import os
import csv
import time
import datetime

def check_file_size(row, path):
    fsize = os.path.getsize(path)
    fsize = fsize/float(1024*1024)
    fsize = round(fsize+0.05,1)
    fsz_str = row[5]
    fsize_csv = float(fsz_str.split(" ")[0])
    return fsize < fsize_csv

# csv读写类
f_r = open("./RAISE_all.csv", encoding='utf-8')
f_w = open("./result.csv", 'w', encoding='utf-8')
csv_reader = csv.reader(f_r)
csv_writer = csv.writer(f_w)
prev_time = time.time()
num_row = 8156 # 文件总数，用于估计下载时间

for i,row in enumerate(csv_reader):
    # 表格第一行
    if i == 0:
        flag = 'Status'
    # 当前不存在的文件进行下载
    elif not os.path.exists(row[0]+'.NEF'):
        flag = os.system('wget -q '+row[1]) # flag==0成功
    # 跳过已经下载的文件
    elif os.path.exists(row[0]+'.NEF'):
        print("%s.NEF is already exist!"%row[0])
        flag = 0
        # continue
    # 估算下载完成时间，并打印当前下载信息
    now = time.time()
    time_left = datetime.timedelta(seconds=(num_row-i)* (now - prev_time))
    tt = time.asctime( time.localtime(now) )
    print("%s [ %d/%d ] [%s] [Flag: %s] [ETA: %s] "%(tt, i, num_row, row[0], flag, time_left))
    # 保存下载结果(flag)到新的表格
    row.append(flag)
    csv_writer.writerow(row)
    prev_time = time.time()

f_w.close()
f_r.close()

f_r = open("./RAISE_all.csv", encoding='utf-8')
csv_reader = csv.reader(f_r)
not_cnt = 0
broken_cnt =0
print("[ * ] checking files")
next(csv_reader)
for i,row in enumerate(csv_reader):
    if not os.path.exists(row[0]+'.NEF'):
        not_cnt += 1
        print("row [%d] name [%s] is not downloaded"%(i,row[0]))
    elif check_file_size(row, row[0]+'.NEF'):
        broken_cnt += 1
        print("row [%d] name [%s] is broken"%(i,row[0]))
if broken_cnt==1 and not_cnt==1:
    print("[ * ] The whole dataset is download, no broken data.")
else:
    print("[ * ] %d images are broken %d images are not downloaded"%(broken_cnt,not_cnt))
f_r.close()


