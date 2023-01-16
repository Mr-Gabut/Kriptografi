import hashlib
plaintext=input("Nilai string : ")
md5 = hashlib.md5(plaintext.encode())
print ("Nilai MD5 nya : ", md5.hexdigest())