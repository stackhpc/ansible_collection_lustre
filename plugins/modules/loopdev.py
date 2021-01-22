#!/usr/bin/python

# Copyright: (c) 2020, StackHPC
# Apache 2 License

from ansible.module_utils.basic import AnsibleModule
import os

ANSIBLE_METADATA = {
    "metadata_version": "0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: loopdev
short_description: Set up loop device
description:
    - "Set up the first unused loop device using a specified backing file"
options:
    path:
        description:
            - Path to file to use to back loop device.
        required: true
        type: str
    fstype:
        description:
            - Filesystem type
        type: str
        required: false
        default: ext4
returns:
    dev:
        description: Name of loop device e.g. /dev/loop0
        type: str
requirements:
    - "python >= 3.6"
author:
    - Steve Brasier, StackHPC
"""

EXAMPLES = """
- name: Ensure loop device exists
  loopdev:
    path: "/path/to/file"
"""

def run_module():
    module_args = dict(
        path=dict(type="str", required=True),
        fstype=dict(type="str", required=False, default='ext4'),
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    
    path = module.params["path"]
    fstype = module.params["fstype"]
    result = {"changed": False, "path": path, "fstype": fstype}
    
    if module.check_mode:
        module.exit_json(**result)

    # Check for existing loop device on `path` and create new if necessary:
    _, check_lo, _ = module.run_command("losetup -j %s" % path, check_rc=True)
    loop_dev = check_lo.strip()
    if loop_dev == '':
        _, create_los, _ = module.run_command("losetup -f --show %s" % path)
        loop_dev = create_los.strip()
        result['changed'] = True
    else: # is something like "/dev/loop0: []: (/var/mgt)"
        loop_dev = loop_dev.split(':')[0]
    result['dev'] = loop_dev
    
    # Check for filesystem:
    _, lsblk, _ = module.run_command("lsblk -f %s" % loop_dev)
    fsinfo = lsblk.split('\n')[1].split() # e.g. either ['loop0'] or ['loop0', 'ext4', <label>, <uuid>]
    if fstype not in fsinfo:
        # Make filesystem:
        _, mkfs, _ = module.run_command("mkfs -t %s %s" % (fstype, loop_dev))
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()