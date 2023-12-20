#!/bin/bash

file_path="choice_script_file.txt"
input_string=$(<"$file_path")
IFS=','
read -ra myArray <<< "$input_string"
IFS=' '
userResponse=("1.1.6" "1.7.5" "1.7.6")

for element in "${userResponse[@]}"; do
  if [ "$element" = "1.1.4" ]; then
      source Hard_Script_1.1.4.sh
  fi
  if [ "$element" = "1.1.5" ]; then
      source Hard_Script_1.1.5.sh
  fi
  if [ "$element" = "1.1.6" ]; then
      source Hard_script_1.1.6.sh
  fi
  if [ "$element" = "1.3.2" ]; then
      source Hard_Script_1.3.2.sh
  fi
  if [ "$element" = "1.6.1.1" ]; then
      source Hard_Script_1.6.1.1.sh
  fi
  if [ "$element" = "1.6.1.2" ]; then
      source Hard_Script_1.6.1.2.sh
  fi
  if [ "$element" = "1.6.1.3" ]; then
      source Hard_Script_1.6.1.3.sh
  fi
  if [ "$element" = "1.7.4" ]; then
      source Hard_Script_1.7.4.sh
  fi
  if [ "$element" = "1.7.5" ]; then
      source Hard_Script_1.7.5.sh
  fi
  if [ "$element" = "1.7.6" ]; then
      source Hard_Script_1.7.6.sh    
  fi
done
