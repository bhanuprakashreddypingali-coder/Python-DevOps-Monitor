
FROM python:3.11-slim

WORKDIR /app

# Update Debian packages to the latest available security fixes
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Upgrade Python packaging tools and vulnerable dependencies
RUN python -m pip install --no-cache-dir --upgrade \
        pip \
        setuptools \
        wheel \
        "jaraco.context>=6.1.0" \
        "msgpack>=1.2.1" \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip install --no-cache-dir --upgrade \
        setuptools \
        wheel \
        "jaraco.context>=6.1.0" \
        "msgpack>=1.2.1"

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

