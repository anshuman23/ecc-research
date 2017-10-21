from flask import Flask
from flask import request
import json
import seccure
import random
import string
import time,requests
counter =7
app = Flask(__name__) 

enc_data = {}
@app.route('/determine_escalation/', methods = ['POST'])
def determine_escalation():
	global enc_data
	global counter
	decTime = 0
	decrypted_bytestring = ''
	decryptedTextString = ''
	strdec = ''
	decrypted = []
	private_key = '77'
	jsondata = request.get_data()
	enc_data.update({jsondata[-3:]:jsondata[:-3]}) 
	#stuff happens here that involves data to obtain a result
	result = {'status': 'data received'}
	if counter > 0:
		counter -= 1
	if counter == 0:
		ciphertext = []
		temp = {}
		for el in enc_data:
			temp.update({int(el,2):enc_data[el]})
		for key in sorted(temp.iterkeys()):
			ciphertext.append(temp[key])
		for k in range(7):
			t1 = time.time()
			decrypted.append(seccure.decrypt(ciphertext[k], private_key))
			t2 = time.time()
			decTime = decTime + (t2-t1)
			#print decrypted[k]
			decrypted_bytestring += decrypted[k]
		for l in range(len(decrypted_bytestring)/7):
			strdec += chr(int(decrypted_bytestring[l*7:(l+1)*7],2))
		decryptedTextString = strdec
		print "\nFinal Decrypted String: {}".format(decryptedTextString)
		enc_data={}
		counter = 7
	return json.dumps(result)
if __name__ == '__main__':
    app.run(debug=True)
