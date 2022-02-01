from setuptools import setup

setup(
        name='my-minipack',
        version='1.0.0',
        description='Howto create a package in python.',
        py_module=['loading', 'logger'],
        package_dir={'':'src'},
        author="Antoine Barthelemy",
        author_email="abarthel@student.42.fr",
        python_requires='>=3.7',
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: Students",
            "Topic :: Education",
            "Topic :: HowTo",
            "Topic :: Package",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
        ],
        )
