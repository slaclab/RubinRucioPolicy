# RubinRucioPolicy
This is the Rucio policy package for Rubin.

## How to use this policy package
* Mount the policy package files into /opt/permissions/rubin
* `/opt/permissions/rubin` should be on the `PYTHONPATH` for the container
* Set `package = rubin` in the `policy` section of the Rucio configuration file.

## Source files
* `__init__.py` - registers the SURL and LFN2PFN algorithms when the package is loaded.
* `permission.py` - permission functions for the policy package.
* `schema.py` - schema functions and data for the policy package. Currently just a copy of the generic code with no Rubin-specific customisation.

## More Information
* https://rucio.cern.ch/documentation/operator/policy_packages
