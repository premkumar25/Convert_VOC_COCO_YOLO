# VOC_to_TXT

Python script to convert PASCAL VOC annotation xml's to .txt files

### Eg:

#### VOC format

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

Above is the annotation file which is  `.xml` (This is known as Pascal VOC format)

#### .txt file

```
without_mask 79 105 109 142
with_mask 185 100 226 144
```

## To use this script

- Change the Annotation file path
- Specify the path to save the txt file
- Run the below command

```
python voc2txt.py
```

Note: This script is for `Groundtruth` files only. For `Detection` add the confidence score in the script.
