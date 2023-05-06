#!/bin/bash
app_name="primaryschool"
app_name_sh="${app_name/l/1}.sh"
app_name_py="${app_name/l/1}.py"
venv_dir_name="venv"
venv_dir_path="${PWD}/${venv_dir_name}"
py_version="$(python3 --version)"
# global_parameters=$@

src_path="${PWD}/src"
main_src_path="${src_path}/${app_name}"
main_src_ln_path="${PWD}/${app_name}"
locale_path="${main_src_path}/psl10n"
pot_path="${locale_path}/${app_name}.pot"
po_lang0="en_US"
po0_path="${locale_path}/${po_lang0}/LC_MESSAGES/${app_name}.po"
psdep_path="${main_src_path}/psdep"
pypitxt_path="${psdep_path}/pypi.txt"

license0_path="${PWD}/LICENSE"
license0n_paths=( "${main_src_path}/LICENSE" )

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
            python3 -m venv "${venv_dir_path}"
        elif [[ -f $(which virtualenv) ]];
        then
            virtualenv venv
        else
            echo "'virtualenv' is not installed!"
        fi
    fi
    
    if ! [[ -d "${venv_dir_path}" ]];
    then
        return 0
    fi

    if [[ "$SHELL" == *"bash"* ]];
    then
        . "${venv_dir_path}/bin/activate"
        echo_use_venv_y
    else
        . "${venv_dir_path}/bin/activate.fish"
        echo_use_venv_y
    fi
    venv_used=1
    return 1        
}

msg_get(){
    [[ -f $pot_path ]] || touch "${pot_path}"
    
    find "${src_path}" \
        -name "*.py" \
        -exec \
            xgettext \
                -v \
                -j \
                -L Python \
                --output="${pot_path}" \
                {} +

    # xgettext \
    #        -v \
    #        -j \
    #        -L Python \
    #        --output="${pot_path}" \
    #        $(find "${src_path}" -name "*.py")

    [[ -f $po0_path ]] || touch "$po0_path"

    find "${locale_path}/" \
        -name "*.po" \
        -exec \
            msgmerge -U -v {} \; "${pot_path}"
    # for _po in $(find "${locale_path}/" -name "*.po")
    # do
    #     msgmerge -U -v "${_po}" "${pot_path}"
    # done

}

msg_fmt(){
    pos=$(find "${locale_path}" -name "*.po")
    for _po in ${pos}
    do
        echo -e "$_po --> ${_po/.po/.mo}"
        msgfmt -v -o "${_po/.po/.mo}" "${_po}"
    done
}

install_requirements(){
    pypideps=""
    depindex=-1
    breaked_line=""
    while IFS= read -r line; do
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

        if [[ $((depindex%6)) == 0 ]];
        then
            pypideps+=" ${line}"
        fi
        depindex=$((depindex+1))
    done < "${pypitxt_path}"
    pip3 install "${pypideps}"
    depindex=-1
}

get_rqmts(){
    install_requirements
}

get_deps(){
    install_requirements
}

black79(){
    [[ "$(which black)" == *"${venv_dir_path}"* ]] || \
    pip3 install -U black jupyter-black
    [[ "$(which isort)" == *"${venv_dir_path}"* ]] || \
    pip3 install -U isort
    isort .
    black -l79 .
}

blk79(){
    black79
}

code_style(){
    black79
}

cdfmt(){
    code_style
}

psread(){
    [[ $(which python3) == *"${venv_dir_path}"* ]] || use_venv
    [[ "$(which ipython3)" == *"${venv_dir_path}"* ]] || \
    pip3 install -U ipython
    [[ "$(which jupyter-lab)" == *"${venv_dir_path}"* ]] || \
    pip3 install -U jupyterlab
    [[ "$(which pre-commit)" == *"${venv_dir_path}"* ]] || \
    pip3 install -U pre-commit

    if [[ -f $(which cmp) ]];
    then
        for i in "${license0n_paths[@]}";
        do
            cmp -s "${license0_path}" "${i}" || cp "${license0_path}" "${i}"
        done
    fi

    [[ $PYTHONPATH == *"${PWD}/src"* ]] || \
    export PYTHONPATH=${PYTHONPATH}:${PWD}/src
    [[ -d "${main_src_ln_path}" ]] || ln -sr "${main_src_path}" \
    "${main_src_ln_path}"
}

build0(){
    python3 "${app_name_py}" --upptoml
    python3 -m build
}
build(){
    blk79
    python3 "${app_name_py}" --upptoml
    python3 -m build
}


if [[ $# == 0 ]];
then
    psread
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

