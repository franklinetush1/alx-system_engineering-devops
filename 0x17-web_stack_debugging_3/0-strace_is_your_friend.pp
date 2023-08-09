# Ensure proper wording
package { 'apache2':
  ensure => 'installed',
}
package { 'php':
  ensure => 'installed',
}
exec { 'fixspell':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
