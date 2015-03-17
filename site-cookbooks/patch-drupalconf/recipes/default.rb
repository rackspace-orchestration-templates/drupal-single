include_recipe 'drupal'

# find the apache config template defined in drupal::default
# and use our own template which includes "AllowOverride All"

begin
  t = resources(:template => "#{node['apache']['dir']}/sites-available/drupal.conf")
  t.source "drupal.conf.erb"
  t.cookbook "patch-drupalconf"
  t.variables(:params => { :server_name => node['fqdn'],
                           :server_aliases => node['fqdn'],
                           :docroot => node['drupal']['dir'],
                           :name => 'drupal' })
rescue Chef::Exceptions::ResourceNotFound
  Chef::Log.warn "could not find template #{node['apache']['dir']}/sites-available/drupal.conf to modify"
end
