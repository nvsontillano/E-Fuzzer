#! /bin/bash

while read line;
do

	result=$(echo $line | ./urlencoder);
	echo $result;
done < "encoder_lists.txt"









