#!/usr/bin/python3

import sys
import os


resource = open('subdomain.txt', 'r+')
subdomain_list = resource.readlines()
resource.close()

for index in range(len(subdomain_list)):
    subdomain_list[index] = subdomain_list[index].rstrip('\n')

for prefix_subdomain in subdomain_list:
    url = "host -t cname "+ prefix_subdomain+"."+"businesscorp.com.br | grep 'alias for'"

    os.system(url)

    







