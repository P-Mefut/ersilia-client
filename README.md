# Ersilia Client

Ersilia Client is a Python client to interact with served Ersilia models. It is developed by the Ersilia Open Source Initiative.

## Installation

You can install Ersilia Client directly from the source code:

```bash
git clone https://github.com/ersilia-os/ersilia-client.git
cd ersilia-client
pip install -e .
```


## Usage

```python
from ersilia_client import ErsiliaClient, example_url

ec = ErsiliaClient(url=example_url)
input = ["CCCCOC", "CCCCCN"]
result = ec.run(input)
print(result)
```

## To-do

- [ ] There is an `app.py` file containing a FastAPI implementation. We may want to use it here or move it elsewhere, for example, as part of a new template.
- [ ] The client only works for `Compound` inputs, for now. Accept other input types.
- [ ] Complex outputs are not yet parsed.

## About us

This package is part of the [Ersilia Open Source Initiative](https://ersilia.io). Please see the [Ersilia's main repository](https://github.com/ersilia-os/ersilia) for more information.
