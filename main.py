import time, sys, math


def typewrite(output):                     # typewrite() - takes in an input and prints it slowly across the screen (like a typewriter?)
  for letters in str(output):
    sys.stdout.write(letters)
    time.sleep(0.038)
    sys.stdout.flush()


def intInput(x):                           # intInput() - takes a string and sanitises the input, repeating the input until a integer is recieved
  try:
    typewrite(str(x))
    realInput=int(input())
    return realInput
  except ValueError:
     return intInput(x)


def inputCheck(test, check):               # inputCheck() - takes an inputted string and compares it to a predetermined string, returning true if similair
  score=0
  for i in range (len(test)):
    try:
      if check[i]==test[i]: score+=1
    except IndexError:
      pass
  fractionScore=float(score/len(test))
  if fractionScore>=0.5 and check[0]==test[0]:
    return True
  elif fractionScore>=8:
    return True
  else:
    return False


def switch(arguement):                     # switch() - a blank switch function using a dictionary to work
  switch={
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6"
  }
  return switch.get(arguement, "default")


def primeList(total):                      # primeList() - returns a list of primes the length of the integer inputted
  if total>1: lis=[2, 3]
  elif total==1: lis=[2]
  else: lis=[]
  primeAmount=2
  primeCheck=1
  while primeAmount < total:
    falsePrime=0
    primeCheck+=1
    multiple=1
    if primeCheck%2==0:  continue
    while falsePrime==0:
      multiple+=2
      if primeCheck%multiple==0:
        falsePrime=1
      elif multiple>(math.sqrt(primeCheck)):
        lis.append(primeCheck)
        primeAmount+=1
        falsePrime=1
  return(lis)


# number=0
# number += 1 while number >= 20