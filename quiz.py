print("Enter your name")
user= str(input())
points= 0
print("hello,", user, ".")
print("I am going to ask you a set of 3 GK questions to check your score. Ready?")
print("\n 3...")
print("\n 2...")
print("\n 1...")
print("1) Who is the current prime minister of India?")
a= "a) Narendra Modi"
b= "b) I dont know"
c= "c) Donald Trump"
d= "d) yes."
print(a)
print(b)
print(c)
print(d)
ans1= str(input())
if ans1=="a" or ans1=="A":
    print("+1 point")
    points= points+1
else:
    print("...")
print("2) Which state is known as 'God's own country'?")
a= "a) Delhi"
b= "b) I dont know"
c= "c) Kerala"
d= "d) yes."
print(a)
print(b)
print(c)
print(d)
ans2=str(input())
if ans2=="c" or ans2=="C":
    print("+1 point")
    points=points+1
else:
    print("...")
print("3) Who is also called 'Missile man of india?'")
a= "a) Satoru Gojo"
b= "b) yes."
c= "c) pillowcase"
d= "d) APJ Abdul Kalam"
print(a)
print(b)
print(c)
print(d)
ans3= str(input())
if ans3=="d" or ans3=="D":
    print("+1 point")
    points=points+1
else:
    print("...")
print("\n Your score is ", points)
