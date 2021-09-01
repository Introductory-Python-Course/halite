#!/bin/bash


width=$(( 10 * (2 + $RANDOM % 5)))
height=$(( 10 * (2 + $RANDOM % 5)))
dimensions="$width $height"

arr=(./bots/*)

playerScores=()

# delete unneeded files from directory
for f in "${arr[@]}"; do
   if [ $f = "./bots/hlt.py" ]
   then
     arr=( "${arr[@]/$f}" )
   elif [ $f = "./bots/__pycache__" ]
   then
     arr=( "${arr[@]/$f}" )
   else
     playerScores+=( 0 )
   fi
done

echo "${arr[@]}"

length=$((${#arr[@]}-2))


for i in {1..5}
do
   randomVal=$(($RANDOM % $length))
   randomVal2=$((randomVal + 1+$RANDOM % ($length - 1)))
   player1=${arr[$randomVal]}
   player2=${arr[$(($randomVal2 % $length))]}
   output=$(./halite -d "$dimensions" "python3 $player1" "python3 $player2" -q)
   echo "$output" >> output.txt
   echo "completed match: $i with dimensions: $dimensions"
done

echo "Player Scores: ${#playerScores[@]}"