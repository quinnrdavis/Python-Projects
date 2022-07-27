import os

fPath = "F:\\Repos\\GitHub\\Python-Projects\\file-io\\challenge"

fileList = os.listdir(fPath)

txtList = []

for i in fileList:
    if i.find('.txt') > 0:
        txtList.append(i)

for i in txtList:
    abPath = os.path.join(fPath, i)
    print(abPath)
    print(os.path.getmtime(abPath))




        
