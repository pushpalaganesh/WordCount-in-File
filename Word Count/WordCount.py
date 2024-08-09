import os
# To check whether the file is present in the system or not
isfile = os.path.isfile("C:/Users/Ganesh/Desktop/Word Count/file.txt")
print(isfile)
# To count number of words in (file.txt) file and check output result in another file (file1.txt)
count=0
file=open("C:/Users/Ganesh/Desktop/Word Count/file.txt")
for line in file:
    words = line.split(" ")
    count = count+len(words)
file2 = open("C:/Users/Ganesh/Desktop/Word Count/file1.txt","w")
file2.write("No of words present in text file is: "+str(count))
file.close()
file2.close()
    
