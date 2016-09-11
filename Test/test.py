def unique(t):

    lst=[]

    lineList=t.split("\n")

    

    for line in lineList:

        wordsInLine=line.split()

        temp=[]

        for word in wordsInLine:

            if word not in temp:

                temp.append(word)

        lst.append(len(temp))#add to your list the length of unique list

            

    return (lst)



text="it is what it is\ni mean what i say and i say what i mean"

print(unique(text))
