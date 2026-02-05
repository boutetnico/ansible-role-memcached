import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("memcached"),
    ],
)
def test_memcached_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_memcached_service_is_running(host):
    service = host.service("memcached")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize(
    "path,user,group,mode",
    [
        ("/etc/memcached.conf", "root", "root", 0o644),
    ],
)
def test_memcached_config_file_exists(host, path, user, group, mode):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == user
    assert config.group == group
    assert config.mode == mode


def test_memcached_is_listening(host):
    socket = host.socket("tcp://127.0.0.1:11211")
    assert socket.is_listening
