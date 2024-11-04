## Overview

Library for generating random PIN codes satisfying the following criterias:

* Each PIN code in the batch should be unique
* Each PIN should be:
* 4 digits long
* Two consecutive digits should not be the same (e.g. 1156 is invalid)
* Three consecutive digits should not be incremental (e.g. 1236 is invalid)

## Installation

```Shell
pip install --upgrade pip
pip install -i https://test.pypi.org/simple/ pin-generator-1-relduz-chloe
```

## Usage

```Python
from pin_generator_1_relduz_chloe import batch_generate_pin

pins = batch_generate_pin()
```

## Running Tests

```Shell
pip install tox
tox
```
