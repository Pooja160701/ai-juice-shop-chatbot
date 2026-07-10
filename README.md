# 🤖 AI-Powered OWASP Juice Shop Assistant

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5--mini-412991?logo=openai)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5?logo=kubernetes)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?logo=githubactions)
![Trivy](https://img.shields.io/badge/Trivy-Security_Scanning-1904DA)
![GHCR](https://img.shields.io/badge/GHCR-Container_Registry-181717?logo=github)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C?logo=prometheus)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end AI-powered assistant for OWASP Juice Shop built using FastAPI, OpenAI, ChromaDB, Docker, Kubernetes, and GitHub Actions.

The project demonstrates production-style deployment engineering practices, including containerization, CI/CD, security scanning, image publishing, and Kubernetes deployment.

---

# 📌 Project Overview

The AI-Powered OWASP Juice Shop Assistant enhances the OWASP Juice Shop application by providing an intelligent chatbot capable of answering questions about products using Retrieval-Augmented Generation (RAG).

Instead of relying solely on a language model, the assistant retrieves relevant product information from a vector database before generating responses, resulting in more accurate and contextual answers.

The project also demonstrates modern DevOps and Platform Engineering practices including Docker image optimization, automated CI/CD pipelines, vulnerability scanning, GitHub Container Registry, Kubernetes deployments, health monitoring, and secret management.

---

# ✨ Features

- AI-powered product assistant
- Retrieval-Augmented Generation (RAG)
- OpenAI GPT integration
- ChromaDB vector database
- FastAPI backend
- Docker containerization
- Docker Compose orchestration
- GitHub Actions CI
- Trivy container security scanning
- GitHub Container Registry (GHCR)
- Kubernetes deployment (Minikube)
- Kubernetes Secrets
- Readiness & Liveness Probes
- Resource Requests & Limits
- Structured logging
- Health check endpoint

---

# 🏗️ Solution Architecture

![alt text](images/arch.png)

---

# 📂 Project Structure

```text
ai-juice-shop-chatbot/
│
├── ai-service/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── ingestion/
│   │   ├── middleware/
│   │   ├── rag/
│   │   └── main.py
│   │
│   ├── chroma_db/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── juice-shop/
│
├── kubernetes/
│   ├── ai-service/
│   ├── juice-shop/
│   └── secrets/
│
├── monitoring/
│
├── docker-compose.yml
│
└── .github/
    └── workflows/
```

---

# ⚙️ Technology Stack

| Category           | Technologies              |
| ------------------ | ------------------------- |
| Backend            | FastAPI, Python           |
| AI                 | OpenAI GPT-5 Mini         |
| Vector Database    | ChromaDB                  |
| Frontend           | OWASP Juice Shop          |
| Containerization   | Docker                    |
| Orchestration      | Docker Compose            |
| CI/CD              | GitHub Actions            |
| Registry           | GitHub Container Registry |
| Security           | Trivy                     |
| Container Platform | Kubernetes (Minikube)     |
| Monitoring         | Prometheus                |
| Version Control    | Git & GitHub              |

---

# 🚀 CI/CD Pipeline

The project uses GitHub Actions to automate the deployment workflow.

Pipeline includes:

* Checkout Repository
* Install Dependencies
* Build FastAPI Application
* Build Juice Shop
* Docker Validation
* Docker Image Build
* Trivy Security Scan
* Publish Docker Images to GHCR

---

## 🚀 Deployment Workflow

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├────────────► Install Dependencies
    ├────────────► Run Tests
    ├────────────► Docker Build
    ├────────────► Trivy Scan
    └────────────► Push Image to GHCR
                           │
                           ▼
                    GitHub Container Registry
                           │
                           ▼
                  Kubernetes (Minikube)
                           │
                 Rolling Deployment
                           │
                           ▼
                  AI Juice Shop Running
```

---

# ☸️ Kubernetes Deployment

The application is deployed on a Kubernetes cluster using Minikube.

Deployment includes:

* Deployments
* Services
* Kubernetes Secrets
* Resource Requests
* Resource Limits
* Readiness Probes
* Liveness Probes
* Rolling Updates

---

# 🔐 Security

Security best practices implemented:

* Kubernetes Secrets
* GitHub Secrets
* Trivy Vulnerability Scanning
* Optimized Docker Images
* Environment Variable Management

---

# 📊 Deployment Verification

Verify Kubernetes resources:

```bash
kubectl get all -n juice-shop
```

View application logs:

```bash
kubectl logs deployment/ai-service -n juice-shop
```

Port forward the AI service:

```bash
kubectl port-forward svc/ai-service 8000:8000 -n juice-shop
```

Health endpoint:

```
http://localhost:8000/health
```

---

# 🐳 Docker

Build AI Service

```bash
docker build -t ai-service ./ai-service
```

Run Docker Compose

```bash
docker compose up --build
```

---

# ☸️ Kubernetes

Deploy application

```bash
kubectl apply -f kubernetes/
```

Verify deployment

```bash
kubectl get all -n juice-shop
```

---

# 📸 Screenshots

![alt text](images/image.png)

![alt text](images/image-3.png)

![alt text](images/image-4.png)

![alt text](images/image-5.png)

![alt text](images/image-6.png)

![alt text](images/image-7.png)

---

# 🔮 Future Enhancements

* Helm Charts
* Horizontal Pod Autoscaler
* NGINX Ingress
* AWS EKS Deployment
* Terraform Infrastructure
* Grafana Dashboards
* Loki Log Aggregation
* GitOps with ArgoCD

---

# 👩‍💻 Author

**Pooja**

GitHub: [https://github.com/Pooja160701](https://github.com/Pooja160701)

---