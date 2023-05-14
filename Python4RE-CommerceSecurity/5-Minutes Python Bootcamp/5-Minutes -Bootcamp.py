# Author   : Amrit Chhetri, Cyber Security Researcher
# Purpose  : 5 Minutes Boot Camp
# Scope    : Comments to Function, Modules to Exception Handling

#1. print() : prints message to Terminal, print number , variable and object
print("E-Commerce Security",45)

#2. Variable is declared without data type, it defined automatically to data assigned
text="This is Python for Digital Forensic"     # String
number= 23                                     # Number
floaingPoint=23.45
print(floaingPoint)

#3. # defines single line comments and ''' defines multiline comments
''' I am covering python basic, then Digital Forensic 
and finally Python on Digital Forensics'''
# Single LIne


#4. [] defines list and stores multiple and allows changes using append() function, index at 0
listA= ["Python","C++", "Kotlin"]
listA.append("Ruby")
print(listA[0])

#3. (), Parentheses is used to define tuple and does now allow changes, immutable
tupleA= ("Monday",)
daysInWeek=("Monday", "Tuesday", "Wednesday")
print(daysInWeek[0:2])

#4. (x,1) declares one number tuple
oneTuple=(34,)
print(oneTuple)

#5. {} is used declare key-value pair dictionary
ditionary={3:"Play Station", 4:"Play Station VR"}
print(ditionary[4])

#6. open() create file object and argument mode a, r, w
fileObj=open("File.txt","w")
fileObj.write("Writing to text file")

#7. readline() reads line
fileObj=open("File.txt","r")
for line in fileObj:
    print(line)

#8. {} is used to define SET too, omits duplicate values

setValue={2,3,5,6,7,3,5,6}
print(setValue)

#9. if-elseif-else is used to define If-Else Control Statement

counterX= (2==3)
counterY=False
if counterY:
    print("She Forensic Hypnotist")
elif counterY:
    print("He is Neuropsycholist")
else:
    print("He is Cyber Psychologist")

#10. try-except is used for exception handling
try:
    fileObj=open("File2.txt","w")
    fileObj.write("Writing to text file")
except:
    print("Entered Error Block")
finally:
    fileObj.close()

#11. def key is used to define function, function may or may return values
def funcWithNoReturn(arg1, arg2):
    compute= arg1**2+arg2**2
    print(compute)
funcWithNoReturn(2,2)

#12. logging module is for logging, support 5 levels of logging starting DEBUG to CRTICAL
import logging as log

logger=log.getLogger("AppLogger")
logHandler=log.FileHandler("AppLog.log")
logger.addHandler(logHandler)
#Writing messages
logger.warning("This is Warning Message")
logger.error("This is error message")

#13. Logging is used with Exception handling
try:
    ileObj=open("File.txt1","r")
    for line in fileObj:
        print(line)
except:
    logger.error("Entered Error Block")
    print("Entered Error Block")
finally:
    fileObj.close()

#14. Pilllow Module perfroms Metadata analysis
from PIL import Image
#img= Image.open("Image.jpg")







