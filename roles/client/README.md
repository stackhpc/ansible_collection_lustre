Role Name
=========

Configure Lustre client.

Requirements
------------

Configuration is currently only included for Centos 7.8 (untested) and Centos 8.2. (See `vars/main.yml` to extend this).

Role Variables
--------------

- `lustre_lnet`: Optional. Name of lnet. Default `tcp`. **NB** currently this is the only one supported.
- `lustre_mgs_addr`: Required. IP of MGS.
- `lustre_fs_name`: Required. Name of filesystem.
- `lustre_mount_point`: Optional. Mountpoint on client, will be created if it doesn't exist. Default `/mnt/lustre`.

Dependencies
------------

None, although obviously this is designed to work with the `client` role.

Example Playbook
----------------

See [../../playbooks/clients.yml](../../playbooks/clients.yml)

License
-------

See [../../LICENSE](../../LICENSE).

Author Information
------------------

https://www.stackhpc.com/
