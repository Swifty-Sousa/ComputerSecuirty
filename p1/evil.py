#!/usr/bin/python3
# coding: latin-1

blob = """
               G�vW�p��3ߝK]û�{�)X�#C:yrLz�a��P��m��#�3�s%�47��dJ��r����Ϝb��}\�*v{�61��4�U�w��0Y��Q�]��ׇh����}�G|'�o^����$��6"""
from hashlib import sha256
if (sha256(blob.encode("latin-1", errors="ignore")).hexdigest() == "a9f34719405a944d8d7e0af71a04f2ec5eefee654a6208c907292da4e28ed6f4"):
	print("Use SHA-256 instead!")
else:
	print("MD5 is prefectly secure!")
