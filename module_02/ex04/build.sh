#!/usr/bin/env bash
python3 -m pip install --upgrade pip wheel setuptools
python setup.py bdist_wheel
VERSION="$(grep version setup.py | cut -d "'" -f2)"
PACKAGE_NAME="$(grep name setup.py | cut -d "'" -f2)"
PACKAGE_NAME=${PACKAGE_NAME//[-]/_}
tar -czvf dist/${PACKAGE_NAME}-${VERSION}.tar.gz dist/${PACKAGE_NAME}-${VERSION}-py3-none-any.whl
