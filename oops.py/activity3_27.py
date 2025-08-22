#write a program to create a class that will find the numberin the tuple that add up to a sum and return the position of an element
#the value of sum can be taken as an input
#tuple = (10,20,30,40,50,60,70)

class pair_elements():
    def twoSum(self, nums, target):
        lookUp= {}
        for i, num in enumerate(nums):
            if target-num in lookUp:
                return (lookUp[target-num], i)
            lookUp[num]= i
value= int(input("Enter sum for which you want to make this search:  "))
print("index1= %d, index2= %d" % pair_elements().twoSum((10,20,30,40,50,60,70),value))