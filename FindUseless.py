#比對目標資料夾內檔案是否符合useless資料夾中檔案 名稱相符則移動至useless資料夾

import shutil
import os
from os.path import join

HomePath  = 'D:/graplib/'

print('請輸入目標資料夾路徑: ')
KEYWORD = input()


#DestPath  = 'D:/graplib/0_English/' #目標目錄
DestPath  = 'D:/graplib/'+KEYWORD+'/' #目標目錄
StandPath = 'D:/graplib/stand/useless/'
UPath = DestPath + 'useless'
AllFiles = os.listdir(DestPath)
UFiles = os.listdir(StandPath)
#print(AllFiles)

#print('請輸入檔案關鍵字:')
#KEYWORD = input()

for i in UFiles:
    TARGET = i[2:]
    for j in AllFiles:
        FullPath = join(DestPath, j)
        FileName = join(j)
        if TARGET in FileName:
            if not os.path.exists(UPath):
                os.mkdir(UPath)
            print('將 '+FileName+' 移動至useless資料夾')
            shutil.move(FullPath, UPath)



# for i in AllFiles:
#     FullPath = join(MyPath, i) # 獲取檔案完整路徑
#     FileName = join(i) # 獲取檔案名稱
#     DestPath = (MyPath +'/'+ KEYWORD)
#     #print (FullPath)
#     #print (FileName)
#     if KEYWORD in FileName:
#       if not os.path.exists(MyPath +'/'+ KEYWORD +'/'+ FileName):
#         if not os.path.exists(DestPath):
#           os.mkdir(MyPath+'/'+KEYWORD)
#           print ('建立 "'+KEYWORD+'" 資料夾...')
#         shutil.move(FullPath, MyPath+'/'+KEYWORD)
#         print ('成功將', FileName, '移動至', KEYWORD, '資料夾')
#       else :
#         print (FileName, '已存在，故不執行動作')
#     else:
#       print(FileName, '檔案不符合關鍵字', KEYWORD)
#
