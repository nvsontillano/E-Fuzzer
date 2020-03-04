#! /bin/bash

target_url=$1
data=$2
method=$3
normal_count=$4
cookie=$5
test_name=$6
payloads_folder=$7

files=$(ls $payloads_folder);

for file in $files;
do
	dir_name=$(echo $test_name)_$(date +%F)_$(echo $file | cut -d '.' -f 1);
	
	#create a directory named $dir_name
	mkdir $dir_name;
	
	#name of the urlencoded file
	urlencoded=$(pwd)/$dir_name/$(echo "url_encoded_"$file);

	#name of the result file	
	result_file=$(pwd)/$dir_name/$test_name$file;
	
	echo "[*] URL Encoding payload: "$file;
	# Running url encoding
	python3 urlencoder.py $payloads_folder/$file > $urlencoded;
	echo "[*] URL Encoding save location: "$urlencoded;	

	echo "[*] Running Normal Script...";
	# Running script normal
	~/thesis/E-Fuzzer/scripts/sqli_leak_normal.sh "$target_url" $urlencoded "$data" $method "$(echo $result_file).normal" $normal_count "$cookie"

	echo "[*] Running Encoded Script...";
	# Running script encoded
	~/thesis/E-Fuzzer/scripts/sqli_leak_3.sh "$target_url" $urlencoded "$data" $method "$(echo $result_file).encoded" $normal_count "$cookie"

	echo "[*] Creating Statistics...";
	# Stats
	python3 count_worked_encoded.py "$(echo $result_file).encoded" "encoder_lists.txt" > $(echo $dir_name/stats.txt);
	
done










