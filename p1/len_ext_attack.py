from pymd5 import md5, padding
seed= "Use HMAC, not hashes"
Hash= md5()
Hash.update(seed)
print(Hash.hexdigest(), "which matches what is expected")

bits = "some shite"
test= md5(state=bytes.fromhex("3ecc68efa1871751ea9b0b1a5b25004d"), count=bits)