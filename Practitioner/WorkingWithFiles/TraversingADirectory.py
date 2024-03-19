import os

def traverse(fld):
    for fldpath, fldnames, flnames in os.walk(fld):
        print(f'Folder: {fldpath}')
        for fn in flnames:
            print("\t" + fn)

traverse("./files")