# Why persistent an object come in handy?
# Saving Internal state to disk, a database, or over the network

import pickle

class Person:
    age = 45
    name = 'John Smith'
    kids = ['Tom', 'Jerry']
    employers = {'Google': 'Software Engineer', 'Facebook': 'Product Manager'}
    shoe_size = (11, 12)

def serialize(obj):
    pickled = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f'Serialized object: {pickled}')
    return pickled

def deserialize(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized object: {unpickled}')
    return unpickled

def deserialize_employers(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized employers: {unpickled.employers}')
    return unpickled

def obj_to_file(fn, obj):
    with open(fn, 'wb') as f:
        pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)

def file_to_obj(fn):
    with open(fn, 'rb') as f:
        obj = pickle.load(f)
        print(f'Object from file: {obj}')
        return obj 
    
# pickled = serialize(Person)
# deserialized = deserialize(pickled)
# deserialize_employers(pickled)

obj = obj_to_file('files_to_read/person.pkl', Person())
person = file_to_obj('files_to_read/person.pkl', obj)   
