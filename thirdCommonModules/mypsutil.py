import psutil
# print(psutil.test())
print(psutil.disk_usage('/'))
print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))