# Use the official Node.js image
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Clone the Uptime Kuma repo from GitHub
RUN git clone https://github.com/louislam/uptime-kuma.git .

# Install dependencies
RUN npm install

# Build Uptime Kuma
RUN npm run build

# Expose the port
EXPOSE 3001

# Start Uptime Kuma
CMD ["npm", "start"]
