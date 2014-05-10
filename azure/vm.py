from sh import azure
import json
import time

def create_vm(dns, port, name, size, image, username, password):
    # print azure.vm.create(dns, image, username, password, e=port, n=name, json=True, z=size)
    print wait_ready(name)

def wait_ready(name):
	while True:
		info = azure.vm.show(name, json=True)
		print info
		info = json.loads(info)
		if info["InstanceStatus"] == "ReadyRole":
			break
		print info["InstanceStatus"]
		time.sleep(5000)
	return info

def delete_vm(name, disk):
	azure.vm.delete(name, "-bq", json=True)
	azure.vm.disk.delete(disk)

if __name__ == '__main__':
	create_vm("tefx-test-linux", 12345, "ubuntu-t-0", "extrasmall", "ubuntu-t", "tefx", "Hh12345&")
	# delete_vm("ubuntu-t-0", "ubuntu-0-ubuntu-0-0-201402091941550840")