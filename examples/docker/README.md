# Docker Examples

_Docker examples showing proper use of NOT applying the Cisco Sample Code header._



> **There is NO need to include a Cisco copyright or license notice in your Dockerfile or Docker-Compose files** like you would with your Sample Code files as these contain "build instructions only," not code or other potentially copyrightable material.


## Dockerfile

### Dockerfile Header

```dockerfile
# Dockerfile example.
#
# AUTHOR(s): Zaphod Beeblebrox <zaphodbe@cisco.com>
# CONTRIBUTOR(s): Arthur Dent <arthurde@cisco.com>
#                 Ford Prefect <fordpref@cisco.com>
#                 Slartibartfast <slartiba@cisco.com>
```

The Dockerfile header (comment) should **NOT** contain the Cisco copyright and license notice. It should contain descriptive information and/or documentation for your Dockerfile (see [Dockerfile Format](https://docs.docker.com/engine/reference/builder/#format)). It may also contain attribution (recommended) for the author(s) and contributor(s) who created the Dockerfile.

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

> **You should not add "license" or "copyright" labels to an image.**  We are not supplying a license nor asserting a copyright for the contents of the image. The individual components contained within an image are each subject to and governed by their own individual license terms and copyright notices.

### Build Instructions

```dockerfile
# Your build instructions here.
```

Continue with your Docker image's build instructions.  See [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) for more information.

## Docker Compose File

### Docker Compose Header

```yaml
# Docker-Compose example.
#
# AUTHOR(s): Zaphod Beeblebrox <zaphodbe@cisco.com>
# CONTRIBUTOR(s): Arthur Dent <arthurde@cisco.com>
#                 Ford Prefect <fordpref@cisco.com>
#                 Slartibartfast <slartiba@cisco.com>
```

The Docker Compose header (comment) should **NOT** contain the Cisco copyright and license notice. It should contain descriptive information and/or documentation for your compose file. It may also contain attribution (recommended) for the author(s) and contributor(s) who created the compose file.

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
      com.cisco.author: "Zaphod Beeblebrox <zaphodbe@cisco.com>"
```

Continue with your docker-compose file's service, network, and volume definitions and specifications.  See the [Docker-Compose file reference documentation](https://docs.docker.com/compose/compose-file/) for more information.

> **You should not add "license" or "copyright" labels to a container (service).**  We are not supplying a license nor asserting a copyright for the contents of the container.  The individual components contained within a container are each subject to and governed by their own individual license terms and copyright notices.
