ansible-role-memcached
======================

This role installs and configure Memcached.

[![Build Status](https://travis-ci.org/boutetnico/ansible-role-memcached.svg?branch=master)](https://travis-ci.org/boutetnico/ansible-role-memcached)

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------
- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)


Role Variables
--------------

| Variable                     | Required | Default                         | Choices   | Comments                                      |
|------------------------------|----------|---------------------------------|-----------|-----------------------------------------------|
| memcached_daemon             | true     | `true`                          | boolean   |                                               |
| memcached_logfile            | true     | `/var/log/memcached.log`        | string    |                                               |
| memcached_verbose            | true     | `false`                         | boolean   |                                               |
| memcached_more_verbose       | true     | `false`                         | boolean   |                                               |
| memcached_memory             | true     | `64`                            | integer   |                                               |
| memcached_port               | true     | `11211`                         | integer   |                                               |
| memcached_user               | true     | `memcache`                      | string    |                                               |
| memcached_listen             | true     | `127.0.0.1`                     | string    |                                               |
| memcached_pidfile            | false    |                                 | string    | OS-specific. See `vars/*.yml`                 |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-memcached

Testing
-------

## Debian

`molecule --base-config molecule/shared/base.yml test --scenario-name debian`

## Ubuntu

`molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu`

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
