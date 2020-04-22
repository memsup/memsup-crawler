#!/bin/bash

function trim() {
    local temp="$2"
    if [ $temp != "404" ]; then
        temp=$(sed 's/src=/ /' <<< $temp)
        temp=$(sed 's/"/ /' <<< $temp)
        temp=$(sed 's/"/ /' <<< $temp)
        temp=$(echo -e "${temp}" | tr -d '[:space:]')
        temp="https:$temp"
        echo $temp
    else
        echo "404"
    fi
}

count=0
for keyword in $(cat words.txt); do
    response=$(py crawler.py $keyword)
    url=$(trim $response)
    if [ $url != "404" ]; then
       echo "keyword is $keyword, url is $url"
       #echo "$line $url" >> result.txt
       curl $url --output "audio/$keyword.mp3"
    fi
    echo "counter is $count"
    ((count++))
done
