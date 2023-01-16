import hashlib
import time

counter = 1

md5_hash = input("Hash Md5 : ")
pwdfile = input("Alamat WL : ")

try:
  pwdfile = open(pwdfile, "r")
except:
  print ("File Tidak Ditemukan")
  quit()

for password in pwdfile:
  md5 = hashlib.md5()
  md5.update(password.strip().encode('ascii'))
  start = time.time()
  print ("Coba Pasword : %d: %s" % (counter, password.strip()))
  counter += 1
  end = time.time()
  t_time = end - start
  
  if md5_hash.strip() == md5.hexdigest():
    print ("Passnya adalah : %s" % password.strip())
    print ("Total Waktu : ", t_time, "second")
    time.sleep(5)
    break
  else:
    print ("Password tidak ditemukan :))")