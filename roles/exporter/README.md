Role Name
=========

Install a Prometheus exporter for [Lustre metrics](https://github.com/HewlettPackard/lustre_exporter), creating a systemd service `lustre_exporter`. Metrics are available on `http://localhost:9169/metrics`.

Some grafana dashboards for this exporter are listed [here](https://github.com/HewlettPackard/lustre_exporter/issues/45#issuecomment-454393303).

TODO: add configuration of port and TLS.

Requirements
------------

The ansible control host host requires `make` installed. Run with `facts: true`.

Role Variables
--------------

Generally the only variable needing setting is:

- `lustre_exporter_flags`: Optional. Mapping defining which collectors to enable. The default is:

      lustre_exporter_flags:
        ost: extended
        mdt: extended
        mgs: extended
        mds: extended
        client: extended
        generic: extended
        lnet: extended
        health: extended

  where values may be one of the following as per [docs](https://github.com/HewlettPackard/lustre_exporter#flags):
    - `disabled`: Completely disable all metrics for this portion of a source.
    - `core`: Enable this source, but only for metrics considered to be particularly useful.
    - `extended`: Enable this source and include all metrics that the Lustre Exporter is aware of within it.

  Generally this will need to be set per host/group. Note that while overriding the default mapping clears all flags, an un-set flag is equivalent to `extended`. So for example for a MGS/MDS/OSS 
  node where extended metrics are required for all relevant collectors it is sufficent to set the following in `host_vars`:
  
      lustre_exporter_flags:
        client: disabled

For the following role variables the default values are likely to be appropriate:
- `lustre_exporter_builddir`: Optional. Directory to use (e.g. on deployment host) for exporter build. Default `/tmp/lustre_exporter_build`.
- `lustre_exporter_installdir`: Optional. Directory on lustre node to install exported. Default `/usr/local/bin`.
- `lustre_exporter_group`: Optional. Group for lustre exporter. Default `lustre-exp`.
- `lustre_exporter_user`: Optional. User for lustre exporter. Default `{{ lustre_exporter_group }}`.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

The role provides two playbooks:

  - `build`: Build the exporter. Generally should be run on the ansible control host. Requires facts, does not require become.

        - hosts: localhost
          gather_facts: true
          become: false
          tasks:
            - include_role:
                name: exporter
                tasks_from: build

  - `install`: Install the exporter onto lustre nodes (servers, clients, routers). Requires become. E.g.:

        - hosts: servers
          become: true
          tasks:
          - include_role:
                name: exporter
                tasks_from: install
            vars:
              lustre_exporter_flags:
                client: disabled      

License
-------

See [../../LICENSE](../../LICENSE).

Author Information
------------------

https://www.stackhpc.com/
