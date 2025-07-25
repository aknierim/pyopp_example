# pyopp_example

Example package for the PYOPP workshop. Not of any real use.

## Installation as Dev

Use `mamba` or `conda` to install the dev environment
```
$ mamba env create --file=environment.yml
```
and activate it:
```
$ mamba activate pyopp
```
Then install the package as an editable install, e.g. using uv:
```
$ uv pip install --group dev -e .
```
