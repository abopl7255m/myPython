
""" This is the documenatation followed by the code for CPRG-260-CSB Project # 1.
 The code will be submitted in D2L and this information is to validate that none of these below 
 details of this project has been published in any other forum such as Youtube, or any other
 public video sharing services, or social media.
 
 As per the project the requiresd python requirments have been used such as {Functions, MOdules, Variables:Constants, Variables: Data types,  }
 
 
 """


import os
import platform
import socket

OUTPUT_FILE = "output.txt"
SERVICE_STATUS_ALL = "service --status-all >> " + OUTPUT_FILE

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
    append_to_outputfile(error)

def append_to_outputfile(s):
  try:
    fileObject = open("./" + OUTPUT_FILE ,"a")    # open an empty output file in an append mode
    fileObject.write(s) 
  except FileNotFoundError as error:
    append_to_outputfile(error)

def print_cpu_details():
  cpuinfo = readFile("/proc/cpuinfo")
  append_to_outputfile(cpuinfo[0])
  append_to_outputfile(cpuinfo[1])
  append_to_outputfile(cpuinfo[3])
  append_to_outputfile(cpuinfo[4])
  append_to_outputfile(cpuinfo[8])
  
def print_dash_line():
  append_to_outputfile( "\n" + "-" * 30 + "\n")

 
def print_user_details():
  lines = readFile("/etc/passwd");   # calling readFile function to get all the linse in file as list 
  for line in lines:
    print_dash_line()
    splittedLine = line.split(":") # splitting string based on colon : as a seperator 
    # example line variable is root:1:1:1:root:/root:/root/bin/shell
    append_to_outputfile("User: " + splittedLine[2] + "\t Group: " + splittedLine[3] + "\n")
    append_to_outputfile(splittedLine[0] + "\t" + splittedLine[4])
    print_dash_line()

append_to_outputfile("System Informations : \n")

append_to_outputfile("Hostname	: " + platform.node() + "\n") # we can use socket.gethostname() as well

print_cpu_details()

print_dash_line()

append_to_outputfile("List of all users and group they are associated with : \n")
	
print_dash_line()

print_user_details()

os.system(SERVICE_STATUS_ALL)

lines = readFile(OUTPUT_FILE) # we are reading the line in the output file
for line in lines:
  print(line) # after reading we shall though print all the content of the file
  
  
  
  
  
