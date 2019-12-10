#File operations
f = open("Modules.py")    # open file in current directory
print(f.readlines());
f.close()

#after with block is over it will call the f.close() almost same as using in c#
with open("pythonOutPut.txt", 'w', encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

with open("pythonOutPut.txt") as fout:
    print(fout.readlines())

#directory handling
import os
#os.getcwd()  # present working directory
#os.chdir('D:\\Hello') # Changing current directory to D:\Hello
#os.listdir()  # list all sub directories and files in that path
#os.mkdir('test') # making a new directory test
#os.rename('test','tasty') # renaming the directory test to tasty
#os.remove('old.txt')  # deleting old.txt file
print(os.getcwd())
print(os.listdir())
