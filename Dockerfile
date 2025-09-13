# Use an official lightweight Python image
FROM python:3.11-alpine

# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser

# Set the working directory
WORKDIR /app

# Copy application files
COPY text_editor.py .
COPY my_text_file.txt .

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Run the application
CMD ["python", "text_editor.py"]