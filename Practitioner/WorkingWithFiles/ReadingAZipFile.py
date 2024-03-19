import zipfile

def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as z:
        lst = z.namelist()
        for l in lst:
            zfinf = z.getinfo(l)
            print(f'{l} => {zfinf.file_size} bytes, {zfinf.compress_size}')

read_zip('files.zip')