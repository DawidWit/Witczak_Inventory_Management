# Use an official Node.js image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy the rest of the app
COPY . .

# Expose the frontend port
EXPOSE 3000

# Run the dev server
CMD ["npm", "run", "dev"]
