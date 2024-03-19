import os

def remove_file(f):
    if os.path.isFile(f):
        try:
            os.remove(f)
        except OSError as e:
            print(f'Error: {f} : {e.strerror}') 
    else:
        print(f'{f} is not a file') 

remove_file("./files/text.txt")