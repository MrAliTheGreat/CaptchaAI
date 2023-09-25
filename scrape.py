import os
import shutil

i = 1

for name in os.listdir("./Annotated-Dataset"):
    shutil.copy(f"./Annotated-Dataset/{name}", f"./Unannotated-Dataset/{i}.png")
    i += 1