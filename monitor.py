import requests
import psutil

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
   
    return cpu, memory

def check_logs():
    error_count = 0
    with open('app.log', 'r') as file:
        for line in file:
            if 'ERROR' in line:
                error_count += 1
    return error_count

def check_api():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        if response.status_code == 200:
            return "UP"
        else:
            return "DOWN"

    except:
        return "DOWN"

   




import time

while True:
    cpu, memory = check_system()
    errors = check_logs()
    api_status = check_api()

    print("\n=================================")
    print("\--- Application Health Check ---")
    print("=================================")   
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Total Errors: {errors}")
    print(f"API Status: {api_status}")

    if cpu > 80:
       print("Warning: High CPU Usage")
    if errors > 2:
       print("Warning: High number of errors in logs")
    if api_status == "DOWN":
       print("Warning: API is down")

    time.sleep(5)  # Check every 60 seconds

    def save_report(cpu, memory, errors, api_status):
        with open('health_report.txt', 'a') as file:
           file.write(f"CPU Usage: {cpu}%, Memory Usage: {memory}%, Errors: {errors}, API Status: {api_status}\n")

    save_report(cpu, memory, errors, api_status)






