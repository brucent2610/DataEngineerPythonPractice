import xml.etree.ElementTree as ET

def parse_xml_et(fn):
    tree = ET.parse(fn)
    root = tree.getroot()
    print(root.tag)
    print(root.attrib)
    print(root.attrib['name'])
    for child in root:
        print(child.tag, child.attrib)
        for c in child:
            print(c.tag, c.attrib, c.text)  

def add_xml_element_et(fn, el, attr, val):
    tree = ET.parse(fn)
    root = tree.getroot()
    new_el = ET.SubElement(root, el)
    new_el.set(attr, val)
    tree.write(fn)

def change_xml_element_et(fn, el, attr, oldval, newval):
    tree = ET.parse(fn)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)
        if child.tag == el and child.attrib[attr] == oldval:
            child.set(attr, newval)
    tree.write(fn)

# parse_xml_et('files_to_read/ef_author.xml')  
# add_xml_element_et('files_to_read/ef_author.xml', 'domain', 'name', 'Computer Science')    
change_xml_element_et('files_to_read/ef_author.xml', 'domain', 'name', 'Computer Science', 'Information Technology')