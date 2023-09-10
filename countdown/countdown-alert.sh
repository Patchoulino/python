#!/bin/bash

while getopts "m:f:b:" opt; do
    case ${opt} in
        m)
            MAIL=${OPTARG}
            ;;
        f)
            FILE=${OPTARG}
            ;;
        b)
            BODY=${OPTARG}
            ;;
        \?)
            echo "Invalid option: -${OPTARG}" >&2
            exit 1
            ;;
        :)
            echo "Option -${OPTARG} requires an argument." >&2
            exit 1
            ;;
    esac
done

if [[ -z $MAIL || -z $FILE ]]; then
    echo "Usage: $0 -f file -m email.example.com [-b \"body_message\"]"
    echo "  -f <countdown_file>"
    echo "  -m <mail>"
    echo "  -b \"body message\""
    exit 1
fi

grep "$(date +%m-%d)" $FILE > /dev/null 2>&1
if [ $? == 0 ]; then
    SUBJECT=$(grep "$(date +%m-%d)" $FILE | awk -F \| '{print $2}')
    if [ -z "$BODY" ]; then
        BODY=$SUBJECT
    fi
    echo "subject: $SUBJECT"
    echo "body: $BODY"
    echo "mail: $MAIL"
    echo -e "Subject: $SUBJECT\n\n$BODY\n" | sendmail $MAIL #> /dev/null
fi