# Ensure proper wording
package { 'apache2':
  ensure => 'installed',
}

package { 'php':
  ensure => 'installed',
}
