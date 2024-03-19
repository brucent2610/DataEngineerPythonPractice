import json

def read_print_json(fn, pretty, sort):
    with open(fn, 'r') as f:
        data = json.load(f)
        print(json.dumps(data, sort_keys=sort, indent=4
        if pretty else data))

def update_authot_json(fn, arr_name, pos, key, value):
    with open(fn, 'r') as f:
        data = json.load(f)
        data[arr_name][pos][key] = value
        with open(fn, 'w;') as f:
            json.dump(data, f)

# read_print_json('files_to_read/authors.json', False, True)
update_authot_json('files_to_read/authors.json', 'authors', 0, 'name', 'John Doe') 