 # Ensure that the php package is installed first
file { '/var/www/html/wp-settings.php':
  ensure  => 'file',
  source  => 'puppet:///path/to/your/wp-settings.php',
  notify  => Exec['replace'],
}

exec { 'replace':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  refreshonly => true,
}
