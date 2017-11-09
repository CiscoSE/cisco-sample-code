# Notes | Python Template for Cisco Sample Code

## Shebang Line
``` python
#!/usr/bin/env python
```

A "shebang" (`#!`) line, if used (executable Python file), should be the first line in the Python script and should reference the interpreter that will be used to execute the script.  This can also be a good way to indicate what Python version a file has been written to support.
  * `python` - Python v2 or v3
  * `python2` - Python v2
  * `python3` - Python v3

## Source File Encoding
``` python
# -*- coding: utf-8 -*-
```

The source file encoding declaration (if present), "must be placed into the source files either as first or second line in the file" ([PEP263](https://www.python.org/dev/peps/pep-0263/#defining-the-encoding)).

"Files using ASCII (in Python 2) or UTF-8 (in Python 3) should not have an encoding declaration" ([PEP8](https://www.python.org/dev/peps/pep-0008/#source-file-encoding)).


## Module | Script Docstring
``` python
"""Python Template for Cisco Sample Code.

Copyright (c) <current year> Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of
the License at

https://developer.cisco.com/site/licenses/CISCO-SAMPLE-CODE-LICENSE-V1.0

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied.

"""
```

The module or script docstring **must contain the Cisco copyright and license notice** and may also contain a useage message and/or other module-level documentation for your file (see [PEP257](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings)).


## Module | Script Metadata (aka. "Dunders")
``` python
# from __future__ import absolute_import, division, print_function

__author__ = "Zaphod Beeblebrox <zaphodbe@cisco.com>"
__contributors__ = [
    "Arthur Dent <arthurde@cisco.com>",
    "Ford Prefect <fordpref@cisco.com>",
    "Slartibartfast <slartiba@cisco.com>",
]
__copyright__ = "Copyright (c) <current year> Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"
```

"Module level "dunders" (i.e. names with two leading and two trailing underscores) such as `__all__`, `__author__`, `__version__`, etc. should be placed after the module docstring but before any import statements except from `__future__` imports. Python mandates that future-imports must appear in the module before any other code except docstrings" ([PEP8](https://www.python.org/dev/peps/pep-0008/#module-level-dunder-names)).

## Your Code
``` python
# Your code goes here.
```

Continue with your module or script's code.  See [PEP8](https://www.python.org/dev/peps/pep-0008/) for Style Guide recommendations.
