import secrets
import hashlib
import re
p = re.compile(b'\'=\'')

found = False
while (found == False):
	password = secrets.token_hex(16) 
	theHash = hashlib.md5(password.encode('utf-8')).digest()
	if p.match(theHash) != None:
		found = True
	
print(password)
print(theHash)