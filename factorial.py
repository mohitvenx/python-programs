#TO FIND FACTORIAL OF A NUMBER 
def fact(n):
 if( n==0):
  return 1 
 else:
  return(n*fact(n-1))
five=fact(5)
print(five)
