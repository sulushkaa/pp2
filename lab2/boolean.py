#ex1
print (10 > 9)
print (10 == 9)
print (10<9)

#ex2
a = 200
b = 33
if b > a :
 print("b is greater than a")
else :
 print("b is not greater than a")
  
#ex3
 print(bool("Hello"))
 print(bool(15))
 
#ex4
 x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#ex5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#ex6
bool(False)
bool(0)
bool(None)
bool("")
bool(())
bool([])
bool({})

#ex7
class myclass():
 def __len__(self):
  return 0

myobj = myclass()
print(bool(myobj))

#ex8
def myfunction():
 return True
print (myfunction())

#ex9
def myFunction():
 return True
if myFunction():
 print("YES!")
else: 
 print("NO!")

 #ex10
 x = 200
 print(isinstance(x, int))
 
 