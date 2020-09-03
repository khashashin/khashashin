FROM node:12.18.3-alpine3.11

# Set working directory.
RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY package*.json /app/

# Install app dependencies.
RUN npm install

# Copy app files.
COPY . /app/

# Build app
RUN npm run build -- --output-path=./dist/out

