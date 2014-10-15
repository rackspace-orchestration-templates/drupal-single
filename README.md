Description
===========

This is a Heat template to deploy a single Linux server running Drupal.


Requirements
============
* A Heat provider that supports the following:
  * OS::Nova::KeyPair
  * Rackspace::Cloud::Server
  * OS::Heat::RandomString
  * OS::Heat::ChefSolo
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `server_hostname`: Hostname to use for the server that's built. (Default:
  Drupal)
* `username`: Username for the Drupal admin login (Default: admin)
* `domain`: Domain to be used with the Drupal site (Default: example.com)
* `image`: Required: Server image used for all servers that are created as a
  part of this deployment. (Default: Ubuntu 12.04 LTS (Precise Pangolin))
* `version`: Version of Drupal to install (Default: 7.32)
* `database_name`: Drupal database name (Default: drupal)
* `flavor`: Required: Rackspace Cloud Server flavor to use. The size is based
  on the amount of RAM for the provisioned server. (Default: 4 GB Performance)
* `chef_version`: Version of chef client to use (Default: 11.14.2)
* `kitchen`: URL for a git repo containing required cookbooks (Default:
  https://github.com/rackspace-orchestration-templates/drupal-single.git)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value of a specific output.

* `mysql_root_password`: MySQL Root Password
* `private_key`: SSH Private Key
* `drupal_password`: Drupal Password
* `server_ip`: Server IP
* `drupal_url`: Drupal URL
* `drupal_user`: Drupal User

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.

Stack Details
=============
#### Getting Started
If you're new to Drupal, check out [Getting started with Drupal 7
administration](https://drupal.org/getting-started/7/admin). The getting
started document will help guide you through the initial steps of checking
your site's status, customizing your site's informaion, adding users, and
more!

#### Logging in via SSH
The private key provided in the passwords section can be used to login as
root via SSH.  We have an article on how to use these keys with [Mac OS X and
Linux](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-linuxmac)
as well as [Windows using
PuTTY](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-windows).

#### Details of Your Setup
This deployment was stood up using
[chef-solo](http://docs.opscode.com/chef_solo.html). Once the deployment is
up, chef will not run again, so it is safe to modify configurations.

A system user called 'drupal' has been created as a part of this deployment.
There is no password associated with this account. You will need to set a
password for this user if you'd like to use the account for transferring
content, backups, or other purposes. Since the account has no password, no
one will be able to login as this user until a password is set.

Drupal was installed using [Drush](http://drush.ws/about). Drupal is
installed into /var/www/drupal and served by
[Apache](http://httpd.apache.org/). The Apache configuration is in
/etc/apache2/sites-enabled/drupal.conf. Any changes to the configuration
would require a restart of Apache.

[MySQL](http://www.mysql.com/) is the database backend used in this
deployment. The MySQL root password is included in the password section of
this deployment. If you do lose the password, it is also available in
/root/.my.cnf. MySQL backups are performed locally by
[Holland](http://wiki.hollandbackup.org/). The backups will be stored in
/var/lib/mysqlbackup.

#### Updating Drupal
Drupal does provide community documentation on [how to
upgrade](https://drupal.org/upgrade) your installation of Drupal. There are
several steps involved with the upgrade process. First, make sure to backup
your site files and your database prior to taking any steps to replace the
core site files. There are number of other tutorials available on places like
YouTube that can also step you though the upgrade/update process. There is
not currently a way to perform these upgrades automatically through the admin
interface.

#### Migrating an Existing Site
Moving a Drupal site can be both difficult and time consuming. Drupal Modules
such as the [Backup and Migrate
module](http://drupal.org/project/backup_migrate) can help you move your
database content. We recommend backing everything up on both the source and
destination locations before anything is done. The content you want to move
over will be in the 'sites' directory. If you're running a single Drupal
site, you may just need the content of 'sites/default/files' along with your
database. Be careful not to overwrite the settings.php file within your site.
It contains the database configuration for your site.

This deployment has all of the core drupal files in place, and their
permissions are properly set. Be careful with ownerhip and permissions as you
move things over. If you're unsure, check the original ownership and
permissions of the files in this deployment.

#### Additional Modules
There are over 22,000 modules that have been created by an enaged developer
community. The [modules](https://drupal.org/project/Modules) section on
Drupal's website provides an easy way to search for and research modules.

#### Scaling out
This single server deployment is not well suited to be scaled out. We
recommend leveraging a multi server option. If content needs to be moved,
instructions above regarding migrating an existing site may help with that
transition.

Contributing
============
There are substantial changes still happening within the [OpenStack
Heat](https://wiki.openstack.org/wiki/Heat) project. Template contribution
guidelines will be drafted in the near future.

License
=======
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
