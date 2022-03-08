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
for x in glob.glob(rootdirectory,recursive=True):
  print(x)
  #if os.path.is_file(x):
    #print(x)
  #elif os.path.is_dir(x):
    #print(x)
