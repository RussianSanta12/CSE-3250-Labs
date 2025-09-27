import paramiko
import threading

def rpi1():
	stdin,stdout,stderr=RPI_1.exec_command('python3 testMine.py ' + '3')
	output = stdout.readlines()
	for items in output:
		print("RPI_1:" + items)
	error = stderr.readlines()
	for items in error:
		print("error - RPI_1:" + items)

def rpi2():
        stdin,stdout,stderr=RPI_2.exec_command('python3 testMine.py ' + '3')
        output = stdout.readlines()
        for items in output:
                print("RPI_2:" + items)
        error = stderr.readlines()
        for items in error:
                print("error - RPI_2:" + items)

RPI_1 = paramiko.SSHClient()
RPI_2 = paramiko.SSHClient()


RPI_1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
RPI_2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
RPI_1.connect(hostname='localhost',username='pgb10',port=5022,password='pgb10')
RPI_2.connect(hostname='localhost',username='pgb10',port=5024,password='pgb10')



t1 = threading.Thread(target=rpi1)
t2 = threading.Thread(target=rpi2)

print("RPI_1 started")
t1.start()
print("RPI_2 started")
t2.start()
t1.join()
t2.join()

RPI_1.close()
RPI_2.close()
