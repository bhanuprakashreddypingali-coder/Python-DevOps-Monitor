# Python DevOps Monitoring Platform

A production-style DevOps monitoring project built with **Python, FastAPI, Docker, GitHub Actions, Trivy, Kubernetes, Prometheus, and Grafana**.

The project demonstrates an end-to-end DevOps workflow from application development and automated testing to containerization, security scanning, Kubernetes deployment, and real-time monitoring.

---

## 🚀 Project Overview

The Python DevOps Monitoring Platform is a lightweight FastAPI application designed to expose application health and infrastructure metrics.

The application provides:

- Application health monitoring
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Prometheus-compatible metrics
- Automated unit testing
- Docker containerization
- CI/CD using GitHub Actions
- Container security scanning using Trivy
- Kubernetes deployment
- Prometheus monitoring
- Grafana dashboards

---

## 🏗️ Architecture

```text
                    Developer
                       |
                       v
                    GitHub
                       |
                       v
              GitHub Actions CI/CD
                       |
          +------------+------------+
          |            |            |
       Pytest       Docker       Trivy
          |          Build       Security
          |            |           Scan
          |            |            |
          +------------+------------+
                       |
                       v
                  GitHub GHCR
                       |
                       v
                  Kubernetes
                       |
          +------------+------------+
          |            |            |
        Pod 1        Pod 2        Pod 3
          |            |            |
          +------------+------------+
                       |
                    /metrics
                       |
                       v
                  Prometheus
                       |
                       v
                    Grafana
                       |
                       v
              Monitoring Dashboard