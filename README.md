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


### Database ###
Pythondex's database must be set up via a Python 3 interpreter. To do so, first install the requirements and activate the virtual environment via the steps provided above. Next, open Python by typing 'python' on your terminal and run the following commands:

```
from server import db

db.create_all()
```

Pythondex comes with aditional utility that allows you to pre-populate data on Pokémon types, generations and habitats. This can be done by running the following commands, **after** you set up the database following the steps above:

```
import server.utils.database_utils as utils

utils.pre_populate()
```

Should you wish to manually add Pokémon types, generations or habitats data, you can still auto-populate the other information separately by running any one of the functions below. **Do not execute any of the functions below more than once, nor together with 'pre_populate()'.**

```
import server.utils.database_utils as utils

utils.pre_populate_types()
utils.pre_populate_gens()
pre_populate_habitats()
```


###### Fetching from PokéAPI ######

Pythondex also has a separate package dedicate to populate Pokémon data through
requests to [PokéAPI](https://pokeapi.co/).

The 'pokeAPI' package can only populate 19 Pokémons per call. This is due to the current limitations on the number of requests per minute to PokéAPI, and its API structure. That is, a few aditional requests per Pokémon are needed in order to fetch all necessary data, including that of all of their abilities.

The 'pokeAPI' package stores request data on a temporary text file, which can be later used to make subsequent requests to PokéAPI, continuing from the last requested Pokémon. This file is created on the './server/temp' directory. Both file and directory are created if non-existant.

Upon running for the first time, the 'pokeAPI' main function should be called without arguments. This will fetch Pokémons from the base url 'https://pokeapi.co/api/v2/pokemon/?limit=19/', which will start from the first Pokémon from the first generation (Bulbasaur). Subsequent calls should pass 'True' as argument to the 'pokeAPI' main function, which will fetch Pokémons continuing from the last one requested. When running, 'pokeAPI' will print requests and parsing info to your terminal.

'pokeAPI' is also aware of the maximum requests number to PokéAPI (100 requests/minute). It will ensure the minimum amount of 60 seconds, as defined on PokéAPI's documentation, has passed between calls.

Should you choose to use Pythondex's 'pokeAPI' package:

- The database has to be set up via the procedures explained above.
- Types, generations and habitats data must already be present on the database.
  - Types, generations and habitats data **must** be pre-populated via the utility functions provided in 'database_utils', as explained above.
  - This is because PokéAPI has its own data structure, and the pokeAPI package will expect data on your local database instance to match that of PokéAPI.
  - Avoid running this function over previously fetched Pokémons, otherwise it will compromise database integrity. It is ideal to only run 'pokeAPI' from the beginning if database data was completely reset.

After taking these precautions, run the following commands on a Python interpreter. Remember to have activated Pythondex's virtual enviroment beforehand:

```
import server.utils.pokeAPI as pokeapi

# If you are running pokeAPI for the first time
pokeapi.pre_populate_pokemons()

# If you are continuing from previous pokeAPI calls and wishes to fetch Pokémons continuing from the last:
pokeapi.pre_populate_pokemons(True)
```


## API documentation ##

Pythondex comes with Swagger UI documentation. It can be accessed by entering 'http://localhost:5000/swagger/' on your Web browser, if running your local Pythondex instance on the default port.
