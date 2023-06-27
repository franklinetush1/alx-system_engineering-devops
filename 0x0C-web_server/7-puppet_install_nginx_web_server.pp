#Install using puppet

package { 'nginx':
  ensure => installed,
}
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  root /var/www/html;
  index index.html index.htm;

  location /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }
}
',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
