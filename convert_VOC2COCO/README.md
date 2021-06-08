# Convert VOC to COCO

### Pascal VOC

The annotation format originally created for the Visual Object Challenge (VOC) has become a common interchange format for object detection labels. It's well-specified and can be exported from many labeling tools including CVAT, VoTT, and RectLabel.
Pascal VOC format is normally a `.xml` file. VOC format is as below.

```
<annotation>
    <folder>images</folder>
    <filename>maksssksksss0.png</filename>
    <size>
        <width>512</width>
        <height>366</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>without_mask</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <occluded>0</occluded>
        <difficult>0</difficult>
        <bndbox>
            <xmin>79</xmin>
            <ymin>105</ymin>
            <xmax>109</xmax>
            <ymax>142</ymax>
        </bndbox>
    </object>
    <object>
        <name>with_mask</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <occluded>0</occluded>
        <difficult>0</difficult>
        <bndbox>
            <xmin>185</xmin>
            <ymin>100</ymin>
            <xmax>226</xmax>
            <ymax>144</ymax>
        </bndbox>
    </object>
</annotation>
```

### COCO

The COCO bounding box format is [top left x position, top left y position, width, height]. The category id corresponds to a single category specified in the categories section. Each annotation also has an id (unique to all other annotations in the dataset).
COCO format is usually a `.json` file.

```
{
	"images": [
		{
			"file_name": "maksssksksss0.png",
			"height": 512,
			"width": 366,
			"id": "maksssksksss0"
		}
	],
	"type": "instances",
	"annotations": [
		{
			"area": 154192,
			"iscrowd": 0,
			"image_id": "maksssksksss0",
			"bbox": [
				79,
				105,
				109,
				142
			],
			"category_id": 0,
			"id": 1,
			"ignore": 0,
			"segmentation": []
		},
		{
			"area": 79530,
			"iscrowd": 0,
			"image_id": "maksssksksss0",
			"bbox": [
				185,
				100,
				226,
				144
			],
			"category_id": 1,
			"id": 2,
			"ignore": 0,
			"segmentation": []
		}
	],
	"categories": [
		{
			"supercategory": "none",
			"id": 0,
			"name": "without_mask"
		},
		{
			"supercategory": "none",
			"id": 1,
			"name": "with_mask"
		}
	]
}
```

## How to run?

- pip install lxml
- Run the following command

`python convert_VOC2COCO.py xml_list.txt ../Annotations ../output.json`

- **xml_list.txt** is the `.txt` file which contains all the `.xml` file names in it.

```
maksssksksss0.xml
maksssksksss1.xml
maksssksksss2.xml
```

- **../Annotations** is the path where the `.xml` files are present.
- **../output.json** is the name of the output `.json` file in `COCO` format with complete path.

