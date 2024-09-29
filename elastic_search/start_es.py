import subprocess

def start_elasticsearch():
    try:
        # Run the system command to start Elasticsearch
        result = subprocess.run(['sudo', 'systemctl', 'start', 'elasticsearch.service'], check=True)
        print("Elasticsearch started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Elasticsearch: {e}")

if __name__ == "__main__":
    start_elasticsearch()
