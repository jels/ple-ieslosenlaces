# Ubuntu #

## Usar el apt-cache ##
```
echo 'Acquire::http::Proxy "http://172.30.6.92:3142";' | sudo tee /etc/apt/apt.conf.d/01proxy
```