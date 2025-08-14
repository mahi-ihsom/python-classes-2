#write a program to calculate the number of strings where the string length is 2 or more snd the first and last characters are the same, from a given list of strings
def match_words(words):
    count= 0
    list1= []
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            count= count + 1
            list1.append(i)
    print("List of words with first and last character same: \n", list1)
    print("count= ", count)
res= match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print(res)