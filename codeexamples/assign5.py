# CST 100 Assignment 5 - Lists and Dictionaries 
# by Mike Davidovich
# Last modified 4/22/2016

# part 1

def find_longest_word(wordlist):     #funtion to define longest work
    words = wordlist.split()        # takes list string and split to list
    longest_word = ""               #initializes longest word tracking
    for item in words:              #for statement updates longest word
        if len(item) > len(longest_word):
            longest_word = item
        else:
            longest_word = longest_word
    return(longest_word)            #function returns logest word
            
wordlist = input("Enter a few words and I will find the longest: ")   #inputs for word list

#print statements for outputs

print('\n'+"The list of words entereed is:"+'\n')

print(wordlist.split())

print('\n'+"The longest word in the list is:"+'\n')

print(find_longest_word(wordlist)+'\n')

# part 2

numList = [int(input("Enter a number (-9999 to end):"))]  #initializes number list; couldn't start at [] as i got errors

while numList[-1] != int(-9999):       #allows user to update numlist until it terminates with -9999
    newnum = int(input('\n'+"Enter a number (-9999 to end):"))
    numList.append(newnum)

numList = numList[:-1]     #excludes -9999 from num list as it's the break command

def allNumAvg(numList):          #function to find average of all numbers
    total = 0
    for number in numList:      #this for loop finds total to calculate average
        total = total + number
    AvgAllNum = total/len(numList)
    return AvgAllNum
   
def posNumAvg(numList):         #function to find average of all pos numbers
    posNumList = []
    for number in numList:
        if number > 0:
            posNumList.append(number)       #creates new list with only pos numbers
    total = 0
    for number in posNumList:
        total = total + number
    AvgPostive = total/len(posNumList)
    return AvgPostive

def nonPosAvg(numList): #function to find average of all neg numbers
    nonPosList = []
    for number in numList:
        if number < 1:
            nonPosList.append(number)       #creates new list with only neg numbers
    total = 0
    for number in nonPosList:
        total = total + number
    AvgNonPos = total/len(nonPosList)
    return AvgNonPos

readout = {}        #creates blank dictionary

readout['AvgAllNum'] = allNumAvg(numList)   #assigns keys and values to dictionary

readout['AvgPositive'] = posNumAvg(numList)

readout['AvgNonPos'] = nonPosAvg(numList)

#print commants for output

print('\n'+"The list of all numbers is:",'\n')
print(numList,'\n')
print("The dictionary with averages is:",'\n')
print(readout)

#end program
