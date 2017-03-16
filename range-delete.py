#!/usr/bin/env python

# empty a range... and delete it.  easy to make it do dynamic.. guess how.
import activate
activate.activate()

from cyder.models import *

Range.objects.get(start_str="10.195.128.2").staticinterfaces.delete()
#Range.objects.get(start_str=).delete()

