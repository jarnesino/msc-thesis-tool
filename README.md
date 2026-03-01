# Runtime Verification for Real Time DAQs


## Project Setup in Ubuntu


### Base Python installation

1. Python 3.11 (https://www.python.org/)
2. PIP (https://pip.pypa.io/en/stable/installation/)


### IDE setup


#### PyCharm

1. Go to `PyCharm -> Preferences -> Project -> Python Interpreter`
2. Add `WxPhython` and `z3-solver`


#### IntelliJ IDEA Ultimate

1. Go to `File -> Project Structure`
2. Go to `Platform Settings -> SDKs`
3. Select `Add new SDK -> Add Python SDK`
4. Create a **_new_** `Virtualenv Environment`
5. Go to `Platform Settings -> Project`
6. Choose the newly created SDK
7. Select `Apply` and `OK`

*Install all PIP packages inside the Python environment, using IDEA's console.


### Libraries and packages

Run the following terminal commands for each step.
1. Ubuntu package dependencies: `sudo make install-ubuntu-dependencies`
2. Python package dependencies: `install-python-dependencies-for-development` (make sure the terminal is using the Python environment, if you have previously set it up)

**Optional:** To install the prototype's dependencies, run `make install-prototype-python-dependencies`
*This will take some minutes. It should not be done unless you need to work inside the prototype's folder.


## Linting

To run the linter in autocorrect mode, just execute `make lint` in the root folder.
Make sure to run it inside the Python environment, if you use one. 


## Build and install as library

1. Build it by running `make build-package`
2. Install it by running `make install-package`


## Example usage

1. Run the tool's interface with `make run` from the root of the project.
2. Choose one set of example input files from the `example/` directory.
3. Configure the logging as desired and start the verification.


## Simulator framework

- Simulator's description
- Architecture

