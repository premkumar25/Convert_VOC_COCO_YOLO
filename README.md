## Convert_VOC_COCO_YOLO

One of the important step in Object detection is to convert the Annotation file to corresponding format based on the Object detection model used.

### Different types of Annotation formats

- Pascal VOC
- COCO
- YOLO

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
			"file_name": "918121_1557903451205255_561212074_n.jpg",
			"height": 640,
			"width": 640,
			"id": "918121_1557903451205255_561212074_n"
		}
	],
	"type": "instances",
	"annotations": [
		{
			"area": 154192,
			"iscrowd": 0,
			"image_id": "918121_1557903451205255_561212074_n",
			"bbox": [
				66,
				202,
				419,
				368
			],
			"category_id": 4,
			"id": 1,
			"ignore": 0,
			"segmentation": []
		},
		{
			"area": 79530,
			"iscrowd": 0,
			"image_id": "918121_1557903451205255_561212074_n",
			"bbox": [
				273,
				47,
				330,
				241
			],
			"category_id": 4,
			"id": 2,
			"ignore": 0,
			"segmentation": []
		},
		{
			"area": 78430,
			"iscrowd": 0,
			"image_id": "918121_1557903451205255_561212074_n",
			"bbox": [
				0,
				92,
				310,
				253
			],
			"category_id": 4,
			"id": 3,
			"ignore": 0,
			"segmentation": []
		}
	],
	"categories": [
		{
			"supercategory": "none",
			"id": 0,
			"name": "bracelet"
		},
		{
			"supercategory": "none",
			"id": 1,
			"name": "earring"
		},
		{
			"supercategory": "none",
			"id": 2,
			"name": "necklace"
		},
		{
			"supercategory": "none",
			"id": 3,
			"name": "ring"
		},
		{
			"supercategory": "none",
			"id": 4,
			"name": "watch"
		}
	]
}
```

### YOLO

In YOLO labeling format, a . txt file with the same name is created for each image file in the same directory. Each . txt file contains the annotations for the corresponding image file, that is object class, object coordinates, height and width.

```
<object-class> <x> <y> <width> <height>
```

Example:

```
car 45 55 29 67
bus 99 83 28 44
```

## How to use?

- If you want to convert **Pascal VOC** format to **.txt** then check the `README.md` file in [convert_VOC](convert_VOC)
- If you want to convert **Pascal VOC** format to **YOLO** then check the `README.md` file in [convert_YOLO](convert_YOLO)
- If you want to convert **Pascal VOC** format to **COCO** then check the `README.md` file in [convert_VOC2COCO](convert_VOC2COCO)
- If you want to convert **COCO** format to **.txt** then check the `README.md` file in [convert_COCO](convert_COCO) 
