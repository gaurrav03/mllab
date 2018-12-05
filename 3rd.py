import csv
# specialize function same as find s 
def specialize(s,row,g):
	for i in range(attr):
		if s[i]!= row[i]:
			s[i] ='?'
# additional functionality to remove the genralized terms that do not support the new hypothesis
	for generalizations in g:
		for i in range(attr):
			if generalizations[i] != row[i] and generalizations[i]!='?' :
				g.remove(generalizations)
def generalize(s,row,g):
	# for the first time , generalize contains all ? and needs to be removed 
	if len(g)==1:
		g.pop()
	for i in range(attr):
		if row[i] == s[i] or s[i]=='?':
			continue
		else:
			list = []
			for j in range(i):
				list.append('?')
			list.append(s[i])
			for j in range(i+1, attr):
				list.append('?')
			g.append(list)		
data =[]			
with open('trainingexamples.csv')  as csvFile:
	csvfile = csv.reader(csvFile, delimiter =',')
	print("the set of training examples are:\n")
	for row in csvfile:
		print(row)
		data.append(row)
	attr = len(row)-1
	g =[['?']*attr] # at any point, specialize has one term but generalize may have more than 1 term, so g is a list of lists
	s = ['$']*attr
	print(" G0 = ",g)
	print(" S0 = ",s)
	print("\n\n**********************************\n\n")
	j=0;
	#initializing the first specialize 
	for i in range(attr):
		s[i]=data[0][i]
	for row in data:
		j+=1
		print(row)
		if row[attr].upper() =="Y":
			specialize(s,row,g)
		else:
			generalize(s,row,g)
		print("G{0} =".format(j), g)
		print("s{0} =".format(j),s)
		print("\n\n**********************************\n\n")	
