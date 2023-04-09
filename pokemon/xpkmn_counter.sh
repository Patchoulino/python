#!/bin/bash
pokemon=$1
if [ -z $pokemon ]; then
	grep / pkmn/* | cut -d : -f1 | sort | uniq -c | sort -n
else
	grep / pkmn/* | cut -d : -f1 | sort | uniq -c | sort -n | grep $pokemon
fi
