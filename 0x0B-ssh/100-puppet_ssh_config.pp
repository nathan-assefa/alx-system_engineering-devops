#configuration managment using puppy

file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  content => '
SendEnv LANG LC_*
HashKnownHosts yes
GSSAPIAuthentication yes
IdentityFile ~/.ssh/school
PasswordAuthentication no ' }
