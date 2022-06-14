import winapps
# get each application with list_installed()
for item in winapps.list_installed():
    print(item)