# This is the Build Stage 
FROM python:3.12-slim as builder 


RUN apt-get update && apt-get install -y \ 
  build-essential \ 
  && rm -rf /var/lib/apt/lists* 


WORKDIR /app 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Runtime stage
FROM python:3.12-slim

RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin


COPY . .

RUN chown -R appuser:appuser /app

USER appuser


EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
