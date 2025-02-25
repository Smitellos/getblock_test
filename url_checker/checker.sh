#! /bin/bash

# get location
inputFile=$1

urlArray=( $(cat $inputFile) )

# function
check_url () {

    local myVar="$1"

    # iterate trough list
    for value in "$@"; do
        # get response code
        local status=$(curl -s -o /dev/null -w "%{http_code}" http://$value)
        echo $status" :status of " $value
        fc=`echo $status | cut -c1-1`

        # check rsp code not 5XX or 4XX
        if [[ "$fc" =~ ^(5|4) ]]; then
            echo "fail"
            return 1
        fi
    done

    return 0

    # stop if url is unreachable
}

check_url "${urlArray[@]}"