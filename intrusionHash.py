import hashlib, os, glob


#The following is a list of resourses used.
#https://docs.python.org/3/library/os.html

#ignore list
ignore = []

#root directory to start at
rootdirectory = "/"

#class declarations
#Class to keep track of files hashed.
class fileHash:
  pass #will revise once more research

#iterate through the different directories
for x in glob.glob(rootdirectory,root_dir=rootdirectory,dir_fd=None,recursive=True):
  if os.is_file(x):
    print(x)
  elif os.is_dir(x):
    print(x)
