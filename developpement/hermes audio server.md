https://pypi.org/project/hermes-audio-server/




Voice activity detection
```
"vad": {
    "mode": 0,
    "silence": 2,
    "status_messages": true
}
```
####mode    
This should be an integer between 0 and 3. 0 is the least aggressive about filtering out non-speech, 3 is the most aggressive. Defaults to 0.   
####silence     
This defines how much silence (no speech detected) in seconds has to go by before Hermes Audio Recorder considers it the end of a voice message. Defaults to 2  
####status_message      
This is a boolean: true or false. Specifies whether or not Hermes Audio Recorder sends messages on MQTT when it detects the start or end of a voice message. Defaults to false. This is useful for debugging, when you want to find the right values for mode and silence.  