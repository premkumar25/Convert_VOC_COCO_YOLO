import os
import xml.etree.ElementTree as ET
from pathlib import Path
import json
from tqdm import tqdm
import xmltodict


# File paths of xml location, txt save location

xml = Path(r"D:\praser\ann")
xmls = os.listdir(xml)
xmls = [f for f in xmls if f.split(".")[-1] == "xml"]

txt_path = Path(r"D:\praser\txt")


# code to convert xml to txt (for GroundTruth files only, add confidence score for  detections)

for xl in xmls:
    # xl = "abc.xml"
    file_id = xl
    txt_data = []
    with open(os.path.join(xml, file_id), "rb") as f:
        xml_data = xmltodict.parse(f, xml_attribs=False)

    try:
        if isinstance(xml_data["annotation"]["object"], list):
            for box in xml_data["annotation"]["object"]:
                cls_name = box['name']
                coord = box["bndbox"]
                txt_data.append(cls_name + " " + coord["xmin"] + " " + coord["ymin"] + " " + coord["xmax"] + " " + coord["ymax"])
        else:
            box = xml_data["annotation"]["object"]
            cls_name = box['name']
            coord = box["bndbox"]
            txt_data.append(cls_name + " " + coord["xmin"] + " " + coord["ymin"] + " " + coord["xmax"] + " " + coord["ymax"])
        
        with open(os.path.join(txt_path, file_id.rstrip('.xml') + '.txt'), "w") as file:
            file.write("\n".join(txt_data))

    except KeyError:
        print('Object details missing in file: %s' % file_id)
