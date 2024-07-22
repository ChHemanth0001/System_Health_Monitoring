# System_Health_Monitoring
Python script that checks the CPU usage, memory usage, disk space, and running processes.
##Prerequisites
- Python 3.x
- `psutil` library

Install the `psutil` library using pip:

#Thresholds
The threshold values that i choose to use here are as follows

CPU_THRESHOLD = 40.0  
MEMORY_THRESHOLD = 60.0  
DISK_THRESHOLD = 80.0 

This Script throws out desired outputs such as
    cpu_usage
    memory_usage
    disk_usage
    running_processes
