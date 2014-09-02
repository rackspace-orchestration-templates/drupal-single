import re
from fabric.api import env, run, task, hide
from envassert import detect, file, package, port, process, service


def drupal_is_responding():
    with hide('running', 'stdout'):
        homepage = run('curl http://localhost/')
    if re.search('Welcome to Drupal7', homepage):
        return True
    else:
        return False


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("php5")
    assert package.installed("holland")
    assert file.is_dir("/var/www/vhosts")
    assert port.is_listening(80)
    assert process.is_up("apache2")
    assert process.is_up("mysql")
    assert service.is_enabled("apache2")
    assert service.is_enabled("mysql")
    assert drupal_is_responding(), 'Drupal did not respond as expected.'
