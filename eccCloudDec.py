import seccure
import random
import string
import time,requests,unicodedata
decTime = 0
decrypted_bytestring = ''
decryptedTextString = ''
decrypted = []
ciphertext = []
private_key = '77'
for k in range(7):
    t1 = time.time()
    r = requests.get('http://127.0.0.1:5000/cloud'+str(k+1))
    #tempText = unicodedata.normalize('NFKD', r.text).encode('ascii','ignore')
    ciphertext.append(r.text)
    t2 = time.time()
    decTime = decTime + (t2-t1)
    #print decrypted[k]
print '\n\n\n',ciphertext[0],'\n\n'
for k in range(7):
    decrypted.append(seccure.decrypt(ciphertext[k], private_key))
    decrypted_bytestring += decrypted[k]

strdec = ''
for l in range(len(decrypted_bytestring)/7):
    strdec += chr(int(decrypted_bytestring[l*7:(l+1)*7],2))

#print strdec
decryptedTextString = strdec

print 'Decryption Time for the iteration',decTime

print "\nFinal Decrypted String: {}".format(decryptedTextString)