Role Name
=========

Configure lustre server components: MGS, MDS and OSS. **NB: This will change the running kernel, if necessary.**

Requirements
------------

Configuration is currently only included for Centos 7.8. (See `vars/main.yml` to extend this).

Role Variables
--------------

- `lustre_reformat`: Optional, default `false`. Set `true` to reformat all mgt/mdt/ost, e.g. if needed to change configuration  **WARNING: THIS WILL DELETE ALL DATA **.
- `lustre_fs_name`: Required. Name of filesystem.
- `lustre_mgs_addr`: Required. IP of MGS.
- `lustre_mgt`: Optional. Path of block device to use for mgt. Default '' does not create mgt (and hence mgs).
- `lustre_mdts`: Optional. Mapping with
    - key: integer index for MDT, unique to filesystem (i.e. spans all MDS)
    - value: path of block device to use for MDT.

  Default `{}` does not create MDT (and hence MDS).

- `lustre_osts`: Optional, as for `lustre_mdts` but for OSTs. Default `{}` does not create OST (and hence OSS).
- `lustre_lnet`: Optional. Name of lnet. Default `tcp`. **NB** currently this is the only one supported.

Dependencies
------------

None, although obviously this is designed to work with the `client` role.

Example Playbook
----------------

See [../../playbooks/servers.yml](../../playbooks/servers.yml)

License
-------

See [../../LICENSE](../../LICENSE).

Author Information
------------------

https://www.stackhpc.com/
