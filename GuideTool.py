def IPV4checker(ipAddress):
    temp = list(map(int, ipAddress.split(".")))
    
    #if ip length (temp) is not 4 after split (invalid)
    if(len(temp) != 4):
        return False
    
    #Ip value checker (if invalid)
    for i in temp:
        if i >= 256 or i  < 0:
            return False
    
    return True

def Prefixchecker(prefixLength):
    if(prefixLength >= 0) and (prefixLength <= 32):
        return True
    else:
        return False
    

def subnetCalculator():
    print("\nSample Format: 192.168.1.0/24")
    ipString = input("Input IP Address: ")
    temp = ipString.split("/")
    ipAddress = temp[0]
    prefixLength = int(temp[1])
    results = []
    
    if IPV4checker(ipAddress) and Prefixchecker(prefixLength):
        subnetsArray = []
        currentAddress = ipAddress
        networkId = 0
        
        networks = int(input("Input network num: "))
        
        for i in range(networks):
            networkName = input("Input the name of network " + str(i + 1) + ":")
            ipNeeded = int(input("Input the number of IP Addresses needed: "))
            subnetsArray.append((networkName,ipNeeded))
        subnetsArray.sort(key = lambda x:x[1], reverse = True)
        
        for j in subnetArray:
            #Network Imformation:
            output = []
            
            #Network ID
            temp.append(int(networkID + 1))
            
            #Network Name
            temp.append(i[0])
            
            #Curent Network 
            temp.append(currentAddress)
            
            #Subnet Mask
            
            
            
        
            
        
    
    

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
