import hyperlink

url1 = hyperlink.parse(u'https://familydoctor.org/healthy-ways-to-gain-weight-if-youre-underweight/')
url2 = hyperlink.parse(u'https://www.nhlbi.nih.gov/health/educational/lose_wt/index.htm')
url3 = hyperlink.parse(u'https://zenhabits.net/weight/')
url4 = hyperlink.parse(u'https://health.usnews.com/health-news/blogs/eat-run/2012/09/24/7-ways-to-lose-fat-fastand-fit-into-your-skinny-jeans')

def user_input():
  global w
  global h
  global b
  
  print("Welcome to the fitness calculator!\nLet us calculate your BMI by looking at your height and weight.\nYou will gain an idea about how fit you really are.\nLet's go!\n")
  w=float(input("Please enter your weight in Kilograms\n"))
  h=float(input("Please enter your height in metres\n"))
  return w,h
user_input()

def BMI():
  b=w/(h**2)
  print("Your BMI is " + str(b))
  if b<=18.5:
    print("You are underweight!\nPlease visit  \n" + str(url1) +"  \nto gain tips on how to increase weight!")
    exit
  elif b>=18.5 and b<=24.9:
    print("You are in a great shape!\nPlease visit \n" + str(url2) + " \nto remain in great shape!")
    exit
  elif b>=25 and b<=29.9:
    print("you are overweight!\nPlease visit\n" + str(url3) + " \nto regain healthy weight!")
    exit
  elif b>=30:
    print("Sad to say but you are obese. However you can regain a healthy weight by visiting\n\n" + str(url4) + "\n")
    exit
  else:
    print("Please enter the right values")
    user_input()
    return b
BMI()

def calculate_again():
  use_again = input("Do you want to use the calculator again? Type Y if yes and N if no\n\n")
  if use_again == "Y":
    user_input()
    BMI()
    calculate_again()
  elif use_again == "N":
    print("Thanks for using this calculator! Please visit again!")
    exit
  else:
    print("\nPlease enter valid response.")
    calculate_again()
calculate_again()