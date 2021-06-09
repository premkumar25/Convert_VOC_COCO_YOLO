import os
import xml.etree.ElementTree as ET
from pathlib import Path
import xmltodict

# Specify classes present in the xmls
## Note: If you want to directly get classes without specifiying them,
## Comment the below line and directly give the class name in txt file
classes = ['braclet', 'ring', 'earring', 'watch', 'necklace']


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x, y, w, h)


def convert_annotation(file, output_path):

    filename = file.split('\\')[-1]
    txt_data = []
    with open(file, 'rb') as in_file:
        xml_data = xmltodict.parse(in_file, xml_attribs=False)

    size = xml_data['annotation']['size']
    w = int(size['width'])
    h = int(size['height'])

    if isinstance(xml_data["annotation"]["object"], list):
        for obj in xml_data["annotation"]["object"]:
            difficult = obj['difficult']
            cls = obj['name']
            if cls not in classes or int(difficult) == 1:
                continue

            ## If you want the class name in txt file change the below statement
            cls_id = classes.index(cls)             # cls_id = cls
            xmlbox = obj['bndbox']
            b = (float(xmlbox['xmin']), float(xmlbox['xmax']), float(xmlbox['ymin']),
                 float(xmlbox['ymax']))
            bb = convert((w, h), b)
            txt_data.append(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    else:
        obj = xml_data["annotation"]["object"]
        difficult = obj['difficult']
        cls = obj['name']
        if cls not in classes or int(difficult) == 1:
            print('Class not found %s' % cls)

        ## If you want the class name in txt file change the below statement
        cls_id = classes.index(cls)             # cls_id = cls
        xmlbox = obj['bndbox']
        b = (float(xmlbox['xmin']), float(xmlbox['xmax']), float(xmlbox['ymin']),
             float(xmlbox['ymax']))
        bb = convert((w, h), b)
        txt_data.append(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    with open(os.path.join(output_path, filename.rstrip('.xml') + '_yolo.txt'), 'w') as out_file:
        out_file.write("".join(txt_data))


# File location of xmls and output files
full_dir_path = Path(r'D:\Vf\convert_YOLO\sample\Annotations')
output_path = Path(r'D:\Vf\convert_YOLO\sample\yolo')

# List the files in the directory
list_dir = os.listdir(full_dir_path)

if not os.path.exists(output_path):
    os.makedirs(output_path)

for file in list_dir:
    convert_annotation(os.path.join(full_dir_path, file), output_path)

print("Finished processing")
