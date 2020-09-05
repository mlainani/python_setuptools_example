# A working example of a Python33 module with an executable script created using setuptools

python3 -m venv venv

source venv/bin/activate

pip3 install --upgrade setuptools wheel

python3 setup.py bdist_wheel

python3 setup.py develop

python3 setup.py develop --uninstall

deactivate

