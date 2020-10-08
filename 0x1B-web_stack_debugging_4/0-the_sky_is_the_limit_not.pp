# .php
exec { 'setting.php':
  path    =>  ['/bin'],
  command =>  'rm -f abcdef',
  }