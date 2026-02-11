[![tests](https://github.com/boutetnico/ansible-role-memcached/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-memcached/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.memcached-blue.svg)](https://galaxy.ansible.com/boutetnico/memcached)

ansible-role-memcached
======================

This role installs and configures [Memcached](https://memcached.org/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Debian - 13 (Trixie)](https://wiki.debian.org/DebianTrixie)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                     | Required | Default                    | Choices   | Comments                                 |
|------------------------------|----------|----------------------------|-----------|------------------------------------------|
| memcached_daemon             | true     | `true`                     | boolean   |                                          |
| memcached_logfile            | true     | `/var/log/memcached.log`   | string    |                                          |
| memcached_verbose            | true     | `false`                    | boolean   |                                          |
| memcached_more_verbose       | true     | `false`                    | boolean   |                                          |
| memcached_memory             | true     | `64`                       | integer   |                                          |
| memcached_port               | true     | `11211`                    | integer   |                                          |
| memcached_user               | true     | `memcache`                 | string    |                                          |
| memcached_listen             | true     | `127.0.0.1`                | string    |                                          |
| memcached_pidfile            | false    |                            | string    | OS-specific. See `vars/*.yml`.           |

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

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
