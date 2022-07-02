from cryptography.fernet import Fernet
key = b'1lJywpzg8mqytKBIhGEZd0ApquuF13DwR-zWUUw068c='
cipher_suite = Fernet(key)
ciphered_text = b'gAAAAABircYeSPEU4DDHjq88imhhaWWB8I3aayLrmKir1ov_9By6RDagJlXC1Yu9AyOO4Vn3GesnH1Kry0AfJ-N3amONczz72g=='
unciphered_text = (cipher_suite.decrypt(ciphered_text))
print(unciphered_text)
