from lab4 import *
import sys

listOfLinesInDNS = dnsList("./dns_list.txt")
listOfLinesInHosts = dnsList("./hosts")
print(listOfLinesInHosts)

insertDNSatIndex = listOfLinesInHosts.index("\n")

#using list slicing
listOfLinesInHosts[insertDNSatIndex:insertDNSatIndex] = listOfLinesInDNS

print(listOfLinesInHosts)

#joining in empty string to convert list in string
c = "".join(listOfLinesInHosts)
print(c)

try:
  fileHostsInWriteMode = open("./hosts","w")
  content = "".join(listOfLinesInHosts)  # conversion from list to string
  fileHostsInWriteMode.write(content)
except FileNotFoundError as error:
  print(error)

