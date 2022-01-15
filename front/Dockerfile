# stage1 as builder
FROM node:14-alpine as builder

WORKDIR /site

# Copy the package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy rest of the files
COPY . .

# Build the project
RUN npm run build


FROM nginx:alpine as production-build
#COPY ./nginx/nginx.conf /etc/nginx/conf.d

## Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Copy from the stahg 1
COPY --from=builder /site/dist /var/www/html

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]