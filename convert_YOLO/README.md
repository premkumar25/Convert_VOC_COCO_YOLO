# Convert VOC to YOLO

In YOLO labeling format, a . txt file with the same name is created for each image file in the same directory. Each . txt file contains the annotations for the corresponding image file, that is object class, object coordinates, height and width.

### VOC

The annotation format originally created for the Visual Object Challenge (VOC) has become a common interchange format for object detection labels. 
It's well-specified and can be exported from many labeling tools including CVAT, VoTT, and RectLabel. Pascal VOC format is normally a .xml file. VOC format is as below.

```
<annotation>
	<folder>Annotations</folder>
	<filename>AMZ01866__41hHQC--VqL.jpg</filename>
	<path>C:\Users\Nehal.Gupta\Desktop\Nehal_AmazonSet2_2611\AMZ01866__41hHQC--VqL.jpg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>1000</width>
		<height>1000</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>necklace</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>141</xmin>
			<ymin>136</ymin>
			<xmax>816</xmax>
			<ymax>790</ymax>
		</bndbox>
	</object>
</annotation>
```

### YOLO

Convert the above shown VOC format to YOLO.

```
<object-class> <x> <y> <width> <height>
```
`.txt` YOLO file for above mentioned VOC.

```
4 0.47750000000000004 0.462 0.675 0.654
```

## How to use?

- Add the file paths of Annootation xml files and output files in the script
- Run the below command

```
python convert_YOLO.py
```

- Output `.txt` file will be present in the specified output folder
