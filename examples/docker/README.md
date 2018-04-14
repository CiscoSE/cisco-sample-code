# Docker Examples

_Docker examples showing proper use of the Cisco Sample Code header._

## Dockerfile

### Dockerfile Header

```dockerfile
# Dockerfile example showing proper use of the Cisco Sample Code header.
#
# Copyright (c) {{current_year}} Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.0 (the "License"). You may obtain a copy of the
# License at
#
#                https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
#
# AUTHOR(s): Zaphod Beeblebrox (zaphodbe@cisco.com)
# CONTRIBUTOR(s): Arthur Dent (arthurde@cisco.com)
#                 Ford Prefect (fordpref@cisco.com)
#                 Slartibartfast (slartiba@cisco.com)
```

The Dockerfile header (comment) **must contain the Cisco copyright and license notice** and may also contain descriptive information and/or documentation for your Dockerfile (see [Dockerfile Format](https://docs.docker.com/engine/reference/builder/#format)).

It may also contain attribution (recommended) for the author(s) and contributor(s) who created the Dockerfile.

### From

```dockerfile
FROM {{image}}:{{tag}}
```

A Dockerfile must start with a `FROM` instruction.

### Image Metadata

```dockerfile
LABEL com.cisco.author="Zaphod Beeblebrox <zaphodbe@cisco.com>"
```

"The LABEL instruction adds metadata to an image. A LABEL is a key-value pair. To include spaces within a LABEL value, use quotes and backslashes as you would in command-line parsing. An image can have more than one label. You can specify multiple labels on a single line. Prior to Docker 1.10, this decreased the size of the final image, but this is no longer the case. You may still choose to specify multiple labels in a single instruction." (see [Dockerfile Label](https://docs.docker.com/engine/reference/builder/#label)).

> **You should not add "license" or "copyright" labels to an image.**  We are not supplying a license nor asserting a copyright for the contents of the image.  The license and copyright notice included in the header of this Dockerfile applies to the "build instructions" contained herein. The individual components contained within an image are each subject to and governed by their own individual license terms and copyright notices.

### Build Instructions

```dockerfile
# Your build instructions here.
```

Continue with your Docker image's build instructions.  See [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) for more information.

## Docker Compose File

### Docker Compose Header

```yaml
# Docker-Compose example showing proper use of the Cisco Sample Code header.
#
# Copyright (c) {{current_year}} Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.0 (the "License"). You may obtain a copy of the
# License at
#
#                https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
#
# AUTHOR(s): Zaphod Beeblebrox (zaphodbe@cisco.com)
# CONTRIBUTOR(s): Arthur Dent (arthurde@cisco.com)
#                 Ford Prefect (fordpref@cisco.com)
#                 Slartibartfast (slartiba@cisco.com)
```

The docker-compose header (comment) **must contain the Cisco copyright and license notice** and may also contain descriptive information and/or documentation for your docker-compose file.

It may also contain attribution (recommended) for the author(s) and contributor(s) who created the Dockerfile.

### version

```yaml
version: '3'
```

A docker-compose file should have a `version` entry at the root of the YAML document; if not specified, docker-compose defaults to the legacy `version: '1'` specification.

## Service, Network and Volume Definitions

```yaml
# Your service, network, and volume deffinitions
services:
  app:
    build:
      context: .
    labels:
      com.cisco.author: "Zaphod Beeblebrox (zaphodbe@cisco.com)"
```

Continue with your docker-compose file's service, network, and volume definitions and specifications.  See the [Docker-Compose file reference documentation](https://docs.docker.com/compose/compose-file/) for more information.

> **You should not add "license" or "copyright" labels to a container (service).**  We are not supplying a license nor asserting a copyright for the contents of the container.  The license and copyright notice included in the header of this docker-compose file applies to the service definitions and specifications contained herein. The individual components contained within a container are each subject to and governed by their own individual license terms and copyright notices.
