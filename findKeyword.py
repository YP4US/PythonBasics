Greetings="Hi|Mr.|Root|"
pipe1=Greetings.find("|",0)

part1=Greetings[0:pipe1]
print(part1)
pipe2=Greetings.find("|",pipe1+1)

part2=Greetings[pipe1+1:pipe2]
print(part2)

pipe3=Greetings.find("|",pipe2+1)
part3=Greetings[pipe2+1:pipe3]
print(part3)