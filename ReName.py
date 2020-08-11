#比對xlsx清單中內容 對照名稱後變更檔名

import shutil
import os
from os.path import join
import pandas as pd

HomePath = 'D:/graplib/'
print('輸入目的資料夾路徑:')
tar = input()
TarPath = HomePath + tar +'/'


M = pd.read_excel('D:/graplib/rnlist.xlsx')

oname = M['Name']
nname = M['ReName']
count = 0

for i in oname:
    count = count + 1
    for j in os.listdir(TarPath):
        #print('尋找目的資料夾中的'+i)
        FullPath = join(TarPath, j)
        FileName = join(j)
        if i in FileName:
              os.rename(TarPath+FileName, TarPath+nname[count-1]+'.png')
              print('找到 '+FileName+'更名為 '+ nname[count-1]+'.png')




#for i in data['dir']:

# HomePath  = 'D:/graplib/'
#
# #DestPath  = 'D:/graplib/0_English/' #目標目錄
# DestPath  = 'D:/graplib/'+KEYWORD+'/' #目標目錄
# StandPath = 'D:/graplib/stand/useless/'
# UPath = DestPath + 'useless'
# AllFiles = os.listdir(DestPath)
# UFiles = os.listdir(StandPath)
# #print(AllFiles)
#
# #print('請輸入檔案關鍵字:')
# #KEYWORD = input()
#
# for i in UFiles:
#     TARGET = i[2:]
#     for j in AllFiles:
#         FullPath = join(DestPath, j)
#         FileName = join(j)
#         if TARGET in FileName:
#             if not os.path.exists(UPath):
#                 os.mkdir(UPath)
#             print('將 '+FileName+' 移動至useless資料夾')
#             shutil.move(FullPath, UPath)
#
#
