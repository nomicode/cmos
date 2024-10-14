# Use the official Python image as a base
FROM python:3.9-slim

# Update apt and install pipx
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip \
    python3-venv \
    pipx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry using pipx
RUN pipx install poetry

# Set the PATH for pipx
ENV PATH="/root/.local/bin:$PATH"
