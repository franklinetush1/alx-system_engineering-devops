  exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
  }

  exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
  }

  file { '/etc/nginx/conf.d/custom_response_header.conf':
    ensure  => present,
    content => "add_header X-Served-By $hostname;",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/conf.d/custom_response_header.conf'],
  }
