pypitxt_path="primaryschool/psdep/pypi.txt"

dindex=-1
pypideps=""
breaked_line=""
while IFS= read -r line; do
    echo $line
    if [[ $line == *'\'* ]];
    then
        breaked_line+="${line::-1}"
        continue
    fi

    if  [[ ${breaked_line} != "" ]];
    then
        line="${breaked_line}${line}"
        breaked_line=""
    fi

    if [[ $((dindex%6)) == 0 ]];
    then
        pypideps+=" $line"
    fi
    dindex=$((dindex+1))
done < $pypitxt_path
dindex=-1
echo $pypideps

