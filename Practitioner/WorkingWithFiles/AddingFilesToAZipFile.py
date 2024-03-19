import zipfile

to_add = ['./files/text.txt',
          './files/text2.txt']

def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as z:
        for f in files:
            lst = z.namelist()
            if f not in lst:
                z.write(f)
            else:
                print(f'File exists in zip: {f}')

add_to_zip('files.zip', to_add, 'w')