#! /bin/bash

zip_name=$(echo "$1.zip")

echo "[*] Zipping...";
#Zipping
zip -r "$zip_name" $1*
echo "[*] Done!";

echo "[*] Emailing...";

for count in {1..100}
do

echo -e "Tapos na po mga boxzs:\n\nTime Ended: "$(date) | mutt -s "Thesis Script Run" -a $zip_name -- altelusenyodelus@gmail.com;
sleep 1;

done
echo "[*] Done!";







