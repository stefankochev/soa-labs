FROM nginx:1.23.3

# Remove default Nginx config
RUN rm /etc/nginx/nginx.conf

# Copy the modified Nginx conf
COPY nginx.conf /etc/nginx

# Copy proxy config template file
COPY api_nginx.conf /api_nginx.conf.template

# Create proxy def file
RUN mkdir /etc/nginx/sites-enabled
RUN touch /etc/nginx/sites-enabled/api_nginx.conf

# Copy the custom setup and entrypoint scripts
COPY serve.sh /serve.sh

ENTRYPOINT ["/bin/bash", "/serve.sh"]