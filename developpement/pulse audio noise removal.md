# Pulse audio noise reduction (called eco cancellation)
https://askubuntu.com/questions/18958/realtime-noise-removal-with-pulseaudio
```
# Edit pulseaudio config
sudo nano /etc/pulse/default.pa

# Add this line at the place that talk about eco cancellation
load-module module-echo-cancel
```
