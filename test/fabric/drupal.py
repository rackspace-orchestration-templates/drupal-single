from fabric.api import env, run, task
from envassert import detect, file, group, package, port, process, service, \
    user


@task
def check():
    env.platform_family = detect.detect()
    release = run("/usr/bin/lsb_release -r | awk {'print $2'}")

    assert package.installed("php5")
    assert package.installed("holland")
    assert file.is_dir("/var/www/vhosts")
    assert port.is_listening(80)
    assert process.is_up("apache2")
    assert process.is_up("mysql")
    assert service.is_enabled("apache2")
    assert service.is_enabled("mysql")
