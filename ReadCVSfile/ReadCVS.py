import csv

with open("CSVData.csv") as csvfile:
	readcsv=csv.reader(csvfile,delimiter=",")
	dates=[]
	colors=[]
	for row in readcsv:
		#print(row)
		#print(row[0])
		date=row[0]
		color=row[3]

		dates.append(date)
		colors.append(color)
#--------------------------just playing with cvs data---------------------------
print("list of dates is:",dates)
print("list of colors is:",colors)

userInput=input("what colors date you want?\n")
colorIndex=colors.index(userInput.lower())
print("Date of",userInput,"is:",dates[colorIndex])