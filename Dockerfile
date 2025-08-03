# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY text_editor.py .
COPY my_text_file.txt .

# Run the script
CMD ["python", "text_editor.py"]