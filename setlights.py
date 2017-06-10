import lazylights
import time
import binascii
import argparse
#------------------------------------------------------------------------------------------------------------
# I use this to manually create a bulb using IP and MAC address.
def createBulb(ip, macString, port = 56700):
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
#------------------------------------------------------------------------------------------------------------
class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass

import argparse

parser = argparse.ArgumentParser(description='control lights. Both state and brightness arguments are optional and mutually exclusive',
                                 epilog='Examples of Use:\n----------------\nsetlights.py -s on -b 56',
                                 formatter_class=CustomFormatter)
requiredNamed = parser.add_argument_group('required named argument')
requiredNamed.add_argument('-s', '--state', dest='state', required=False, help='[Input] lights on or off'
requiredNamed.add_argument('-b', '--brightness', dest='brightness', required=False, help='[Input] brightness of lights: 0-100')
results = parser.parse_args()
print results

myBulb1 = createBulb('10.0.0.x','xx:xx:xx:xx:xx:xx')
#myBulb2 = createBulb('10.0.0.x','xx:xx:xx:xx:xx:xx')
bulbs=[myBulb1]

#bulbs = lazylights.find_bulbs(expected_bulbs=6)

if results.brightness:
    print "Setting Brightness"
    val = int(results.brightness)/float(100)
    print val
    lazylights.set_state(bulbs, 1, 0, val, 4000, 100, raw=False)
    exit(0)

if results.state=='on':
    print 'Turning on'
    lazylights.set_power(bulbs, True)
else:
    print 'Turning off'
    lazylights.set_power(bulbs, False)
