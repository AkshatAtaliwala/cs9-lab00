# Lab00, CS 9, Akshat Ataliwala

def areElementsInList(list1, list2):
    ''' 
      This function takes two lists as its parameters (list1 and
      list2). Return True if each element in list1 exists in list2.
      Return False otherwise. If list1 contains no elements, True is
      returned.
    '''

    x = set(list1) 
    y = set(list2)
# I converted the lists into sets because the .issubet method for sets allows us to compare the 
# elements much easier than if they were still lists, i remember seeing something like this 
# in either the hw or the reading.

    if len(list1) == 0:
        return True
    if x.issubset(y) == True:
        return True
    else:
        return False
    
assert areElementsInList(["one",2], [0,"one",2,"three"]) == True
assert areElementsInList([],[1,2,3,4]) == True
assert areElementsInList([1,2,3],[1,2]) == False
assert areElementsInList([1,2,3],[3,2,1]) == True


########################################################################


def alternateCase(s):
    ''' 
      This function takes a string parameter (s) and returns a new
      string that flips the case of each alpha character in s.
    '''
    return s.swapcase() # string method that swaps the case

assert alternateCase("") == ""
assert alternateCase("This is a Sentence") == "tHIS IS A sENTENCE"
assert alternateCase("CS9") == "cs9"
assert alternateCase("9.95") == "9.95"


########################################################################


def getCharacterCount(s):
    '''
        This function takes a string parameter (s) and returns a dictionary
        type where each key in the dictionary is a unique upper-case character
        in s and its associated value is the number of occurences the unique
        character exists in s. Note that the unique characters should be case
        insensitive ("a" and "A" are considered the same and should be stored as
        "A" in the dictionary). Non alpha characters (including whitespaces)
        and their occurences should also be stored in the dictionary.
    '''
    charCount = {} # initializing the dictionary

    for i in s: # forloop to iterate through the string and add each char individually
        i = i.upper() or i.lower() # to get rid of case sensitivity
        if i in charCount:
            charCount[i] += 1 # if the char is already in the function, update the value instead
        else:
            charCount[i] = 1 # if it is a new char, start from 1

    return charCount #return the new dictionary at the end


x = getCharacterCount("This is a Sentence")
assert x.get("S") == 3
assert x.get("P") == None
assert x.get("I") == 2
assert x.get(" ") == 3

y = getCharacterCount("Pi is Approximately 3.14159")
assert y.get("1") == 2
assert y.get("A") == 2
assert y.get("P") == 3
assert y.get(".") == 1
assert y.get(4) == None