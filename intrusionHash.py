import hashlib, os, glob


#The following is a list of resourses used.
#https://docs.python.org/3/library/os.html

#ignore list
ignore = []

#files/directories with name as key and hash as value to detect file movements
filedict={}
dirdict={}

#root directory to start at
rootdirectory = "/**"

#iterate through the different directories
for x in glob.iglob(rootdirectory,recursive=True):
  if os.path.isfile(x):
    print("file: "+os.path.basename(x))
  elif os.path.isdir(x):
    print("Directory: "+os.path.dirname(x))
