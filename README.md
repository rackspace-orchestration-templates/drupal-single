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
* `username`: Username for Drupal admin login (Default: drupal)
* `domain`: Domain to be used with Drupal site (Default: example.com)
* `image`: Required: Server image used for all servers that are created as a
  part of this deployment. (Default: Ubuntu 12.04 LTS (Precise Pangolin))
* `prefix`: Prefix to use for Drupal database tables (Default: drupal_)
* `version`: Version of Drupal to install (Default: 7.31)
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
* `drupal_password`: Dupal Password
* `server_ip`: Server IP
* `drupal_user`: Drupal User

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.

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
