# Rename page images from the pattern used in the PDF extraction
# script to the original 8-digit numbers, used in the IIIF manifest

# Tabula vocalis = volume-1-004.jpg
# Tabula vocalis = 13265220

# so: id number = pdf-page-number + 13265216
import os
import glob
import re

# volume 1: starts with 13265216
#pagenum_offset = 13265216
#volume_number = 1

# volume 2: starts with 13265950
pagenum_offset = 13265950
volume_number = 2

pattern = r"volume-2-(\d+).jpg"
mypath = "./*.jpg"
pageimages = (glob.glob(mypath))
pageimages.sort()
for pageimage in pageimages:
    #print(f"pageimage: {pageimage}")
    imagenum = int(re.search(pattern, pageimage)[1])
    #print(f"imagenum: {imagenum}")
    file_number = str(imagenum + pagenum_offset)
    print(pageimage + " -> " + file_number + ".jpg")
    #breakpoint()
    os.rename(pageimage, f"./{file_number}.jpg")
