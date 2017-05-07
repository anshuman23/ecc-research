import random
teststring = 'Hello my name is shivam.'
# Step 1

# Converting string to byte array
b = bytearray(teststring)
encstr = ''

# Concatenating the byte to form a string
for i in b:
	encstr = encstr + str(i)
print encstr
# converting string to binary
binstr = bin(long(encstr))
binstr = binstr[2:]
print binstr
# Calculating length of packet
paclen = len(binstr)/4
pacrem = len(binstr)%4
print paclen

# Making the packets by equally dividing the concatenated string.
packets = []
pacstr1 = binstr[-paclen:]
pacstr2 = binstr[-paclen*2:-paclen]
pacstr3 = binstr[-paclen*3:-paclen*2]
pacstr4 = binstr[0:-paclen*3]
print "Packet 1"
print pacstr1
print len(pacstr1)
print "Packet 2"
print pacstr2
print len(pacstr2)
print "Packet 3"
print pacstr3
print len(pacstr3)
print "Packet 4"
print pacstr4
print len(pacstr4)

# Step 2

# Adding 00,01,10,11 to all the packets randomly

enc_list = ['00','01','10','11']

r1 = random.choice(enc_list)
enc_list.remove(r1)
r2 = random.choice(enc_list)
enc_list.remove(r2)
r3 = random.choice(enc_list)
enc_list.remove(r3)
r4 = random.choice(enc_list)
enc_list.remove(r4)

pacstr1 = pacstr1 + str(r1)
pacstr2 = pacstr2 + str(r2)
pacstr3 = pacstr3 + str(r3)
pacstr4 = pacstr4 + str(r4)

print pacstr1
print pacstr2
print pacstr3
print pacstr4
