# Ensure proper wording
package { 'apache2':
  ensure => 'installed',
}

package { 'php':
  ensure => 'installed',
}

file { '/etc/php/5.6/apache2/php.ini':
  ensure => 'file',
  content => template('your_module/php.ini.erb'),
  require => Package['php'],
  notify => Service['apache2'],
}
