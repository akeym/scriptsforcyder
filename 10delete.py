#!/usr/bin/env python
import struct
import socket
import activate
activate.activate()
from cyder.models import *

ip_start = struct.unpack("!L", socket.inet_aton('10.0.0.0'))[0]
ip_end = struct.unpack("!L", socket.inet_aton('10.255.255.255'))[0]
public = View.objects.get(name="public")
private = View.objects.get(name="private")

s = StaticInterface.objects.filter(ip_lower__gte=ip_start,ip_lower__lte=ip_end)
for x in s:
  x.views.remove(public)

a = AddressRecord.objects.filter(ip_lower__gte=ip_start,ip_lower__lte=ip_end)
for x in a:
  x.views.remove(public)

p = PTR.objects.filter(ip_lower__gte=ip_start,ip_lower__lte=ip_end)
for x in p:
  x.views.remove(public)

r = Range.objects.filter(start_lower__gte=ip_start,end_lower__lte=ip_end)
for x in r:
  x.views.remove(public)
