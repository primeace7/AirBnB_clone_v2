#!/usr/bin/env bash
# set up web servers for deployment of web_static

# update packages repo
apt update

# install Nginx
apt install nginx -y

# create folders
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

# create fake HTML file
html_file='/data/web_static/releases/test/index.html'
cat > $html_file <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# create sym link
ln -sn /data/web_static/releases/test /data/web_static/current

# change ownership of /data/
chown -RP ubuntu:ubuntu /data/

# update Nginx config file
config='/etc/nginx/sites-enabled/default'
old_line="root \/var\/www\/html;"
new_line="$old_line\n\n\tlocation \/hbnb_static \{\n\t\talias \/data\/web_static\/current;\n\t\}"

sed -i "s/$old_line/$new_line/" $config

# remove duplicates/backups
rm /etc/nginx/sites-enabled/*~

# restart Nginx
service nginx restart
