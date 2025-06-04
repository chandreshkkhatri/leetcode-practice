#!/usr/bin/env bash
declare -A frequency_table

while IFS= read -r line; do
    for word in $line; do
        ((frequency_table["$word"]++)) 
    done
done < words.txt 

for key in "${!frequency_table[@]}"; do
    echo "$key ${frequency_table[$key]}"
done | sort -k2 -nr