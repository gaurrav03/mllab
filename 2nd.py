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







import csv
with open('trainingexamples.csv')  as csvFile:
    data = [tuple(line) for line in csv.reader(csvFile)]
def Domain(): #All possible unique values an attribute/field can hold.
    D =[]
    for i in range(len(data[0])):
        D.append(list(set([ele[i] for ele in data])))
    return D
D = Domain()
def consistant(h1, h2):
    for x, y in zip(h1, h2):
        if not (x == "?" or (x != "?" and (x == y or y == "?"))):
            return False
    return True
def candidate_elimination():
    G = {('?',)*(len(data[0]) - 1),}
    S = ['?']*(len(data[0]) - 1)
    no = 0
    print("\n G[{0}]:".format(no), G)
    print("\n S[{0}]:".format(no), S)
    for item in data:
        no += 1
        inp , res = item[:-1] , item[-1]
        if res in "Yy": 
            i = 0 #Remove from G any inconsistancy
            G = {g for g in G if consistant(g,inp)}
            for s,x in zip(S,inp):   # similar to find-s
                if not s==x:
                    S[i] = '?' if s != '?' else x
                i += 1
        else:
            S = S #unaffected for this eg.
            Gprev = G.copy()
            for g in Gprev: #for each hypothesis
                if g not in G: # if g gets removed.
                    continue
                for i in range(len(g)):  #for every fiels/atribute
                    if g[i] == "?":  #if it can be more generalized.
                        for val in D[i]: # for each possible values in domain.
                            if inp[i] != val and val == S[i]: # check if this possible value in domain is applicable.
                                g_new = g[:i] + (val,) + g[i+1:]
                                G.add(g_new)
                    else:
                        G.add(g)  # difference_update() used to remove the items from the set which is passed to it.            
                G.difference_update([h for h in G if
                                 any([consistant(h, g1) for g1 in G if h != g1])])
        print("\n G[{0}]:".format(no), G)
        print("\n S[{0}]:".format(no), S)
candidate_elimination()
