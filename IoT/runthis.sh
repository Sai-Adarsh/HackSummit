#!/bin/sh

CT=0


rm *.jpg

while [ True ]
do
	FNAME="pipic$CT.jpg"

	#Taking a snap and sending it to server
	raspistill -w 640 -h 480 -o "$FNAME"
	python imgproc.py $FNAME
	RESULT=$(curl -s  http://thermalstress.herokuapp.com/api -F "file=@$FNAME" | grep -i "result" | awk '{print $2}' | sed 's/\"//g')
	echo "$FNAME uploaded..."

	#Getting result
	echo "RESULT = $RESULT"

	#Preparing for next cycle
	CT=$((CT+1))
	rm $FNAME
done
