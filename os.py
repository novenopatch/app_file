from lib2to3.pgen2 import driver
import os
import psutil

#


def makeDirectory():
    print(f"Actualy Directory is : {os.getcwd()}")
    newPath = str(input("Enter Path : "))
    os.chdir(newPath)
    print(f"New Directory is : {os.getcwd()}")
    newDirName = str(input("Enter Directory name : "))
    os.makedirs(newDirName)
    
def listDirectory():
    os.listdir()
    
#var=os.system("wmic logicaldisk get name")
#print(var)
#print(os.system("wmic logicaldisk get name"))
#print(os.system( str(input("Enter Command : "))))
#print(f"Actualy Directory is : {os.getcwd()}")
#makeDirectory()
#print(listDirectory())
#print(listDirectory("D:\\"))


drps = psutil.disk_partitions()
drives = [dp.device for dp in drps ]
print(drives)