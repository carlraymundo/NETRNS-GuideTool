def subnetCalculator():
    print("subnet")

def checkAddressClass():
    print("Checking")
    
def checkAddressType():
    print("Check 2")

def exit():
    print("Good Luck Network Admin!")

def main():
  print("Hello there Network Admin!\n")
  print("In order to help you, please select any of the following options:")
  print("[1] Subnet Calculator")
  print("[2] Check Address Class")
  print("[3] Check Address Type")
  print("[4] Exit\n")

  menu = input("Input: ")
  if int(menu) == 1:
      subnetCalculator()
  elif int(menu) == 2:
      checkAddressClass()
  elif int(menu) == 3:
      checkAddressType()
  else:
      exit()

main()
