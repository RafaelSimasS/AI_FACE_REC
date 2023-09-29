#!/bin/bash

pip install virtualenv

virtualenv linx_env

source linx_env/bin/activate

pip install -r requirements.txt

deactivate