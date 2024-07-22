import psutil
import logging


logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


CPU_THRESHOLD = 50.0  
MEMORY_THRESHOLD = 50.0  
DISK_THRESHOLD = 50.0  

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
        print(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage: {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")
        print(f"High Memory usage detected: {memory_usage}%")
    else:
        logging.info(f"Memory usage: {memory_usage}%")

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk_usage}%")
        print(f"High Disk usage detected: {disk_usage}%")
    else:
        logging.info(f"Disk usage: {disk_usage}%")

def check_running_processes():
    processes = len(psutil.pids())
    logging.info(f"Number of running processes: {processes}")
    print(f"Number of running processes: {processes}")

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    
