# Changing the OS configuration so that the holberton user can log in
# and open a file without any error message.
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
