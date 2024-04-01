# Use the official Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code to the container
COPY . .

# Set the command to run the application
CMD [ "python", "bot.py" ]