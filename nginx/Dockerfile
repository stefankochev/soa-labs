FROM nginx:1.17.6

RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y apache2-utils jq

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
COPY env_setup.sh /env_setup.sh

ENTRYPOINT ["/serve.sh"]