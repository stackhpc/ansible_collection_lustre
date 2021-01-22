
Molecule tests using the OpenStack driver.

Note this role can't be tested using Docker as it requires specific/changing kernels.

# Installation

First `git clone` this repo to somewhere ansible expects to find collections, using the right namespace, e.g. `~/.ansible/collections/ansible_collections/stackhpc/lustre`.

Install `molecule` and the `openstack` driver:

```shell
sudo yum install -y gcc python3-pip python3-devel openssl-devel python3-libselinux
cd <collection>
python3 -m venv venv-mol
. venv-mol/bin/activate
pip install -U pip
pip install -r molecule/requirements.txt
```

Install the roles this collection depends on, into `<repo_root>/roles`:
TODO: needs the


# Configuration

Download an openstack `*rc.sh` file and source it.

Find generic CentOS images, flavors and an external network:

```shell
alaska openstack image list | grep -i centos
alaska openstack flavor list
alaska openstack network list
```

Using the above, copy `molecule/alaska-config.yml` and create a config file for your specific cloud. Now source that.

**NB: At present only testing of CentOS 8.2 images is configured** TODO: FIXME:

# Tests

The following tests are defined:
- `default`: Checks role defaults work. It creates:
    - A combined MGS/MDS/OSS Lustre server. The MGT/MDT/OST are created on loop devices backed by files created in the directory specified by `OPENSTACK_SERVER_DISK_DIR`. This must have 1.5GB of space available.
  It checks that: TODO:

Run tests using:

```shell
molecule --env-file molecule/alaska-config.yml test
```

or whatever your cloud config file is.