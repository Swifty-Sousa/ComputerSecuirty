from pymd5 import md5, padding
seed = "Use HMAC, not hashes"
Hash = md5()
Hash.update(seed)
print("MD5 hash of 'Use HMAC, not hashes' is: ", Hash.hexdigest())

#Guess the length of m
length_of_m = 20
#setting the function’s message length counter to the size of m plus the padding (a multiple of the block size)
bits = (length_of_m + len(padding(length_of_m *8)))*8
extension = "Good advice"
test = md5(state=bytes.fromhex(Hash.hexdigest()), count=bits)
test.update(extension)
print("Hash extended with 'Good advice.' is: ", test.hexdigest())
#Verify that test equals the expected MD5 hash
expectedVal = md5()
expectedVal.update(seed.encode() + padding(len(seed)*8) + extension.encode())
print("Expected hash with extension is: ", expectedVal.hexdigest())



#Accepts an authorized API URL as a command line argument (sys.argv[1])
###
inputURL = "https://project1.ecen4133.org/elpa8934/lengthextension/api?token=785929c5bbf62fc65fde5855c61c28f7&command=SprinklersPowerOn"
#pull out token
token = "785929c5bbf62fc65fde5855c61c28f7"
#pull out everything after first command=
everythingElse = "SprinklersPowerOn"

Hash = md5()
Hash.update(unputIRL)
print("MD5 hash of inputURL is: ", Hash.hexdigest())
###

#Modifies the URL so that it will execute the UnlockSafes command
###
#Length 8 byte password
length_of_m = 8
#set message length counter to the size of m plus the padding
bits = (length_of_m + len(padding(length_of_m *8)))*8
unlockCommand = "&command=UnlockSafes"
modifiedURL = unputURL + token + unlockCommand
###

#Prints only the modified URL
print("Modified URL to modifiedURL)

