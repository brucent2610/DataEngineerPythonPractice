import os
from pathlib import Path    

def rename_file_1(src, dst):
    os.rename(src, dst)

def rename_file_2(src, dst):
    p = Path(src)
    p.rename(dst)

rename_file_1("./files/text.txt", "./files/text2.txt")  
rename_file_2("./files/text2.txt", "./files/text.txt")  