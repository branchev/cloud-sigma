# You can choose a base image depending on your requirements
# For example, if your project needs Python, you can use python:3.9-slim
FROM python:3.9-slim

# Set environment variables, if any
# ENV EXAMPLE_VAR=value

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file to the working directory
COPY sigma_warehouse/requirements.txt ./sigma_warehouse/requirements.txt
COPY sigma_accounting/requirements.txt ./sigma_accounting/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r sigma_warehouse/requirements.txt
RUN pip install --no-cache-dir -r sigma_accounting/requirements.txt

# Copy the rest of the application code to the working directory
COPY . .
