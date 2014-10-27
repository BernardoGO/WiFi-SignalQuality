import subprocess
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(dest='interface', nargs='?', default='wlan1')
args = parser.parse_args()
frame = 0

while True:
    frame = frame + 1
    cmd = subprocess.Popen('sudo iwconfig %s' % args.interface, shell=True, stdout=subprocess.PIPE)
    for line in cmd.stdout:
        if 'Link Quality' in line:
            if '=-' in line:
                print "-" + line.lstrip(' ').split('=-')[1] + str(frame) + ": ",
            else:
                print line.lstrip(' ')
        elif 'Not-Associated' in line:
            print 'No signal'
    
