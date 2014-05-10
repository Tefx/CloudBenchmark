from fabric.api import run, settings
from fabric.tasks import execute

def task(func):
	def f(password, *args, **kargs):
		with settings(password=password):
			result = func(*args, **kargs)
			if result.succeeded:
				return str(result)
			else:
				return None
	return f

@task
def launch_iperf():
	return run('nohup iperf -sD &', quiet=True)

@task
def test_iperf(ip):
	return run("iperf -r -c %s" % ip, quiet=True)

if __name__ == '__main__':
	result = execute(launch_iperf, hosts=["tefx-test-linux.cloudapp.net:12345"], password="Hh12345&")
	print result["tefx-test-linux.cloudapp.net:12345"]

	result = execute(test_iperf, hosts=["tefx-test-linux.cloudapp.net:12345"], password="Hh12345&", ip="100.85.220.115")
	print result["tefx-test-linux.cloudapp.net:12345"]