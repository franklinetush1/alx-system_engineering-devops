# Increase the traffic for nginx

exec { 'increase-limit':
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
