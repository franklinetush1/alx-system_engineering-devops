# File: apache_php_fix.pp
class apache_php_fix {
    package { 'php5':
        ensure => 'latest',
    }

    service { 'apache2':
        ensure => 'running',
        enable => true,
        require => Package['php5'],
    }
}

include apache_php_fix

