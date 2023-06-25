# Changes SSH config file using puppet
exec { 'ssh_config_update':
  path        => ['/usr/bin', '/bin'],
  command     => 'echo -e "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  refreshonly => true,
  notify      => Service['ssh'],
}

