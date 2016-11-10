# CreditCard-Check

A Python library that checks cardholder's name similarity to user's name. Requires Python 2.7 or 3.x.

## Installation

```
pip install -e git+git://github.com/joaodaher/cc-check.git#egg=cc-check
```

## Similarity

[technique description pending]

### Usage

Depending on the environment

```python
import cc_check as cc

cc.cardholder_check("JOHN A DOE", "JOHN ALBERT DOE")  # returns 0.92


```

## Contributing

Please check the [guidelines for contributing](https://github.com/joaodaher/cc-check/blob/master/CONTRIBUTING.md) to this repository.
