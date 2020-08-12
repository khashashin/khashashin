# Build client App
FROM node:12.18.3-alpine3.11 as build

# Set working directory.
RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY ../client/khas-app/package*.json /app/

# Install app dependencies.
RUN npm install

# Copy app files.
COPY ../client/khas-app/ /app/

# Build app
RUN npm run build -- --output-path=./dist/out


# Prepare proxy
FROM nginx:1.19.1-alpine

# Copy compiled app files from previous build
COPY --from=build /app/dist/out /usr/share/nginx/html

COPY ./default.conf /etc/nginx/conf.d/default.conf
