#!/usr/bin/env bash
export MINICONDA_PATH=/goinfre/miniconda3
if [[ $OSTYPE == 'darwin'* ]]; then
	export TARGET="Miniconda3-py37_4.10.3-MacOSX-x86_64.sh"
else
	export TARGET="Miniconda3-py37_4.10.3-Linux-x86_64.sh"
fi
curl -o /tmp/$TARGET https://repo.anaconda.com/miniconda/$TARGET
bash /tmp/$TARGET -u -b -p $MINICONDA_PATH
grep -qxF 'export PATH=$MINICONDA_PATH:$PATH' ~/.${SHELL##*/}rc || echo 'export PATH=$MINICONDA_PATH:$PATH' >> ~/.${SHELL##*/}rc
builtin type python
python --version
conda install -y "jupyter" "numpy" "pandas"
