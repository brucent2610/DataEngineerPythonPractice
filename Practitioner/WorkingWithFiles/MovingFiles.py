import shutil

def move_file(src, dest):
    shutil.move(src, dest)  

move_file("./files/text.txt", "./files/subfolder/text.txt")
move_file("./files", "./movfder")

