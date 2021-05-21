# Client configuration with Puppet

file_line { 'Private key configuration ~/.ssh/holberton':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '	IdentityFile ~/.ssh/holberton'
}

file_line { 'Refuse auth with password':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '	PasswordAuthentication no',
}
