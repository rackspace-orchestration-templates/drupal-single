from fabric.api import env, task
from envassert import detect, package, port, process, service
from hot.utils.test import get_artifacts, http_check


@task
def check():
    env.platform_family = detect.detect()

    site = "http://localhost/"
    string = "Welcome to Drupal"
    apache_process = 'apache2'
    php_package = 'php5'
    mysql_process = 'mysql'

    assert port.is_listening(80), 'Port 80 is not listening.'
    assert package.installed(php_package), 'PHP is not installed.'
    assert process.is_up(apache_process), 'Apache is not running.'
    assert process.is_up(mysql_process), 'MySQL is not running.'
    assert service.is_enabled(apache_process), 'Apache is disabled at boot.'
    assert service.is_enabled(mysql_process), 'MySQL is disabled at boot.'
    assert http_check(site, string), 'Drupal is not responding as expected.'


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
