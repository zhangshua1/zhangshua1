#!/bin/bash
[ -e "thesame" ]&&{
        rm -f thesame
        }
[ "$#" != "2" ]&& {
        echo "input error"
        exit 0
        }
sort -u $1 > uniq1
sort -u $2 > uniq2
for Text1 in `cat  uniq1`
do
        for Text2 in `cat uniq2`
        do
                if [ "$Text1" =  "$Text2" ]
                then
                echo $Text1 >> thesame
                fi
        done
done
Except=`sed 's/ /|/g' thesame`
grep -vE "$Except" uniq1 > onlyinfile1
grep -vE "$Except" uniq2 > onlyinfile2