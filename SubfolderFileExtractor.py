import os
import shutil

currentdir=os.getcwd()
for dir in os.listdir(currentdir):
    if os.path.isdir(dir):
        subdir=os.path.join(currentdir,dir)
        for file in os.listdir(subdir):
            shutil.move(os.path.join(subdir,file),os.path.join(currentdir,file))
