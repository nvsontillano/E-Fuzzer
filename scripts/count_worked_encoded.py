import sys
import re
import operator

result_file = sys.argv[1]
encoder_file = sys.argv[2]

encoder_list = {}

with open(encoder_file, "r") as rf:
	contents = rf.read()

	contents = contents.split('\n')
	for item in contents:
		encoder_list[item] = 0

with open(result_file, "r") as rf:
	contents = rf.read()

#print(encoder_list)

for key in encoder_list.keys():
	
	occurence = len(re.findall(" "+key+"\n", contents))

	encoder_list[key] = occurence
	#print("[*] {} : {} worked".format(key, occurence))


sorted_list = sorted(encoder_list.items(), key=operator.itemgetter(1))

for value in sorted_list:
	
	print("[*] {} : {} worked".format(value[0], value[1]))







