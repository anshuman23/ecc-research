import seccure
import random
import string
import time,requests
from flask import Flask
# Step 1

# Converting string to byte array
#b = bytearray(testString)
#a = b.decode('utf-8')
#print a

#byteString  =''.join(format(x, 'b') for x in bytearray(testString))
testString = 'Hello world! My name is Anshuman and this code is written in Python.'
byteString = ''
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
    r.append(random.choice(enc_list))
    enc_list.remove(r[y])
    packet[y] = packet[y] + r[y]
    #print packet[y]
encTime = 0

private_key = '77'#random.choice(string.digits)
#print private_key

public_key = str(seccure.passphrase_to_pubkey(private_key))
ciphertext = []

###Encryption phase
for z in range(7):
    t1 = time.time()
    ciphertext.append(seccure.encrypt(packet[z][:-3], public_key))
    t2 = time.time()
    encTime = encTime + (t2-t1)
    #print ciphertext[z]    
print 'Encryption Time for the iteration',encTime

app = Flask(__name__)
@app.route('/cloud1', methods=['GET'])
def get_tasks1():
    return ciphertext[0]

@app.route('/cloud2', methods=['GET'])
def get_tasks2():
    return ciphertext[1]

@app.route('/cloud3', methods=['GET'])
def get_tasks3():
    return ciphertext[2]

@app.route('/cloud4', methods=['GET'])
def get_tasks4():
    return ciphertext[3]

@app.route('/cloud5', methods=['GET'])
def get_tasks5():
    return ciphertext[4]

@app.route('/cloud6', methods=['GET'])
def get_tasks6():
    return ciphertext[5]

@app.route('/cloud7', methods=['GET'])
def get_tasks7():
    return ciphertext[6]

if __name__ == '__main__':
    app.run(debug=True)    