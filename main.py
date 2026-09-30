from datetime import datetime, timezone

import psutil
from fastapi import FastAPI

app = FastAPI(
    title="Python DevOps Monitoring Platform",
    description="Infrastructure health and monitoring API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "Python DevOps Monitoring Platform",
        "status": "running",
        "message": "Monitoring service is operational"
    }


@app.get("/health")
def health():
    return {
        "status": "UP",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/metrics")
def metrics():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": {
            "total_mb": round(memory.total / (1024 * 1024), 2),
            "used_mb": round(memory.used / (1024 * 1024), 2),
            "percent": memory.percent
        },
        "disk": {
            "total_gb": round(disk.total / (1024 ** 3), 2),
            "used_gb": round(disk.used / (1024 ** 3), 2),
            "percent": disk.percent
        },
        "timestamp": datetime.now(timezone.utc).isoformat()
    }