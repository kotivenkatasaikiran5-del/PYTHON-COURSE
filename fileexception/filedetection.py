import os
print("----------------------")
print("FILE SECURITY SCANNER")
print("----------------------")
file=input("Enter the file to verify ")
absolute_path=os.path.abspath(file)
print(absolute_path)
interest=[".py"]
if os.path.isfile(file):
    print("It is a file")
elif os.path.isdir(file):
    print("It is a directory")

    items=os.listdir(file)
    for item in items:
     path=os.path.join(file,item)
     if os.path.isdir(path):
        print(item,"-","directory")
     elif os.path.isfile(path):
            

        size=os.path.getsize(path)
        print(item,"-",size,"Bytes")
        extension=os.path.split(item)[0]
        if extension in interest:
           print("cofidentail file",item)
     else:
           print("It is not a interset")
else:
   print("It is not a directory")