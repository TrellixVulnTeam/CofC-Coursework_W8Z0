# Lab6.py# Name 1: Kendall Dunn# Name 2: Neal Sakashdef nameReverse():    """    Read a name in first-last order and display it in last-comma-first order.    """    name = input("Enter your name: ")    nameList = name.split()    nameF = nameList[0]    nameL = nameList[1]    print(nameL + ', ' + nameF)def companyName():    domain = input("Enter the URL: ")    domainSplit = domain.split(".")    company = domainSplit[1]    print(company)def initials():    numStudents = eval(input("Enter number of students: "))    for i in range(numStudents):            nameF = input("Enter the first name of student" + str(i+1) +": ")            nameL = input("Enter " + str(nameF) + "'s last name: ")#            nameList = name.split()##            nameF = nameList[0]##            nameL = nameList[1]            #isolate characters            nameFi = nameF[0]            nameLi = nameL[0]            print(str(nameF) + "'s initials are: "  + nameFi + nameLi)def names():    listNames = input("Enter list of names as comma separated list: ")    splitNames = listNames.split(",")    initials = " "    for name in splitNames:        nameSplit = name.split()        nameF = nameSplit[0]        nameL = nameSplit[1]        nameFI = nameF[0]        nameLI = nameL[0]        initials += str(nameFI) + str(nameLI) + " "    print("The initials are: ", initials)def thirds():    numSent = eval(input("Enter the number of sentences: "))    for i in range(numSent):            sent = input("Type sentence number" + str(i+1) + ": ")            print()            for j in range(2, len(sent), 3):                print(sent[j], end = "")            print()def wordCount():    numSentences = eval(input("Enter the number of sentences: "))    for i in range(numSentences):        sentence = input("Enter the sentence: ")        splitWords = sentence.split()        print("There are " + str(len(splitWords)) + "in the sentence")def wordAverage():    numSentences = eval(input("Enter the number of sentences: "))    for i in range(numSentences):        sentence = input("Enter the sentence: ")        splitWords = sentence.split()        total = 0        for j in range(len(splitWords)):            total += len(splitWords[j])        average = total/len(splitWords)        print(average)              #wordAverage()#        words = len        #        print("There are " + str(len(splitWords)) + "in the sentence")        def pigLatin():    sentence = input("Enter the sentence: ")    wordList = sentence.split()    print("Translation: ", end = " ")    for word in wordList:        firstL = word[0]        remainingWord = word[1:]        print(str(remainingWord) + str(firstL) + "ay", end = " ")                                        