#this is a break
#write a program to search for alphabet "A" in the given string.
#and terminate the loop after finding the alphabet "A"
ui= input("Enter a word:  ")
for i in ui:
    if (i=="A") or (i=="a"):
        print("A is present in your statement")
        break
    else:
        print("A not found.")