# 🚀 FastAPI-Docker-Pydantic-Practice
This repository is a collection of practical projects and learning exercises focused on building modern APIs with FastAPI, data validation with Pydantic, and containerization with Docker. It includes hands-on implementations of API development, data modeling, and deployment workflows, showcasing proficiency in backend development and DevOps practices.
📖 Overview
This project serves as a practice hub for mastering FastAPI, Pydantic, and Docker. It includes a variety of exercises, such as building a patient management API, exploring Pydantic for robust data validation, and containerizing applications for scalable deployment. The repository demonstrates practical skills in creating production-ready APIs and managing containerized environments.
🎯 Features

FastAPI-based RESTful APIs with endpoints for real-world use cases (e.g., patient management).
Pydantic models for data validation and serialization.
Docker configurations for containerizing API applications.
Modular code structure for learning and experimentation.
Practical examples of API routing, request handling, and response formatting.

🛠️ Tech Stack

Python: Core programming language.
FastAPI: High-performance framework for building APIs.
Pydantic: Data validation and settings management.
Docker: Containerization for deployment and scalability.
Uvicorn: ASGI server for running FastAPI applications.
Git: Version control with .gitignore for clean repository management.

🚀 Getting Started
Prerequisites

Python 3.8+
Docker and Docker Compose
Git

Installation

Clone the repository:git clone https://github.com/RachitNigam19/FastAPI-Docker-Pydantic-Practice.git
cd FastAPI-Docker-Pydantic-Practice


Install Python dependencies:pip install -r requirements.txt

(Note: If requirements.txt is not present, install fastapi, uvicorn, and pydantic manually: pip install fastapi uvicorn pydantic)
Set up Docker (if Docker files are present in subfolders like Machine or Patient API Management):docker-compose up --build



Usage

Run a FastAPI application (e.g., from Patient API Management):uvicorn main:app --reload


Access the API at http://localhost:8000 and interactive docs at http://localhost:8000/docs.


Explore Pydantic examples in Pydantic Crash Course:python pydantic_example.py


Build and run Docker containers for specific projects:docker build -t patient-api .
docker run -p 8000:8000 patient-api



📂 Project Structure
FastAPI-Docker-Pydantic-Practice/
├── Machine/                     # Docker-related experiments and configurations
├── Patient API Management/      # FastAPI project for patient management API
├── Pydantic Crash Course/       # Pydantic data validation exercises
├── __pycache__/                 # Python bytecode cache (auto-generated)
└── *.py                         # Additional FastAPI and Pydantic scripts

🔍 How It Works

Patient API Management: A FastAPI project with endpoints for managing patient data, using Pydantic for request/response validation.
Pydantic Crash Course: A set of scripts demonstrating Pydantic’s data modeling, validation, and serialization features.
Machine: Likely contains Docker configurations or machine-specific setups for containerized API deployment.
FastAPI: Implements high-performance APIs with async support and automatic OpenAPI documentation.
Docker: Enables containerized deployment for consistent and scalable environments.

🌟 Why This Project?

Showcases expertise in modern API development with FastAPI.
Demonstrates proficiency in data validation using Pydantic.
Highlights DevOps skills with Docker for containerized deployments.
Reflects clean coding practices with modular, well-organized code.
Provides practical examples for building production-ready APIs.

📫 Contact

GitHub: RachitNigam19
LinkedIn: Rachit Nigam
Email: rachitn46@gmail.com

Feel free to explore, contribute, or reach out for collaboration!
