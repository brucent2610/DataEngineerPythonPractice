import os

def end_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)  

def start_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)  

end_with("./files", ".txt")
print("-----")
start_with("./files", "01_test")