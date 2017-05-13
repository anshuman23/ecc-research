import seccure
import random

testString = 'Hello world! My name is Anshuman and this code is written in Python.'

# Step 1

# Converting string to byte array
#b = bytearray(testString)
#a = b.decode('utf-8')
#print a

byteString  =''.join(format(x, 'b') for x in bytearray(testString))
dataSize = len(byteString)
dataBuffer = 'empty'
N = 256
packet = []

if dataSize > N: #This chosen value signifies the number of clouds we will divide the data on. If data is short of this value we will fill it with dummy values like spaces. -Anshuman
    dataBuffer = byteString[N:dataSize-1]
    byteString = byteString[0:N-1]

print dataSize
print len(byteString)

for x in range(8):
    packet.append(byteString[(x*32):((32*(x+1))-1)])

# Step 2

enc_list = ['000','001','010','011', '100', '101', '110', '111']
r = []

for y in range(8):
    r.append(random.choice(enc_list))
    enc_list.remove(r[y])
    packet[y] = packet[y] + r[y]
    print packet[y]
    
private_key = '101010101101111100010110011101010'
public_key = str(seccure.passphrase_to_pubkey(private_key))
ciphertext = []
decrypted = []

#Encryption phase
for z in range(8):
    ciphertext.append(seccure.encrypt(packet[z][:-3], public_key))
    print ciphertext[z]
    
#Decryption phase
for k in range(8):
    decrypted.append(seccure.decrypt(ciphertext[k], private_key))
    print decrypted[k]
