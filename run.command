#!/usr/bin/env bash

# Set defaults
set -o nounset -o errexit -o errtrace -o pipefail

# The directory of this script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Directory of the virtual environment relative to the script
VENV_DIR="${SCRIPT_DIR}/venv"

# Check venv is set up
if [[ ! -d "${VENV_DIR}" ]]; then
    echo "Please ensure ${VENV_DIR} is set up" 1>&2
    exit 1
fi

# Run from script directory
cd "${SCRIPT_DIR}"

# Activate the venv
source "${VENV_DIR}/bin/activate"

# Run the script
python "${SCRIPT_DIR}/main.py"

# Deactivate the venv
deactivate

