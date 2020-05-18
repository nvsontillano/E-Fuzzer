#! /bin/bash

target_url=$1
method=$2
normal_count=$3
cookie=$4
test_name=$5
payloads_folder=$6

files=$(ls $payloads_folder);

for file in $files;
do
	dir_name=$(echo $test_name)_$(date +%F)_$(echo $file | cut -d '.' -f 1);
	
	#create a directory named $dir_name
	mkdir $dir_name;
	
	##name of the urlencoded file
	#urlencoded=$(pwd)/$dir_name/$(echo "url_encoded_"$file);

	#name of the result file	
	result_file=$(pwd)/$dir_name/$test_name$file;
	
	#echo "[*] URL Encoding payload: "$file;
	## Running url encoding
	#python3 urlencoder.py $payloads_folder/$file > $urlencoded;
	#echo "[*] URL Encoding save location: "$urlencoded;	

	echo "[*] Running Normal Script...";
	# Running script normal
	python sqli_leak_normal.py "$target_url" "$method" "$(echo $payloads_folder)/$file" "$cookie" "$normal_count" "$(echo $result_file).normal"

	#echo "[*] Running Encoded Script...";
	## Running script encoded
	python sqli_leak_encoded.py "$target_url" "$method" "$(echo $payloads_folder)/$file" "$cookie" "$normal_count" "$(echo $result_file).encoded"

	#echo "[*] Creating Statistics...";
	## Stats
	python3 count_worked_encoded.py "$(echo $result_file).encoded" "encoder_lists.txt" > $(echo $dir_name/$file);
	
done

# Compressing and emailing
./zip_and_email.sh "$test_name"
