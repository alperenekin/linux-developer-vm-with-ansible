import pytest

def test_vscode_command_is_found_(host):
    assert host.run('which code').rc is 0

def test_vscode_version_command_reports_version_1_57_1_(host):
    assert '1.57.1' in host.run('code --version').stdout

@pytest.mark.parametrize('extension', [
    'redhat.ansible',
    'ms-azuretools.vscode-docker',
    'ms-vscode-remote.remote-containers'
])
def test_vscode_extension_is_installed_(host, extension):
    assert extension in host.run('code --list-extensions').stdout
