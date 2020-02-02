from pymd5 import md5, padding
import urllib.parse
import sys

#Prepares URL variables form given command line argument
###
inputURL = sys.argv[1]
#pull out first piece of URL
holder=inputURL.split('=')
prefix = holder[0] + "="
#pull out token
holder2=holder[1].split('&')
holder2=holder2[0]
token = holder2
#pull out everything after first &
holder=inputURL.split('&', 1)
everythingElse = holder[1]
###

#Modifies the URL so that it will execute the UnlockSafes command
###
#Length of (8 byte password || everythingElse)
length_of_m = 8 + len(everythingElse)
#set message length counter to the size of m plus the padding
bits = (length_of_m + len(padding(length_of_m *8)))*8
unlockCommand = "&command=UnlockSafes"
test = md5(state=bytes.fromhex(token), count=bits)
test.update(unlockCommand)
modifiedURL = prefix + urllib.parse.quote(test.hexdigest()) + "&" + everythingElse + urllib.parse.quote(padding(length_of_m *8)) + unlockCommand
###

#Prints only the modified URL
###
print(modifiedURL)
###

