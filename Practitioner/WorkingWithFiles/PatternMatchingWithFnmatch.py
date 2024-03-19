import os, fnmatch

def match(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)  


# match("./files", "*.csv")
match("./files", "*2*_file.csv")