#!/bin/bash/python

list=[]
f = open('/var/log/nginx/access.log-20180303')
str1 = f.readlines()
f.close
for i in str1:
	ip = i.split()[0]

	list.append(ip)

list_num = set(list)

for j in list_num:
	num = list.count(j)
print('IP-----COUNT')
print('%s-----%s' %(j,num))
