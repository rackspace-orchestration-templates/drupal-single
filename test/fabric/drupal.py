import re
from fabric.api import env, run, task, hide
from envassert import detect, file, package, port, process, service
from hot.utils.test import get_artifacts


def drupal_is_responding():
    with hide('running', 'stdout'):
        site = "http://localhost/"
        homepage = run("wget --quiet --output-document - %s" % site)
    if re.search('Welcome to Drupal7', homepage):
        return True
    else:
        return False


@task
def check():
    env.platform_family = detect.detect()

    assert file.is_dir("/var/www/vhosts")
    assert port.is_listening(80)
    assert package.installed("holland")
    assert drupal_is_responding(), 'Drupal did not respond as expected.'

    apache_process = 'apache2'
    php_package = 'php5'
    mysql_process = 'mysql'

    if env.platform_family == 'debian':
        apache_process = 'apache2'
        php_package = 'php5'
        mysql_process = 'mysql'
    elif env.platform_family == 'rhel':
        apache_process = 'httpd'
        php_package = 'php'
        mysql_process = 'mysqld'
    else:
        raise ValueError('OS ' + env.platform_family +
                         ' unknown, update tests.')

    assert package.installed(php_package)
    assert process.is_up(apache_process)
    assert process.is_up(mysql_process)
    assert service.is_enabled(apache_process)
    assert service.is_enabled(mysql_process)


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
