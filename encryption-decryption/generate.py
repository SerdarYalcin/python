from encodings import utf_8
from lib2to3.pgen2 import token
from cryptography.fernet import Fernet
key = Fernet.generate_key()
chiper_suite = Fernet(key)
ciphered_text = chiper_suite.encrypt(b"Qwerty2020!!!!")
print (str(ciphered_text, 'utf_8'))
#print (key)ecn
