#!/usr/bin/python
# encoding: utf-8

"""
@author: zerlee
@time: 2018/12/5 15:20
@desc:

"""
from IPy import IP

ip_s = input('Please input an IP or net-range: ')

ips = IP(ip_s)

if len(ips) > 1:
    print('net: %s' % ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.broadcast())
    print('reverse address: %s' % ips.reverseName()[0])
    print('subnet: %s' % len(ips))
else:
    print('reverse address: %s' % ips.reverseName()[0])

print('hexadecimal: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())  # 注释
