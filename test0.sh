pypitxt_path="primaryschool/psdep/pypi.txt"

dindex=-1
pypideps=""
while IFS= read -r line; do
    if [[ $((dindex%6)) == 0 ]];
    then
        pypideps+=" $line"
    fi
    dindex=$((dindex+1))
done < $pypitxt_path
echo $pypideps

