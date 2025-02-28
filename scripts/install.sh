#!/usr/bin/env bash

# Set defaults
set -o nounset -o errexit -o errtrace -o pipefail

# The directory of this script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Path to the venv directory relative to this script
VENV_DIR="${SCRIPT_DIR}/../venv"

# Path to requirements.txt file relative to this script
REQUIREMENTS_FILE="${SCRIPT_DIR}/../requirements.txt"

# Check venv does not already exist
if [[ -d "${VENV_DIR}" ]]; then
    echo "${VENV_DIR} already exists" 1>&2
    exit 1
fi

# Make venv
python3 -m venv "${VENV_DIR}"

# Activate the venv
source "${VENV_DIR}/bin/activate"

# Deactivate the venv on exit
trap deactivate EXIT

# Install dependencies
pip3 install -r "${REQUIREMENTS_FILE}"

