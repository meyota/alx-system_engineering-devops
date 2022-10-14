# installs the package puppet-lint
package { 'puppet-lint':
  ensure   => '2.2.2',
  provider => 'gem',
}
