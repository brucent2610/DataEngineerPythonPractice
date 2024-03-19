import zipfile

to_zip = ['./files/text.txt',
          './files/text2.txt',
          './files/text3.txt'
          './files/text4.txt']

def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as z:
        for f in files:
            z.write(f)  

create_zip('files.zip', to_zip, 'w')