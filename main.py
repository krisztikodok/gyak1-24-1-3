import random

#classes

class myComplexNr:
  def __init__(self,real=0,imag=0):
    print("Complex number is being created...")
    self.real=real
    self.imag=imag

  def showComplex(self):
    print("{0} + {1}j".format(self.real,self.imag))

newComp1=myComplexNr(10,0)
newComp1.showComplex()

newComp2=myComplexNr(10,10)
print(newComp2.real,newComp2.imag)
newComp2.showComplex()

del newComp2.real

#arrays

arr=[]
for i in range(10):
  arr.append(random.randrange(10,15))
print(arr)

brands=["Datsun","Ford","Honda","Fiat","Chevrolet"]
brands.remove("Datsun")
brands.append("<placeholder>")
print(brands)

brands.pop()
print(brands)
print(set(brands)) #print in alphabetical order

num=["3"]
repeat_num=num*5
print(repeat_num)

for i in range(1,11):
  if i==5:
    print("***")
    continue
  if i==9:
    break
  print(i)