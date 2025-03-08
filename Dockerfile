# Use Python 3.9 Alpine as the base image
FROM python:3.9.21-alpine3.21

# Set the working directory inside the container
WORKDIR /pytest-container

# Copy all project files from the host (C:\Users\Administrator\PycharmProjects\Ecom-app) into /pytest-container
COPY . . /pytest-container

#Run selenium Grid
#RUN docker-compose.yaml

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r /pytest-container/requirements.txt

# Install Chromium browser and necessary dependencies (to run headless in Docker)
RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    nss \
    freetype \
    harfbuzz \
    ttf-freefont


# Set environment variables for Chromium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver

# Run Pytest with Allure and HTML reporting
CMD ["pytest", "test_cases/test_admin_login.py", "--alluredir=allure-results", "--html=report.html", "--browser=chrome"]

