import secrets
import hashlib
import re
p = re.compile(b'\'=\'')

found = False
i = 0
while (found == False):
	password = secrets.token_hex(16) 
	theHash = hashlib.md5(password.encode('utf-8')).digest()
	if p.match(theHash) != None:
		found = True
	i = i + 1
	
print(password)
print(theHash)