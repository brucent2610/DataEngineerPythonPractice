from pathlib import Path

def glob_match(fld, search):
   p = Path(fld)
   for fn in p.glob(search):
       print(fn)

# glob_match("./files", "*2*.t*")
glob_match("./files/subfolder", "*_file_*.t*")