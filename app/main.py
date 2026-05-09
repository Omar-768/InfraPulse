from fastapi import FastAPI
import socket
import psutil
import time
import json
import os
from pathlib import Path
import boto3

app = FastAPI()

START_TIME = time.time()
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

S3_BUCKET = os.getenv("S3_BUCKET", "")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_PREFIX = "reports"

def build_system_report():
    return {
        "project": "InfraPulse",
        "hostname": socket.gethostname(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "uptime_seconds": int(time.time() - START_TIME)
    }

def build_network_report():
    checks = {
        "dns_resolution": False,
        "https_port_443": False,
        "http_port_80": False
    }

    try:
        socket.gethostbyname("google.com")
        checks["dns_resolution"] = True
    except Exception:
        pass

    for host, port, key in [
        ("google.com", 443, "https_port_443"),
        ("example.com", 80, "http_port_80")
    ]:
        try:
            with socket.create_connection((host, port), timeout=3):
                checks[key] = True
        except Exception:
            pass

    return checks

def upload_report_to_s3(report_path: Path):
    if not S3_BUCKET:
        return {
            "enabled": False,
            "uploaded": False,
            "reason": "S3 bucket not configured"
        }

    object_key = f"{S3_PREFIX}/{report_path.name}"

    try:
        s3 = boto3.client("s3", region_name=AWS_REGION)
        s3.upload_file(str(report_path), S3_BUCKET, object_key)

        return {
            "enabled": True,
            "uploaded": True,
            "bucket": S3_BUCKET,
            "object_key": object_key
        }
    except Exception as e:
        return {
            "enabled": True,
            "uploaded": False,
            "error": str(e)
        }

@app.get("/")
def root():
    return {
        "project": "InfraPulse",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/system")
def system():
    return build_system_report()

@app.get("/network-check")
def network_check():
    return build_network_report()

@app.get("/report")
def report():
    timestamp = int(time.time())

    data = {
        "generated_at_epoch": timestamp,
        "system": build_system_report(),
        "network": build_network_report()
    }

    latest_report = REPORT_DIR / "latest_report.json"
    timestamped_report = REPORT_DIR / f"report_{timestamp}.json"

    with open(latest_report, "w") as f:
        json.dump(data, f, indent=2)

    with open(timestamped_report, "w") as f:
        json.dump(data, f, indent=2)

    s3_result = upload_report_to_s3(timestamped_report)

    return {
        "message": "Report generated successfully",
        "latest_report_path": str(latest_report),
        "timestamped_report_path": str(timestamped_report),
        "s3_upload": s3_result,
        "data": data
    }