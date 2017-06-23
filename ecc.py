import seccure
import random
import string
import time
#testString = 'Hello world! My name is Anshuman and this code is written in Python.'

testString = raw_input('Enter message to encrypt: ')

# Step 1

# Converting string to byte array
#b = bytearray(testString)
#a = b.decode('utf-8')
#print a

#byteString  =''.join(format(x, 'b') for x in bytearray(testString))

byteString = ''
decryptedTextString = ''
for x in bytearray(testString):
    substr = format(x,'b')
    if len(substr) < 7:
        substr = '0' + substr
    byteString += substr
    
dataSize = len(byteString)
#dataBuffer = ''
#N = 256
N = 224
enc_times_data = []
dec_times_data = []
tot_times_data = []
while 1:
    dataBuffer = ''
    
    
    packet = []
    if dataSize > N: #This chosen value signifies the number of clouds we will divide the data on. If data is short of this value we will fill it with dummy values like spaces. -Anshuman
        dataBuffer = byteString[N:]
        byteString = byteString[:N]
    enc_list = ['001','010','011', '100', '101', '110', '111']
    r = []
    #print dataSize
    #print len(byteString)
    t1 = time.time()
    tot1 = t1
    for x in range(7):
        packet.append(byteString[(x*32):((32*(x+1)))])
        #print packet[x]
    # Step 2
    for y in range(7):
        r.append(random.choice(enc_list))
        enc_list.remove(r[y])
        packet[y] = packet[y] + r[y]
        #print packet[y]
    
    #private_key = '101010101101111100010110011101010'
    private_key = random.choice(string.digits)
    #print private_key
    public_key = str(seccure.passphrase_to_pubkey(private_key))
    ciphertext = []
    decrypted = []
    
    ###Encryption phase
    for z in range(7):
        ciphertext.append(seccure.encrypt(packet[z][:-3], public_key))
        #print ciphertext[z]
    t2 = time.time()
        
    ###Decryption phase
    #For benchmarking and an easier to understand algorithm we are not fetching data from the different cloud sources and combining it as our purpose here is to test the speed of this proposed encryption algorithm against RSA
    #Ideally, this would go something like this -
    #RECEIVE packet data from CLOUD 1
    #RECEIVE packet data from CLOUD 2
    #RECEIVE packet data from CLOUD 3
    #RECEIVE packet data from CLOUD 4
    #RECEIVE packet data from CLOUD 5
    #RECEIVE packet data from CLOUD 6
    #RECEIVE packet data from CLOUD 7
    #RECEIVE packet data from CLOUD 8
    #Combine packets and store in the list cyphertext in the order that they appeared
    
    print 'Encryption Time for the iteration',t2-t1
    enc_times_data.append(t2-t1)
    
    decrypted_bytestring = ''
    t1 = time.time()
    for k in range(7):
        decrypted.append(seccure.decrypt(ciphertext[k], private_key))
        #print decrypted[k]
        decrypted_bytestring += decrypted[k]

    #print decrypted_bytestring == byteString
    #print len(decrypted_bytestring)

    strdec = ''
    for l in range(len(decrypted_bytestring)/7):
        strdec += chr(int(decrypted_bytestring[l*7:(l+1)*7],2))
    
    #print strdec
    decryptedTextString += strdec

    t2 = time.time()
    tot2 = t2
    print 'Decryption Time for the iteration',t2-t1
    dec_times_data.append(t2-t1)
    print 'Total Time for the iteration',tot2-tot1
    tot_times_data.append(tot2-tot1)

    byteString = dataBuffer
    if len(dataBuffer) == 0:
        break
    

print enc_times_data

print dec_times_data

print tot_times_data
print 'Encryption Time = ',sum(enc_times_data)
print 'Decryption Time = ',sum(dec_times_data)
print 'Total Time(Encryption + Decryption) = ',sum(tot_times_data)
print "\nFinal Decrypted String: {}".format(decryptedTextString)
