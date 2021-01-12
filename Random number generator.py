import random

num_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,
          57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

def add_interval():
  global a 
  global b
  a = int(input("Enter the left interval"))
  b = int(input("Enter the right interval"))
  return a,b
  valid_intervals()
add_interval()
def valid_intervals():
  if a<1 or b>100:
    print("please enter valid intervals")
    add_interval()
    valid_intervals()
  else:
    print("the random number in this range is" + str(random.choice(num_list)))
valid_intervals()
def play_again():
  ask=input("Do you want to play again?Type Y if yes and N if no")
  if str(ask)=="Y":
    add_interval()
    valid_intervals()
    play_again()
  elif str(ask)=="N": 
    print("Thanks for playing!")
  else:
    print("Enter valid response")
    exit
play_again()