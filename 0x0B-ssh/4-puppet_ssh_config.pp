# Execute a command
exec { 'ssh_conf':
  command => 'echo "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no\n" >> /etc/ssh/ssh_config',
  path    => ['/bin',],
}