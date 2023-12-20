#!/bin/bash
#demofile2.txt
file_path="choice_script_file.txt"
input_string=$(<"$file_path")
IFS=','
read -ra myArray <<< "$input_string"
#IFS=' '
#userResponse=("1.1.6" "1.7.5" "1.7.6")
#userResponse=("0")
#echo "${myArray[2]}"

for element in "${myArray[@]}"; do
  #echo "$element"
  if [ "$element" = "1" ]; then
      source Hard_Script_1.1.4.sh
  fi
  if [ "$element" = "2" ]; then
      source Hard_Script_1.1.5.sh
  fi
  if [ "$element" = "3" ]; then
      source Hard_script_1.1.6.sh
  fi
  if [ "$element" = "4" ]; then
      source Hard_Script_1.3.2.sh
  fi
  if [ "$element" = "5" ]; then
      source Hard_Script_1.6.1.1.sh
  fi
  if [ "$element" = "6" ]; then
      source Hard_Script_1.6.1.2.sh
  fi
  if [ "$element" = "7" ]; then
      source Hard_Script_1.6.1.3.sh
  fi
  if [ "$element" = "8" ]; then
      source Hard_Script_1.7.4.sh
  fi
  if [ "$element" = "9" ]; then
      source Hard_Script_1.7.5.sh
  fi
  if [ "$element" = "10" ]; then
      source Hard_Script_1.7.6.sh    
  fi
done
