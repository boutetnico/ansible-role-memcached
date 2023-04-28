import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "name",
    [
        ("memcached"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("root", "root", "/etc/memcached.conf"),
    ],
)
def test_memcached_config_file(host, username, groupname, path):
    memcached_config = host.file(path)
    assert memcached_config.exists
    assert memcached_config.is_file
    assert memcached_config.user == username
    assert memcached_config.group == groupname
