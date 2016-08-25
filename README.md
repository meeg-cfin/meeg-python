# meeg-python

Various helper utilities for `meeg-cfin`-related scripts and notebooks.

# Usage

After Installation (see below) you can, _e.g._,

```python
from meeg import wavhelpers
```
# Installation 

## The one-off way

You can add the following lines to the beginning of your script/notebook to make the module `meeg` accessible in that script/notebook:

```python
import sys
sys.path.insert(0, '/path/to/meeg-python')
```

## The permanent way(s)

### Install a fixed version

To permanently install a version into your personal python path, execute this in a terminal:

```bash
cd /path/to/meeg-python
python setup.py install --user
```

### Install a development version

Note that the above needs to be executed _every time you download a new version of the code_. Since the code may change a lot, you may want to do this instead:

```bash
cd /path/to/meeg-python
python setup.py develop --user
```

This way, if you update (_e.g._, by pulling changes from github) the `meeg-python` repository, the changes will be available to all of your scripts.
