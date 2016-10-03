##Palindrome Detector

def detector(input):
    string = (str(input)).lower()
    string = string.replace(" ", "")
    string = "".join(e for e in string if e.isalnum())
    reversedString = "".join(reversed(string))
    if string == reversedString:
        return True, reversedString, string
    else:
        return False, reversedString, string

    
    
results, revString, string = detector(raw_input("Test if your statement is a palidrome.\n"))
if results:
    print "This is a palindrome; " + "%s is the reverse of %s." % (revString, string) 
else:
    print "This is not a palindrome; " + "%s is not the reverse of %s." % (revString, string)