#!/usr/bin/env python
import manage
from cyder.models import *

# open csv
# old name, new name, ip, ctnr, <rest is ignored>
# find old name in zone specified
# update system name
# update interface name
# update interface domain
# saves

fd = open('rename-hosts.csv','r')

networks_list = []
changed = False

for line in fd.readlines():
    entry = line.strip('\t\r\n ').split(',')
    try:
        the_host = StaticInterface.objects.get(fqdn=entry[0])
    except StaticInterface.DoesNotExist:
        print "{0} does not exist, doing nothing.".format(entry[0])
        continue
    if the_host.system.name != entry[1].split('.',1)[0]:
        print "System: {0} -> {1}".format(the_host.system.name, entry[1].split('.',1)[0])
        the_host.system.name = entry[1].split('.',1)[0]
        the_host.system.save()
    new_label, new_domain = entry[1].split('.',1)
    if the_host.label != new_label:
        changed=True
        print "Updating label."
        the_host.label = new_label
    if the_host.domain != Domain.objects.get(name=new_domain):
        changed=True
        print "Updating domain."
        the_host.domain = Domain.objects.get(name=new_domain)
    if len(entry) > 2:
        print "Updating IP"
        the_host.ip_str = entry[2]
        # might need to change workgroup because of permissions, net changes
        #the_host.workgroup = Workgroup.objects.get(name="Default")
        changed=True
    if len(entry) > 3:
        print "Changing ctnr"
        the_host.system.ctnr=Ctnr.objects.get(name=entry[3])
        the_host.system.save()
        changed=True
    if changed:
        the_host.save()
        changed=False
