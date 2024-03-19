import os
from datetime import datetime

def get_date(timestamp):
    print(timestamp)
    return datetime.utcfromtimestamp(timestamp).strftime("%d %b %Y")

def get_file_attributes(fld):
    with os.scandir(fld) as dir:
        for f in dir:
            info = f.stat()
            print(f"{f.name} was last modified: {get_date(info.st_mtime)}")

get_file_attributes("./files/subfolder")