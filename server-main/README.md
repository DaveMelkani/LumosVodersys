# Lumos Server

This repository computes Wall et al.'s [1] metrics as a quantitative measure of analytic focus and establishes a bi-directional communication channel with the Lumos web app, and

## Requirements

- `Python 3.7` - [Link](https://www.python.org/)
- `pip` - [Link](https://pypi.org/project/pip/) - package installer for Python
- `venv` - [Link](https://docs.python.org/3/library/venv.html) - Serves files in virtual environment

## Setup

_Relax, take a deep breath, it won't take much time._
- Open the command line/terminal on your machine and navigate to this project's top-level directory (i.e. where this file is)

### Windows

1. `py -3.7 -m venv venv` - create a python3 virtual environment called _venv_ in the current directory
2. `venv\Scripts\activate.bat` - enters the virtual environment
   - **FROM THIS POINT ON: only use `python` command to invoke interpeter, avoid using global command `py`!!**
3. `python -m pip install -r requirements.txt` - installs required libraries local to this project environment

### MacOS/Linux

1. `python3.7 -m venv venv` / `virtualenv --python=python3.7 venv` - create a python3 virtual environment called venv
2. `source venv/bin/activate` - enters the virtual environment
   - **FROM THIS POINT ON: only use `python` command to invoke interpeter, avoid using global command `python3.7`!!**
3. `python -m pip install -r requirements.txt` - installs required libraries local to this project environment

## Run

1. Navigate to _app_ folder, e.g. `cd app`
2. Execute `python server.py`
3. This server is served at `http://localhost:3000`. Update this in the `app` repository at `app/src/app/models/config.ts` > `DeploymentConfig.SERVER_URL`
...
4. `Ctrl-C` - stops the server
5. `deactivate` - exits the virtual environment

_You did well, get some rest now!_


### References
\[1\] - Wall, Emily, et al. "Warning, bias may occur: A proposed approach to detecting cognitive bias in interactive visual analytics." 2017 IEEE Conference on Visual Analytics Science and Technology (VAST). IEEE, 2017.
