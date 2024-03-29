#PrettyTable link: https://pypi.org/project/prettytable/
#Installation: python -m pip install -U prettytable
#python -m pip install -U git+https://github.com/jazzband/prettytable

from prettytable import PrettyTable

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
    #check if valid
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
    temp = temp.ljust(32,"0")
    return temp

def binaryToIp(binary):
    temp = [binary[x:x+8] for x in range(0, len(binary), 8)]
    temp = list(map(lambda temp: int(temp, 2), temp))
    ipAddress = ""
    for x in temp:
        ipAddress = ipAddress + str(x) + "."
    return ipAddress[:-1]
    
def octetToBinary(value):
    octet = ""
    octet = bin(int(value)).replace("0b", "")
    octet = octet.rjust(8, "0")
    octet = str(octet)
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

def displayTable(results):
    #print(results)
    #Network Information
    print("\nNetwork Information\n")
    table = PrettyTable(["ID", "Network Name", "Network Address", "Subnet Mask" , "Prefix Length"])
    for i in range(len(results)):
        table.add_row([results[i][0], results[i][1], results[i][2], results[i][3], results[i][4]])
    print(table)

    #Address Information
    print("\nAddress Information\n")
    table2 = PrettyTable(["ID", "First Usable Addr", "Last Usable Addr", "Broadcast Address" , "Usable IPs", "Free IPs"])
    for j in range(len(results)):
      table2.add_row([results[j][0], results[j][5], results[j][6],results[j][7], results[j][8], results[j][9]])
    print(table2)



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
            #Network Information
            output = []
            
            #ID
            output.append(int(networkId + 1))
            #Network Name
            output.append(j[0])
            #Curent Network 
            output.append(currentAddress)
            #Subnet Mask
            hosts = int(getHostsNum(j[1]))
            currentSubnetMask = 32 - hosts
            #print(binaryToIp(subnetMaskToBin(currentSubnetMask)))
            output.append(binaryToIp(subnetMaskToBin(currentSubnetMask)))
            #Prefix Length
            output.append("/" + str(currentSubnetMask))
        

            #Address Information    
            #first usable address
            temp = networkAddress(currentAddress,currentSubnetMask)
            temp = bin(int(ipToBinary(temp),2) + int("1",2)).replace("0b", "")
            temp = temp.rjust(32, "0")
            temp = binaryToIp(temp)
            output.append(temp)
            #last usable address
            temp = broadcastAddress(currentAddress,currentSubnetMask)
            temp = bin(int(ipToBinary(temp),2) - int("1",2)).replace("0b", "")
            temp = temp.rjust(32, "0")
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
            #print(output)

            results.append(output)

            #For next ip address
            networkId += 1
            temp = broadcastAddress(currentAddress,currentSubnetMask)
            temp = bin(int(ipToBinary(temp), 2) + int("1", 2)).replace("0b", "")
            temp = temp.rjust(32, "0")
            temp = binaryToIp(temp)
            currentAddress = temp

        displayTable(results)

    elif Prefixchecker(prefixLength) == False:
        print("Invalid Prefix Length Input!")
    
    else:
        print("Invalid Ip Address Input!")

def checkAddressClass():
    ipInput = input("Input IP Address: ")

    if IPV4checker(ipInput) == True:
        octets = list(map(int, ipInput.split(".")))
        ipClass = ""
        classPrefix = 0

        if octets[0] >= 0 and octets[0] <= 126:
            ipClass = "A"
            classPrefix = 8
        
        elif octets[0] == 127:
            ipClass= "Special Purpose"
            classPrefix = 8
        
        elif octets[0] >= 128 and octets[0] <= 191:
            ipClass = "B"
            classPrefix = 16
        
        elif octets[0] >= 192 and octets[0] <= 223:
            ipClass = "C"
            classPrefix = 24
        
        elif octets[0] >= 224 and octets[0] <= 239:
            ipClass = "D"
            classPrefix = 0
        
        elif octets[0] >= 240 and octets[0] <= 255:
            ipClass = "E"
            classPrefix = 0

        if classPrefix != 0:
            netAddress = networkAddress(ipInput,classPrefix)
        
        if ipClass == "Special Purpose":
            print("The IP Address: " + ipInput + " is a " + ipClass + " Address indicating the LoopBack Address range of " + netAddress + "/" + str(classPrefix))
        
        elif ipClass == "D" or ipClass == "E":
            print("The IP Address: " + ipInput + " is a Class " + ipClass + " Address")
        
        else:
            print("The IP Address: " + ipInput + " is a Class " + ipClass + " Address, whose network address is " + netAddress + "/" + str(classPrefix))

    else:
        print("Invalid Ip Address Input")


    
def checkAddressType():
    print("Sample: 192.168.1.1/24")
    ipInputString = input("Input Ip Address: ")
    temp = ipInputString.split("/")
    ipAdd = temp[0]
    prefix = int(temp[1])

    if IPV4checker(ipAdd) and Prefixchecker(prefix) == True:
        ipType = ""
        if (ipAdd == networkAddress(ipAdd,prefix)):
            ipType = "Network"
        elif (ipAdd == broadcastAddress(ipAdd,prefix)):
            ipType = "Broadcast"
        else:
            ipType = "Host"
        
        print("The IP Address " + ipInputString + " is a " + ipType + " Address ")
    
    elif Prefixchecker == False:
        print("Invalid Prefix Input")
    
    else:
        print("Invalid Ip Address Input")

def exit():
    print("Good Luck Network Admin!")

def main():
  loop = True
  while loop == True:
    print("\nHello there Network Admin!\n")
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
      loop = False
      exit()

#main function
#install PrettyTable first
main()
