import os
import random
import shutil

# 选择指定数量影像移动（非复制）
def movefile(sourceDir, targetDir, movenumber):
    pathDir = os.listdir(sourceDir) 
    filenumber = len(pathDir)
    targetfile = random.sample(pathDir, movenumber) 
    for name in targetfile:
        shutil.move(sourceDir + "\\" + name, targetDir + "\\" + name)

# 删除重复项
def removefile(labDir,imgDir):
    # 获取列表
    fileD={}
    for root,dirs,files in os.walk(labDir):
        for f in files:
            if f=="classes.txt":
                continue
            fib=f.split('_')
            temp={int(fib[0]):[fib[1],fib[2]]}
            fileD.update(temp)
    fileDic={}
    for key in sorted(fileD):
        fileDic[key]=fileD[key]
    # 确定删除列表
    compareList=[]
    saveIDs=[]
    removeIDs=[]
    for k in fileDic:
        if fileDic[k] in compareList:
            removeIDs.append(k)
        else:
            saveIDs.append(k)
        compareList.append(fileDic[k])
    # 删除文件
    pathDir = os.listdir(labDir) 
    for name in pathDir:
        if name =="classes.txt":
            continue
        fid=int(name.split('_')[0])
        if fid in removeIDs:
            rf=os.path.join(labDir,name)
            os.remove(rf)

    # pathDir = os.listdir(imgDir) 
    # for name in pathDir:
    #     fid=int(name.split('_')[0])
    #     if fid in removeIDs:
    #         rf=os.path.join(imgDir,name)
    #         print(rf)
    #         os.remove(rf)
    # print("fin")

# 统计数据信息
def stadata(sourceDir):
    mysta={0:0,1:0,2:0,3:0}
    print(mysta)
    for root,dirs,files in os.walk(sourceDir):
        for f in files:
            if f=="classes.txt":
                continue
            filepath=os.path.join(root,f)
            for line in open(filepath):
                id=int(line.split(' ')[0])
                mysta[id]=mysta[id]+1
    print(mysta)
                
                
# 删除非影像    
def removeimage(labDir,imgDir):
    # 获取列表
    saveIDs=[]
    for root,dirs,files in os.walk(labDir):
        for f in files:
            if f=="classes.txt":
                continue
            fib=f.split('_')
            saveIDs.append(fib[0])
    print(len(saveIDs))

    pathDir = os.listdir(imgDir) 
    for name in pathDir:
        fid=name.split('_')[0]
        if fid not in saveIDs:
            rf=os.path.join(imgDir,name)
            print(rf)
            os.remove(rf)
    print("fin")



if __name__=="__main__":
    #  # 用于从指定文件夹中移动选定数量的文件
    #  sourceDir = ''
    #  targetDir = ''
    #  number=5000
    #  movefile(sourceDir, targetDir, number)

    # 数据清理
    # labDir=''
    # imgDir=''
    # removefile(labDir,imgDir)

    # 统计自定义数据集
    # sourceDir=''
    # stadata(sourceDir)

    labDir=''
    imgDir=''
    removeimage(labDir,imgDir)