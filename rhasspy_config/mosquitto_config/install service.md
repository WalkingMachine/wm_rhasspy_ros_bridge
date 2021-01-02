sudo nano /etc/systemd/system/mosquitto.service
```
[Unit]
Description=Insite MQTT Broker

[Service]
ExecStart=/usr/local/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf
Restart=always

[Install]
WantedBy=multi-user.target
```

sudo systemctl enable mosquitto.service
sudo service mosquitto start
