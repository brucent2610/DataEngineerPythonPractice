def read_txt(fn):
    with open(fn, 'r') as f:
        print(f.read())

def read_txt_by_line(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()
        for l in lines:
            print(l, end='')
            line = f.readline()

def write_new_txt(fn, txt):
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(txt)

def append_to_txt(fn, txt): 
    with open(fn, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(txt)

# read_txt('files_to_read/example.txt')
# read_txt_by_line('files_to_read/example.txt') 