FROM nginx

# Copy the nginx.conf file to the appropriate location in the image
COPY nginx.conf /etc/nginx/nginx.conf