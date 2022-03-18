import pytest

def test_cowsay_is_installed(host):
    assert host.package('cowsay').is_installed

def test_cowsay_command_is_found(host):
    cmd = host.run("/user/games/cowsay hello")
    assert cmd.rc is 0