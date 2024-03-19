import zipfile

def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as z:
        z.extract(fn, path=path)

def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as z:
        z.extractall(path=path)

extract_file('files.zip', 'files/test.txt', 'extracted')
extract_all('files.zip', 'extracted')

