# meeg-python

Various helper utilities for `meeg-cfin`-related scripts and notebooks.

# Usage

After Installation (see below) you can, _e.g._,

```python
from meeg import extract_delays
# to plot trigger-to-light-flash delays and correct the associated events
events = extract_delays(fname_raw, return_values='events')
```
# Installation

## Install a fixed version

To permanently install a version into your personal python path, execute this in a terminal:

```bash
cd /path/to/meeg-python
pip install .
```

## Install a development version

Note that the above needs to be executed _every time you download a new version of the code_. Since the code may change a lot, you may want to do this instead:

```bash
cd /path/to/meeg-python
pip install -e .
```

This way, if you update (_e.g._, by pulling changes from github) the `meeg-python` repository, the changes will be available to all of your scripts.
