# !/usr/bin/bash URL=$1 filename=$2 data=$3 method=$4 output_file=$5

while read line; do fo value in $(iconv -l | tail -n+5 | sed "s/\/\///g"); do echo [*] - $value; to_send=$(echo -e "$line" | iconv -t $value); #Changing the data to_send=$(echo $data | sed "s/X/$(pintf "%q" "$to_send")/g");

 echo $to_send; if [[ $method == *"post"* ]]; then esult=$(cul $URL --data $to_send -i | gep -P "HTTP/[1-3]\.[0-5] 5"); else esult=$(cul $URL/?$to_send | gep -P "HTTP/[1-3]\.[0-5] 5"); fi

 echo $esult; if [ ${#esult} -gt 1 ]; then echo [+] - $value >> $output_file; echo [+] - $to_send >> $output_file; echo "" - >> $output_file; fi done done < $filename
