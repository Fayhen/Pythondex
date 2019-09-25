# Pythondex #

This is a simple Pokédex API able to retrieve Pokémon data from a database
via GET requests. It was made using Python 3, with the Flask framework and
SQLAlchemy.

## Setup ##

Please ensure that you have Python 3 installed and running correctly before
following the steps below.

### Linux ###

To install required dependencies:

```bash
 # Ensures use of Python 3:
alias python='python3'

# Checks and install pip locally:
python -m ensurepip --user 

# Updates pip to latest version if needed:
python -m pip install -U pip --user

# Either installs/updates the virtualenv package:
python -m pip install -U virtualenv --user 

# Create a virtual environment on new directory named venv:
python -m virtualenv venv

# Activates the venv virtual environment:
. ./venv/bin/activate

# Installs Pythondex dependencies:
pip install -r requirements.txt
```

Always remember to activate your virtual enviroment. Following the steps above,
this will be noticeable by a `(venv)` before the $ or # sign on your terminal.

To run Pythondex in dev mode, run:
```bash
./dev.sh
```


### Windows ###

To install required dependencies:

```batch
# Run this with Python 3. Checks and install pip locally:
python -m ensurepip --user 

# Updates pip to latest version if needed:
python -m pip install -U pip --user

# Either installs/updates the virtualenv package:
python -m pip install -U virtualenv --user 

# Create a virtual environment on new directory named venv:
python -m virtualenv venv

# Activates the venv virtual environment:
.\venv\Scripts\activate.bat

# Installs Pythondex dependencies:
pip install -r requirements.txt
```

Always remember to activate your virtual enviroment. Following the steps above,
this will be noticeable by a `(venv)` before the current working directory.

To run Pythondex in dev mode, run:
```batch
dev.bat
```
