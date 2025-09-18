# Stage 1: Build stage with full OS to install dependencies
FROM python:3.11-slim as builder

# Set the working directory inside the container
WORKDIR /app

# Create and activate a virtual environment
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Stage 2: Final stage with only the necessary files
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/venv ./venv

# Copy the application source code
COPY ./src ./src

# Activate the virtual environment for the final command
ENV PATH="/app/venv/bin:$PATH"

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
# We use 0.0.0.0 to make it accessible from outside the container
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]