from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os


image_path = "N/A" if len(sys.argv) == 1 else sys.argv[1]
mode = "-r" 

if len(sys.argv) == 3:
    mode = sys.argv[2]


if image_path == "N/A" or not os.path.isfile(image_path):
    print("file not found!")
    exit()


with Image.open(image_path) as image:
    print("file found!")


    if "c" in mode:
        print("scrubbing meta-data...")
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)

        image_without_exif.save('scrubbed_picture.jpg')

    elif "r" in mode:
        print("reading meta-data...\n")

        verbose_data={
            "format" : image.format
            ,"mode"   : image.mode
        }

        for key in verbose_data.keys():
            print(f"{key:20}: {verbose_data[key]}")


        print("\n")
        exif_data = image.getexif()
        for key in exif_data.keys():
            print(f"{TAGS.get(key):20}: {exif_data[key]}")







