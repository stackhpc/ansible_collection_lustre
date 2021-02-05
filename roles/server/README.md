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
- `lustre_mgt`: Optional. Path of block device to use for MGT. Default '' does not create MGT/MGS.
- `lustre_mdts`: Optional. Mapping with
    - key: integer index for MDT, unique to filesystem (i.e. spans all MDS)
    - value: path of block device to use for MDT.

  Default `{}` does not create MDT/MDS.

- `lustre_osts`: Optional, as for `lustre_mdts` but for OSTs. Default `{}` does not create OST/OSS.
- `lustre_lnet`: Optional. Name of lnet, must start with `tcp` or `o2ib` (for InfiniBand). Default is `tcp`.

# TODO: document `lnet` role vars too.

Note that setting 

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
