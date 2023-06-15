# puppet script to enhance the number of file discriptors for nginx service

exec {'change_userlimit':
  command => '/usr/bin/env sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
}
-> exec {'/usr/bin/env service nginx restart':}
