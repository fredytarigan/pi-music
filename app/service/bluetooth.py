import bluetooth
import os
import subprocess


class Bluetooth():

    def __init__(self):
        self.bluetooth_on = False

    def enable_bluetooth(self):
        process = subprocess.Popen(
            ['/bin/systemctl', 'start', 'bluetooth'],
            stdout=subprocess.PIPE,
            universal_newline=True
        )

        while True:
            output = process.stdout.readline()
            print(output.strip())

            return_code = process.poll()
            if return_code:
                print('Received return code {}'.format(return_code))
                for output in process.stdout.readlines():
                    print(output.strip())
                break

        self.bluetooth_on = True

    def disable_bluetooth(self):
        process = subprocess.Popen(
            ['/bin/systemctl', 'stop', 'bluetooth'],
            stdout=subprocess.PIPE,
            universal_newline=True
        )

        while True:
            output = process.stdout.readline()
            print(output.strip())

            return_code = process.poll()
            if return_code:
                print('Received return code {}'.format(return_code))
                for output in process.stdout.readlines():
                    print(output.strip())
                break

        self.bluetooth_on = False

    def search_devices(self):
        if not self.bluetooth_on:
            self.enable_bluetooth()

        devices = bluetooth.discover_devices(lookup_name=True)
        print("Found {} devices".format(len(devices)))

        for addr, name in devices:
            print("{} - {}".format(addr, name))
