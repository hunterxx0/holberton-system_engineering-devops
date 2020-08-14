#!/usr/bin/env bash
# configure web-02 to be identical to web-01.
exec {'http header':
command  => 'sudo apt-get update -y; sudo apt-get install nginx -y; sudo sed -i "15i \\\n\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf; service nginx restart',
provider => shell,
}
