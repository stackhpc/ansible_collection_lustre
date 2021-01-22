loopdev
=========

Define a loop device.

Requirements
------------

Requires `become`.

Role Variables
--------------

- `loopdev_path`: Required. Path to file backing loop device. Created if it doesn't exist.
- `loopdev_size`: Required if `loopdev_path` doesn't exist. Size of backing file specified as for SIZE option of `truncate` command, e.g. "15GB".
- `loopdev_fstype`: Optional. Filesystem type (default: `ext4`)
- `loopdev_mountpoint`: Optional. Define a path to mount loop device. Will be created if it doesn't exist. Default is not to mount it.
- `loopdev_mountstate`: Optional, same as `ansible.posix.mount:state`. Default `mounted`.

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:



    - hosts: server
      become: yes
      tasks:
      - include_role:
          name: loopdev
        vars:
          loopdev_path: "/var/backingfile"
          loopdev_size: "15GB"
      
      roles:
         - ansible-role-template

License
-------

See license.md

Author Information
------------------

https://www.stackhpc.com/
