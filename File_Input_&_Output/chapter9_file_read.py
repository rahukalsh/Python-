my = open("file.txt", "r")
text = my.read()
print(text)
my.close() 

######################################

myfile = open("text.txt", "r")

textlist = myfile.readline()         # read only first line 
print(textlist)

textlist = myfile.readline()         # read only the next line means second line 
print(textlist)
myfile.close() 

##################################

fileme = open("myfile.txt", "r")
texts = fileme.readlines()         # read all the line ( Entire Containt )  But Shows as a List 
print(texts)

fileme.close() 
