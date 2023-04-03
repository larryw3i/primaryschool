
app_name="primaryschool"
app_name_sh="${app_name}.sh"
app_name_py="${app_name}.py"
venv_dir_name="venv"
venv_dir_path="${PWD}/${venv_dir_name}"
py_version="$(python3 --version)"
global_parameters=$@

locale_path="${app_name}/psl10n"
pot_path="${locale_path}/${app_name}.pot"
po_lang0="en_US"
po0_path="${locale_path}/${po_lang0}/LC_MESSAGES/${app_name}.po"

if ! [[ -v "venv_used" ]];
then
    venv_used=0
fi

echo_use_venv_y(){
    echo "Virtual environment is used."
}

use_venv(){
    if ! [[ -d "${venv_dir_path}" ]];
    then
        if [[ ${py_version} == *"3.11"* ]];
        then
            python3 -m venv ${venv_dir_path}
        elif [[ -f $(which virtualenv) ]];
        then
            virtualenv venv
        else
            echo "`virtualenv` is not installed!"
        fi
    fi
    
    if ! [[ -d "${venv_dir_path}" ]];
    then
        return 0
    fi

    if [[ "$SHELL" == *"bash"* ]];
    then
        . ${venv_dir_path}/bin/activate
        echo_use_venv_y
    else
        . ${venv_dir_path}/bin/activate.fish
        echo_use_venv_y
    fi
    venv_used=1
    return 1        
}

msg_get(){
    [[ -f $pot_path ]] || touch $pot_path

    xgettext \
            -v \
            -j \
            -L Python \
            --output=${pot_path} \
            $(find ${app_name} -name "*.py")

    [[ -f $po0_path ]] || touch $po0_path

    for _po in $(find ${locale_path}/ -name "*.po")
    do
        msgmerge -U -v $_po ${pot_path}
    done
}

msg_fmt(){
    for _po in $(find ${locale_path} -name "*.po")
    do
        echo -e "$_po --> ${_po/.po/.mo}"
        msgfmt -v -o ${_po/.po/.mo} $_po
    done
}

install_requirements(){
    pip3 install $(python3 -m primaryschool.psdep --prn)
}

get_rqmts(){
    install_requirements;
}

black79(){
    [[ -f "$(which black)" ]] || pip3 install -U black
    [[ -f "$(which isort)" ]] || pip3 install -U isort
    isort .
    black -l79 .
}

blk79(){
    black79
}


if [[ $# == 0 ]];
then
    echo "${app_name_sh} is used."
elif [[ $1 == "use_venv" ]];
then
    use_venv
else
    if [[ $venv_used == 0 ]];
    then
        use_venv
    fi

    $@
fi

