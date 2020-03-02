#! /bin/bash

url_files=$1


today_date=$(date +%F);

mkdir payloads_$today_date;

while read line;
do
	wget "$line" -P ./payloads_$today_date;

done < $url_files










