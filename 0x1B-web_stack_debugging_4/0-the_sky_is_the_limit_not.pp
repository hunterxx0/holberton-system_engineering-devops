# .php
exec { 'setting.php':
  path    =>  ['/bin'],
  command =>  'sudo sed -i -e "$aULIMIT=\"-n 4096\"" /etc/default/nginx ; sudo service nginx restart',
  }