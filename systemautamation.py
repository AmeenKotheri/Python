import psutil

cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

if cpu_percent >= 50:
    print("The CPU Health is not ok something Hapening")
else:
    print("The CPU Health is OK")

memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")

if memory.percent >= 90:
    print("Something Happen Over using the memory")
else:
    print("Memory Health is Ok")

disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")

if disk.percent >= 90:
    print("The Disk Health Not Ok it overusing")
else:
    print("Disk Health is ok")
