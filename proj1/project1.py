
""" This is the documenatation followed by the code for CPRG-260-CSB Project # 1.
 The code will be submitted in D2L and this information is to validate that none of these below 
 details of this project has been published in any other forum such as Youtube, or any other
 public video sharing services, or social media.
 
 As per the project the requiresd python requirments have been used such as {Functions, MOdules, Variables:Constants, Variables: Data types,  }
 
 
 """


import os
import platform
import socket

def readFile(filename):
  """ Reads the provided file with exception handling
  
  Parameters
  ---------
  filename : str
    File name to be open in read mode
    
  Returns
  -------
  list
    List of lines from the file 
  
  """
  try:
    readOnlyFile = open(filename, "r") # open file in read mode
    listOfLines = readOnlyFile.readlines() # files content will be converted into list of lines
    return listOfLines
  except FileNotFoundError as error: # Exception Handling with catching error and printing error
    print(error)

def print_cpu_details():
  cpuinfo = readFile("/proc/cpuinfo")
  print(cpuinfo[0])
  print(cpuinfo[1])
  print(cpuinfo[3])
  print(cpuinfo[4])
  print(cpuinfo[8])
  
def print_dash_line():
  print("-" * 30)

 
def print_user_details():
  lines = readFile("/etc/passwd");   # calling readFile function to get all the linse in file as list
  user_name_list = []   # contains all the users
  user_id_list = []     # contains all the user ids
  group_id_list = []    # contains all the group ids
  user_shell_list = []  # contans all the users shells 
  for line in lines:
    print_dash_line()
    splittedLine = line.split(":") # splitting string based on colon : as a seperator 
    # example line variable is root:1:1:1:root:/root:/root/bin/shell
    print("User: " + splittedLine[2] + "\t Group: " + splittedLine[3])
    print(splittedLine[0] + "\t" + splittedLine[4])
    print_dash_line()

print("System Informations : \n")
	
print("Hostname	: ", platform.node()) # we can use socket.gethostname() as well

print("My Ip Address   : ", socket.gethostbyname(socket.gethostname()))

print_cpu_details()

print_dash_line()

print("List of all users and group they are associated with : \n")
	
print_dash_line()

print_user_details()

SERVICE_STATUS_ALL = "service --status-all"
os.system(SERVICE_STATUS_ALL)

