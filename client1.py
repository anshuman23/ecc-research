import sys
import json
import requests
import seccure
import random
import string
import time
testString = 'Hello world! My name is Anshuman and this code is written in Python.'
byteString = ''
encTime = 0
for x in bytearray(testString):
    substr = format(x,'b')
    if len(substr) < 7:
        substr = '0' + substr
    byteString += substr
    
dataSize = len(byteString)

print testString

N = dataSize/7
packet = []
enc_list = ['001','010','011', '100', '101', '110', '111']
r = []

for x in range(7):
    packet.append(byteString[(x*N):((N*(x+1)))])
    #print packet[x]
# Step 2
for y in range(7):
    #r.append(random.choice(enc_list))
    packet[y] = packet[y] + enc_list[y]
    #enc_list.remove(r[y])
    #packet[y] = packet[y] + r[y]
    #print packet[y]
private_key = '77'#random.choice(string.digits)
#print private_key

public_key = str(seccure.passphrase_to_pubkey(private_key))
ciphertext = []
###Encryption phase
for z in range(7):
    t1 = time.time()
    ct=seccure.encrypt(packet[z][:-3], public_key)
    #print tt
    ciphertext.append(ct)
    t2 = time.time()
    conv = {'ciphertext':ct,'cloudNo':packet[z][-3:]}
    s = json.dumps(conv,ensure_ascii=False)
    res=requests.post("http://127.0.0.1:5000/determine_escalation/", data=ct+packet[z][-3:]).json()
    print res 
    encTime = encTime + (t2-t1)
    #print ciphertext[z]
print 'Encryption Time for the iteration',encTime
