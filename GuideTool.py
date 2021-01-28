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
    if(prefixLength > 0) and (prefixLength <= 32):
        return True
    else:
        return False
    
#to get the minimum number of hosts possible
def getHostsNum(value):
    
    exp = 0
    
    while int(value) > ((2 ** exp) - 2):
        exp+=1
    
    return exp
    
def subnetMaskToBin(subnetMask):
    temp = ""
    temp = "1" * subnetMask
    return temp.ljust(32,"0")

def binaryToIp(binary):
    temp = [binary[x:x+8] for x in range(0, len(binary), 8)]
    temp = list(map(lambda temp: int(temp, 2), temp))
    ipAddress = ""
    for x in temp:
        ipAddress = ipAddress + str(x) + "."
    return ipAddress[:-1]
    
def octetToBinary(value):
    octet = ""
    octetValue = bin(int(value)).replace("0b", "").rjust(8, "0")
    octet = str(octetValue)
    return octet

def ipToBinary(ip):
    ipTemp = ""
    ipList = ip.split(".")
    for i in ipList:
        ipTemp = ipTemp + octetToBinary(i)
    
    return ipTemp
    
def networkAddress(ipAddress,prefixLength):
    bits = subnetMaskToBin(prefixLength).count("0")
    ip = ipToBinary(ipAddress)
    ip = ip[:-bits]
    ip = ip.ljust(32,"0")
    
    return binaryToIp(ip)

def broadcastAddress(ipAddress, prefixLength):
    bits = subnetMaskToBin(prefixLength).count("0")
    ip = ipToBinary(ipAddress)
    ip = ip[:-bits]
    ip = ip.ljust(32,"1")

    return binaryToIp(ip)

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
        
        for j in subnetsArray:
            #Network Imformation:
            output = []
            
            #Network ID
            output.append(int(networkId + 1))
            
            #Network Name
            output.append(j[0])
            
            #Curent Network 
            output.append(currentAddress)
            
            #Subnet Mask
            hosts = int(getHostsNum(j[1]))
            currentSubnetMask = 32 - hosts
            print(binaryToIp(subnetMaskToBin(currentSubnetMask)))
            output.append(binaryToIp(subnetMaskToBin(currentSubnetMask)))
            
            #Prefix Length
            output.append("/" + str(currentSubnetMask))
        
            
            #first usable address
            temp = networkAddress(currentAddress,currentSubnetMask)
            temp = bin(int(ipToBinary(temp),2) + int("1",2)).replace("0b", "").rjust(32, "0")
            temp = binaryToIp(temp)
            output.append(temp)

            #last usable
            temp = broadcastAddress(currentAddress,currentSubnetMask)
            temp = bin(int(ipToBinary(temp),2) - int("1",2)).replace("0b", "").rjust(32, "0")
            temp = binaryToIp(temp)
            output.append(temp)

            #Broadcast Address
            broadcast = broadcastAddress(currentAddress,currentSubnetMask)
            output.append(broadcast)

            #Usable Ip num
            usableIpNum = int((2 ** hosts) - 2)
            output.append(usableIpNum)

            #Free IP's
            unusedAddress = int((2 ** hosts) - 2) - j[1]
            output.append(unusedAddress)

            print(output)

            results.append(output)

            networkId += 1
            temp = broadcastAddress(currentAddress,currentSubnetMask)
            temp = bin(int(ipToBinary(temp), 2) + int("1", 2)).replace("0b", "").rjust(32, "0")
            temp = binaryToIp(temp)
            currentAddress = temp

    elif Prefixchecker(prefixLength) == False:
        print("Invalid Prefix Length Input!")
    
    else:
        print("Invalid Ip Address Input!")


            
            
        
    
    

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
