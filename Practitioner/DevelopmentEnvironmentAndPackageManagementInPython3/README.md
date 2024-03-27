# Making Python Packages with PIP

## Installing Packages - Requirements Specifiers

```
# Download and install latest release of arrow
pip install arrow

# Request a specific version
pip install "arrow==1.2.3"

# Version comparision (Operators: <, >, >=, <=)
pip install "arrow<1.2"
pip install "arrow>=1.2"

# Combining operators: comma means AND
pip install "Flask>=1.0.0,!=1.1.0,<=2.0.0"

# Compatible release:
# Same major version, minor version equal or greater
pip install "requests ~=2.24.0"

# Equivalent
pip install "requests >=2.24, ==2.*"

# Environment marker
pip install "asyncio; python_version=='3.4'"
pip install "typing; python_version<'3.5'"

pip install "asyncio; os_name=='posix'" # MacOS, Linux, UNIX
pip install "asyncio; os_name='nt'" # Windows
pip install "asyncio; sys_platform='darwin'" # MacOS

# This will not override existing installation
pip install requests

# Force overwrite
pip install --upgrade requests

# Optional extras
pip install "fastapi[all]"
pip install "fastapi[docs,test]"
```

## Installing from Other Sources

```
# Install from Github URL
pip install "MyProject @ git+ssh://source/MyProject"
pip install "MyProject @ git+https://source/MyProject"

# Install from commit, tag or branch
pip install "MyProject @ git+ssh://source/MyProject@master"
pip install "MyProject @ git+ssh://source/MyProject@da39b"
pip install "MyProject @ git+ssh://source/MyProject@v2.1"

# Install a local project or wheel file
pip install path/to/my/prject
pip install myproject-1.1.whl

# Install editable
pip install -e path/to/my/prject
pip install -e .
```

## Install Outside of a Project

```
# Pipx: https://pypa.github.op/pipx/
# Install packages inside their own venv
pip install black

# Make sure PATH is configured correctly
pipx ensurepath

# Alternative: use pip with --user switch
# This does NOT automaically setup a venv
# And you need to do PATH setup yourself
pip install --user black

# Install for entire system (Linux)
# Probably a bad idea
sudo pip install black
```

# Beyond Pip: pipenv and poetry

## Pipenv Commands: Install, Uninstall

```
# Install packages
# This update Pipfile, installs the package in the venv and update the lockfile
pipenv install requests
pipenv install requests~=2.28 # Support version specifiers
pipenv install -d black # Development dependency

# Install all dependencies from the Pipfile
pipenv install

# Remove package from venv, Pipfile and lockfile
# Does not uninstall dependencies
pipenv uninstall
```

## Pipenv Commands: Updating

```
# Install packages from lockfile in your environment
pipenv sync
pipenv sync -d # Install development dependencies

# Update: update packages and dependencies to latest version
pipenv update
pipenv update requests

# Check which packages have security updates
pipenv check
```

## Pipenv Commands Getting Info

```
# Show installed packages
pipenv graph

# Get help
pipenv -h
pipenv install -h
pipenv update -h
```

## Pipenv Commands: Running

```
# Run commands inside venv
pipenv run python my_script.py
pipenv run black my_pkg

# Start a shell with an active venv
# Make sure to end with "exit" instead of "deactivate"
pipenv shell
```

## Poetry Commands: Install, Update

```
# Install dependencies from pyproject.toml and update the lockfile
# This will not remove packages
poetry install

# Make sure environment matches lockfile
# Remove packages if necessary
poetry install --sync

# Update packages, within the version specifiers from pyproject.toml
poetry update
poetry update requests
```

## Poetry Commands: Getting Info

```
# Show installed packages
poetry show
poetry show -tree
poetry show requests

# Get help
poetry help
poetry help install
poetry help update
```

## Poetry Commands: Running

```
# Run commands inside venv
poetry run python my_script.py
poetry run black my_pkg

# Start a shell with an active venv
# Make sure to end with "exit" instead of "deactive"
poetry shell
```
