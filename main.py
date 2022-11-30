from fractions import Fraction
while True:
  a_g=input("Arthmitic or geometric(respond with a or g)?")
  if a_g=="g":
    a = int(input("Enter  the intial term: "))
    b = float(input("Enter common ratio: "))
    c = int(input("Enter the term to print till: "))
    
    print("The sequence is\n")
    print("{",a)
      
    for i in range(c):
      print(a*Fraction.from_float(b),",")
      a = a*Fraction.from_float(b)
    print("}")
  
  if a_g=="a":
    a = int(input("Enter  the intial term: "))
    b = float(input("Enter common differnce: "))
    c = int(input("Enter the term to print till: "))
    
    print("The sequence is\n")
    print("{",a)
      
    for i in range(c):
      print(a+Fraction.from_float(b),",")
      a = a+Fraction.from_float(b)
    print("}")
  
    
  
  
    
