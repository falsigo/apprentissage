# apprentissage
Ce référentiel servira de magasin pour les petits morceaux que je rassemblerai tout en apprenant divers outils pour le Machine Learning.

## Prerequisites
Stronghold in Python and programmmming

If you do not have a pip package manager that comes bundled with python and you just hit all the nexts without reading, try reinstalling again.
If you did do it the right way and somehow pip is still unrecognized, try runnin : 
*for UNIX/MacOS
$ python -m pip --version
pip X.Y.Z from .../site-packages/pip (python X.Y)
*Windows
C:\> py -m pip --version
pip X.Y.Z from ...\site-packages\pip (python X.Y)

Go through this link to get a thorough installation from the officials: https://pip.pypa.io/en/stable/installing/
Alternatively for a quicker: 

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 then run the following command
For installing on Windows:
py get-pip.py
For installing on Unix/MacOS
python get-pip.py


##### Required Libraries:
1) Tensorflow  :   pip install tensorflow
If you get an erroneous response saying: “Could not find a version that satisfied the requirement. No matching distribution found for tensorflow.”
You must be runnign an unsupported version of python (3.9). If you are, stop doing it and go aback to python 3.8 which is not unsupported for tensorflow

2) Numpy  :  pip install numpy
