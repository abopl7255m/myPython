import win32api
import win32security
import win32print
import win32file
import servicemanager

print("STARTING THE AWESOME PROGRAM WITH BEEEEEEP!!")

win32api.Beep(1000,2000) #used beeps function from win32api module
computerName = win32api.GetComputerName()
print ("Computer Name", computerName) #used GetcomputerName function from win32api module
print ("My name is ", win32api.GetUserName())# uset GetUserName function from win32api module


FILENAME = "file1.txt"

#win32file.CreateFile

#pyHANDLE = CreateFile(fileName, desiredAccess , shareMode , attributes , CreationDisposition , flagsAndAttributes , hTemplateFile )

hFile = win32file.CreateFile(FILENAME, 2, 3, None, 2, 0, None)

data = bytes("This is the data", 'utf-8')

win32file.WriteFile(hFile, data, None)

print("Writing into file", FILENAME)
servicemanager.LogWarningMsg("file "+ FILENAME +" is open in write mode. close the handle")

win32file.CloseHandle(hFile)

print("Copying file : " + FILENAME + " to file2.txt")

win32file.CopyFile(FILENAME, "file2.txt", 0)


#win32file.DeleteFile("file1.txt")
#win32file.DeleteFile("file2.txt")
#win32file.DeleteFile("temp.txt")


security_descriptor = win32security.GetFileSecurity (FILENAME, win32security.OWNER_SECURITY_INFORMATION)#used GetFileSecurity function from win32security module(filename, flag(which specifies the information requested))
owner_sid = security_descriptor.GetSecurityDescriptorOwner ()
name, domain, type = win32security.LookupAccountSid (None, owner_sid)#used LookUpAccountSid function from win32security module
print(win32security.ConvertSidToStringSid(owner_sid))##used ConvertSidToStringSid function from win32security module

print ("File owned by %s\\%s" % (domain, name))

choice = input("Delete file "+ FILENAME + "? (yes/no)")

if choice == "yes":
  win32file.DeleteFile(FILENAME)



#NetUserGetInfo(server, username, level)
#print(win32net.NetUserGetInfo(socket.gethostbyname(socket. gethostname()), "ranga", 0))#used NetUserGetInfo function from win32net module

print("Printer information of computer : ", computerName) 

printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_NAME, None, 1)

for printer in printers:
    print(printer)

defaultPrinter = win32print.GetDefaultPrinter()

print(win32print.GetDefaultPrinter())

#Return PyPrinterHANDLE
hPrinter = win32print.OpenPrinter(defaultPrinter)
if hPrinter:
  print("Able to open printer", defaultPrinter)
  servicemanager.LogInfoMsg("Able to open printer" + defaultPrinter)
else:
  print("Unable to open printer", defaultPrinter)
  servicemanager.LogErrorMsg("Unable to open printer", defaultPrinter)

win32print.ClosePrinter(hPrinter)



servicemanager.LogInfoMsg("This is info message")
servicemanager.LogErrorMsg("This is error message")
servicemanager.LogWarningMsg("This is warning message")








