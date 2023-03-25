
app_name="primaryschool"
app_name_sh="${app_name}.sh"
app_name_py="${app_name}.py"
venv_dir_name="venv"
venv_dir_path="${PWD}/${venv_dir_name}"
py_version="$(python3 --version)"
global_parameters=$@

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
    return 1        
}

if [[ $# == 0 ]];
then
    echo "${app_name_sh} is used."
elif [[ $1 == "use_venv" ]];
then
    use_venv
else
    use_venv
    if ! [[ $? == 1 ]];
    then 
        return
    fi
    $@
fi

