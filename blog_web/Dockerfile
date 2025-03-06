# Use Alpine as the base image
FROM alpine:3.21.3


# Disable output buffering to ensure logs are shown in real-time
ENV PYTHONUNBUFFERED=1

# Install Python, pip, and other dependencies
RUN apk add --no-cache python3 py3-pip tzdata

# Set the working directory
WORKDIR /usr/src/app

# Tạo virtual environment
RUN python3 -m venv /usr/src/app/venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

# Copy requirements and install dependencies
COPY requirement.txt ./
RUN pip3 install --no-cache-dir --break-system-packages -r requirement.txt

# Copy application files
COPY ./ ./

# Expose the application's port
EXPOSE 8000

# Run the application
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ['gunicorn', 'blog_web.wsgi']
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog_web.wsgi:application"]