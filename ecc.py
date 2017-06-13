import seccure
import random
import string

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

while 1:
    dataBuffer = ''
    packet = []
    if dataSize > N: #This chosen value signifies the number of clouds we will divide the data on. If data is short of this value we will fill it with dummy values like spaces. -Anshuman
        dataBuffer = byteString[N:]
        byteString = byteString[:N]


    
    
    print dataSize
    print len(byteString)

    for x in range(7):
        packet.append(byteString[(x*32):((32*(x+1)))])
        print packet[x]
    # Step 2

    enc_list = ['001','010','011', '100', '101', '110', '111']
    r = []
    
    for y in range(7):
        r.append(random.choice(enc_list))
        enc_list.remove(r[y])
        packet[y] = packet[y] + r[y]
        #print packet[y]
    
    #private_key = '101010101101111100010110011101010'
    private_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))
    print private_key
    public_key = str(seccure.passphrase_to_pubkey(private_key))
    ciphertext = []
    decrypted = []
    
    ###Encryption phase
    for z in range(7):
        ciphertext.append(seccure.encrypt(packet[z][:-3], public_key))
        print ciphertext[z]

        if packet[z][-3:] == '000':
            print 'SEND packet[z][:-3] TO CLOUD 1'

        if packet[z][-3:] == '001':
            print 'SEND packet[z][:-3] TO CLOUD 2'

        if packet[z][-3:] == '010':
            print 'SEND packet[z][:-3] TO CLOUD 3'

        if packet[z][-3:] == '011':
            print 'SEND packet[z][:-3] TO CLOUD 4'

        if packet[z][-3:] == '100':
            print 'SEND packet[z][:-3] TO CLOUD 5'
            
        if packet[z][-3:] == '101':
            print 'SEND packet[z][:-3] TO CLOUD 6'

        if packet[z][-3:] == '110':
            print 'SEND packet[z][:-3] TO CLOUD 7'

        if packet[z][-3:] == '111':
            print 'SEND packet[z][:-3] TO CLOUD 8'

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

    decrypted_bytestring = ''

    for k in range(7):
        decrypted.append(seccure.decrypt(ciphertext[k], private_key))
        print decrypted[k]
        decrypted_bytestring += decrypted[k]

    print decrypted_bytestring == byteString
    print len(decrypted_bytestring)

    strdec = ''
    for l in range(len(decrypted_bytestring)/7):
        strdec += chr(int(decrypted_bytestring[l*7:(l+1)*7],2))
    
    print strdec
    decryptedTextString += strdec
    
    byteString = dataBuffer
    if len(dataBuffer) == 0:
        break

print "\nFinal Decrypted String: {}".format(decryptedTextString)
