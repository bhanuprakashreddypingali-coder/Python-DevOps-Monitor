FROM python:3.11-slim

WORKDIR /app

# Update Debian packages to the latest available security fixes
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install application dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Remove potentially stale vulnerable package installations
RUN python -m pip uninstall -y setuptools wheel msgpack jaraco.context \
    && python -m pip install --no-cache-dir \
        setuptools \
        wheel \
        msgpack \
        "jaraco.context>=6.1.0"

# Verify final installed versions
RUN python -c "import setuptools, wheel, msgpack; print('setuptools:', setuptools.__version__); print('wheel:', wheel.__version__); print('msgpack:', msgpack.__version__); import importlib.metadata as m; print('jaraco.context:', m.version('jaraco.context'))"

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]