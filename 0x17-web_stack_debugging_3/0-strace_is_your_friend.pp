# Ensure proper wording
package { 'apache2':
  ensure => 'installed',
}
package { 'php':
  ensure => 'installed',
}
service { 'apache2':
  ensure => 'running',
  enable => true,
  require => Package['apache2', 'php'],
}
