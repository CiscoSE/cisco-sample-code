# Notes | Dockerfile Template for Cisco Sample Code

## Dockerfile Header
``` Dockerfile
# Dockerfile Template for Cisco Sample Code.
#
# Copyright (c) <current year> Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.0 (the "License"). You may obtain a copy of
# the License at
#
# https://developer.cisco.com/site/licenses/CISCO-SAMPLE-CODE-LICENSE-V1.0
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
```

The Dockerfile header (comment) **must contain the Cisco copyright and license notice** and may also contain descriptive information and/or documentation for your Dockerfile (see [Dockerfile Format](https://docs.docker.com/engine/reference/builder/#format)).


## From
``` Dockerfile
FROM <image>:<tag>
```

A Dockerfile must start with a `FROM` instruction.


## Dockerfile Metadata
``` Dockerfile
LABEL author="Zaphod Beeblebrox <zaphodbe@cisco.com>" \
      contributors.1="Arthur Dent <arthurde@cisco.com>" \
      contributors.2="Ford Prefect <fordpref@cisco.com>" \
      contributors.3="Slartibartfast <slartiba@cisco.com>" \
      license="Cisco Sample Code License, Version 1.0" \
      copyright="Copyright (c) <current year> Cisco and/or its affiliates."
```

"The LABEL instruction adds metadata to an image. A LABEL is a key-value pair. To include spaces within a LABEL value, use quotes and backslashes as you would in command-line parsing. An image can have more than one label. To specify multiple labels, Docker recommends combining labels into a single LABEL instruction where possible. Each LABEL instruction produces a new layer which can result in an inefficient image if you use many labels. This example results in a single image layer" (see [Dockerfile Label](https://docs.docker.com/engine/reference/builder/#label)).

## Your Build Instructions
``` Dockerfile
# Your build instructions here.
```

Continue with your Docker image's build instructions.  See [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) for more information.
