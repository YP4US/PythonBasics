Greetings="Hello Mr. Root"
#print(Greetings)
#output=Greetings[0:8]
#print(output)
#output1=Greetings[:-1]
#print(output1)

#move steps
#print(data[::2])


#another way of slicing
data="Hello | Mr. | Root"

outputdata1=data[0:data.index("|")]
print(outputdata1)

index1=data.index("|")

Remainingpart1=data[index1+2:]
#print(Remainingpart1)

outputdata2=Remainingpart1[0:data.index("|")-2]
print(outputdata2)

index2=Remainingpart1.index("|")

outputdata3=Remainingpart1[index2+2:]
print(outputdata3)



