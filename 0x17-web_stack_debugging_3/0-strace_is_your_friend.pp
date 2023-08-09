 # Ensure that the php package is installed first
file { '/var/www/html/wp-settings.php':
  ensure  => 'present',
  content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'),
  require => Package['php'],
}
