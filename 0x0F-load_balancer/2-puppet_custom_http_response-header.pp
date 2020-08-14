#!/usr/bin/env bash
# configure web-02 to be identical to web-01.

sudo apt-get update -y
sudo apt-get install haproxy -y
sudo -i "s|ENABLED=0|ENABLED=1|" /etc/default/haproxy
sudo sed -i '1i \listen holberton\n\tbind *:80\n\tmode http\n\tbalance roundrobin\n\tserver 1080-web-01 35.231.7.140:80 check\n\tserver 1080-web-02 35.227.72.212:80 check\n' /etc/haproxy/haproxy.cfg
service haproxy restart
