# ansible-galaxy-test

An Ansible role to install Test.

## Role Variables

- `test_version` - Nginx version (default: `stable`, valid options are: `stable` or `development`)
- `test_delete_default_site` - Whether or not to delete the default Test site (default: `False`)

## Example Playbook

See the [examples](./examples/) directory.
