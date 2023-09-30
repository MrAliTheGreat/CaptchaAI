import os
import shutil

folderName = ""

with open("clusters.txt", mode = "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if(i % 2):
            for img in line.split(","):
                if(img):
                    shutil.copy(img, f"./Clustered-Dataset/{folderName}")
        else:
            os.mkdir(f"./Clustered-Dataset/{line}")
            folderName = line