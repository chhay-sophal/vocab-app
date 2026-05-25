FROM node:20-alpine

WORKDIR /app

# Copy package files first to leverage Docker's caching mechanism
COPY package*.json ./
RUN npm install

# Copy the rest of your Vue source code
COPY . .

EXPOSE 5173

# Run the Vite development server, binding it to port 5173 
# The '--host' flag is crucial so Docker can route traffic to it
CMD ["npm", "run", "dev", "--", "--host"]