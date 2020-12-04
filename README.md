# Cloudflare-Dynamic-IP-Updater
Update A records using Cloudflare API

I use it on my raspberry pi to check and update every 1 hour with cron:
```
0 * * * * /usr/bin/python3 /home/user/Cloudflare-Dynamic-IP-Updater/cloudflareupdater.py >> /home/user/Cloudflare-Dynamic-IP-Updater/cronip.log 2>&1
```
