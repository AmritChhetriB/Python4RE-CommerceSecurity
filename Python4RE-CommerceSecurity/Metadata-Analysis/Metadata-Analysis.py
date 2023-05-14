# Author: Amrit Chhetri, Digital Forensic Researcher
# Purpose: Image Metadata Analysis
# Module: Pillow, https://pypi.org/project/Pillow/
# Installations: pip3 install Pillow or using Interpreter option in PyCharm

from PIL import Image, ImageEnhance
img_org = Image.open("Image.jpg")
#img.show()
print("Exif Data:", img_org._getexif())
print("Size:", img_org.size)
print("Format:", img_org.format)
print("Mode:", img_org.mode)

'''
#Image Enhancement
enhace_mgae = ImageEnhance.Color(img_org)
enhace_mgae.enhance(10.0).show()
'''


