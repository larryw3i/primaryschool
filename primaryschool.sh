
venv_dir="${PWD}/venv"
py_version="$(python --version)"
global_parameters=$@

use_venv(){
    if ! [[ -d ${venv_dir} ]];
    then
        if [[ ${py_version}==*"3.11"* ]];
        then
            python3 venv ${venv_dir}
        fi

        
    fi
}

