#!/bin/bash

fizzbuzz(){
	local INPUT=$1
	local OUTPUT=""
	if [[ $(($INPUT % 3)) == 0 ]] 
	then
		OUTPUT="Fizz"
	fi
	if [[ $(($INPUT % 5)) == 0 ]] 
	then
		OUTPUT=$OUTPUT"Buzz"
	fi
	if [[ -z $OUTPUT ]]
	then
		OUTPUT=$INPUT
	fi
	echo $OUTPUT
}
wtffizzbuzz(){
	expr $1 % 15 == 0 > /dev/null && echo FizzBuzz && return || 
	expr $1 % 3 == 0 > /dev/null && echo Fizz && return || 
	expr $1 % 5 == 0 > /dev/null && echo Buzz && return || 
	echo $1 
}
for i in `seq 100`
do
	fizzbuzz $i
done
