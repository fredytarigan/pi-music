import bluetooth
import os
import subprocess
import pydbus


class Bluetooth():

    def __init__(self):
        self.bluetooth_on = False

    def enable_bluetooth(self):
        process = subprocess.Popen(
            ['/bin/systemctl', 'start', 'bluetooth'],
            stdout=subprocess.PIPE,
            universal_newlines=True
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
            universal_newlines=True
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
        # if not self.bluetooth_on:
        #     self.enable_bluetooth()

        device_addr = []

        devices = bluetooth.discover_devices(lookup_names=True)
        print("Found {} devices".format(len(devices)))

        for addr, name in devices:
            device = {
                "name": name,
                "addr": addr
            }
            device_addr.append(device)

        return device_addr

    def connect(self, addr):
        device_addr = addr
        adapter_path = '/org/bluez/hci0'
        device_path = f'{adapter_path}/dev_{device_addr.replace(":","_")}'

        bluez_service = 'org.bluez'
        bus = pydbus.SystemBus()
        adapter = bus.get(bluez_service, adapter_path)

        device = bus.get(bluez_service, device_path)

        device.Connect()
