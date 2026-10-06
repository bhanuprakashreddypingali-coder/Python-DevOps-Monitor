from datetime import datetime, timezone

import psutil
from fastapi import FastAPI, Response
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Gauge,
    generate_latest,
)

app = FastAPI(
    title="Python DevOps Monitoring Platform",
    description="Infrastructure health and monitoring API",
    version="1.0.0"
)

# Prometheus metrics
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of application requests",
    ["endpoint", "method"]
)

CPU_USAGE = Gauge(
    "system_cpu_usage_percent",
    "Current CPU usage percentage"
)

MEMORY_USAGE = Gauge(
    "system_memory_usage_percent",
    "Current memory usage percentage"
)

DISK_USAGE = Gauge(
    "system_disk_usage_percent",
    "Current disk usage percentage"
)


@app.get("/")
def home():
    REQUEST_COUNT.labels(endpoint="/", method="GET").inc()

    return {
        "project": "Python DevOps Monitoring Platform",
        "status": "running",
        "message": "Monitoring service is operational"
    }


@app.get("/health")
def health():
    REQUEST_COUNT.labels(endpoint="/health", method="GET").inc()

    return {
        "status": "UP",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/metrics")
def metrics():
    REQUEST_COUNT.labels(endpoint="/metrics", method="GET").inc()

    # Collect current system metrics
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    # Update Prometheus gauges
    CPU_USAGE.set(cpu)
    MEMORY_USAGE.set(memory.percent)
    DISK_USAGE.set(disk.percent)

    # Return Prometheus exposition format
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )