# Telepresence Demo 
url: https://www.telepresence.io/

# Install
## MacOS
`brew install telepresence`

## Linux 
```bash 
   sudo curl -fL https://app.getambassador.io/download/tel2/linux/amd64/latest/telepresence -o /usr/local/bin/telepresence
   sudo chmod a+x /usr/local/bin/telepresence
```

## Windows
https://www.telepresence.io/docs/latest/install/?os=windows


# vpn proxy
```bash
telepresence connect
```

now show in demo how I connect to internal only services via browser
i.e

```
http://wireguard-wg-access-server-web.wireguard/signin
http://ui.lab/
http://argocd-server.devtroncd/
```


# Intercept
```bash
telepresence list # List current intercepts
telepresence intercept backend --port 9090:80 # Intercept a service
telepresence leave # Remove existing intercept
```


# Quit
```bash
telepresence quit
```



