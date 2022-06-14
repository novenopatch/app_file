import os
import psutil
from fnmatch import fnmatch


drps = psutil.disk_partitions()
drives = [dp.device for dp in drps ]
print(drives)

pattern = "*.mkv"
for x in drives:
    x.replace("//","\\")
    for path, subdirs, files in os.walk(x):
        for name in files:
            if fnmatch(name, pattern):
                print(os.path.join(path, name))