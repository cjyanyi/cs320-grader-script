# -*- coding:UTF-8 -*-

import os
import csv
def create_csv(rows):
    path = "results.csv"
    with open(path,'wb') as f:
        csv_write = csv.writer(f)
        csv_head = ["Repo name","test passes", 'test failed']
        csv_write.writerow(csv_head)
        csv_write.writerows(rows)



path = "./" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s=[]
for file in files: #遍历文件夹
     if os.path.isdir(file):
          f = open(path+file+'/assignments/week3/test_result_grader.txt') #打开文件
          iter_f = iter(f); #创建迭代器
          
          for line in iter_f: #遍历文件，一行行遍历，读取文本
              if line.find('tests failed')>0:
                  s.append([file, str(33-int(line[:2])), line[:2]])
create_csv(s)


