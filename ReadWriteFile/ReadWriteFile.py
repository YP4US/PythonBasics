#write into file
text="Hello Yogesh"
saveFile=open("yp.txt",'w')
saveFile.write(text)
saveFile.close()
print("write completed")

#append into same file
text2="\t text appended.."
append=open("yp.txt",'a')
append.write(text2)
append.close()
print("text appended..")

#read file
print(open("yp.txt",'r').read())
