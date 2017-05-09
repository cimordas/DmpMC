#!/bin/bash

check(){
    ndone=$(grep -o "lfn" ${task}.json | wc -w)
    ntotal=$(wc -l ${task}.txt | awk '{print $1}')
    echo "${task}: ${ndone}/${ntotal}"
}

wd=$(pwd)
td=${1} # task dir

cd ${td}
for f in $(ls | grep "json" | awk -F ".json" '{print $1}'); 
do 
    export task=${f}
    check
done



