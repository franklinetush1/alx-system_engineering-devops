# Changes SSH config file using puppet
exec { 'ssh_config_update':
  path    => 'usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/holberton\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}

