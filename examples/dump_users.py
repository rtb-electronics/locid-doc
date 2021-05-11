#!/usr/bin/env python3

import serial
import json

with serial.Serial('/dev/ttyACM0') as s:
    while True:
        j = json.loads(s.readline())
        if j['method'] == 'locid.status':
            print("users:", j['params']['users'])
