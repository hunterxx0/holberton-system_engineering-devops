# .php
exec { 'setting.php':
  path    =>  ['/bin'],
  command =>  'sudo echo "ULIMIT=\"-n 4096\"" >> /etc/default/nginx ; sudo service nginx restart',
  }