def dnsList(ipDetails):
  try:
    fileObject = open(ipDetails, 'r')
    readIpLines = fileObject.readlines()
    return readIpLines
  except FileNotFoundError as error:
    print(error)
 
