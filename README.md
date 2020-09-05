# A working example of a Python3 module with an executable script created using setuptools

python -m venv venv

source venv/bin/activate

python setup.py bdist_wheel

python setup.py develop

python setup.py develop --uninstall

deactivate
