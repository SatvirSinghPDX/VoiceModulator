# Computers, Sound, and Music Final Project — Spring 2020

Authors: Satvir Singh (satvir@pdx.edu) & David Hogan (davhogan@pdx.edu)

## Introduction
The purpose of the Voice Modulator is to allow a user to record their voice then playback the recording with an effect.
The available effects are: 
  * A robot voice
  * A helium effect
  * Having it sound like it is raining in the background
  * An echo effect
  * A chimpmunk effect
  * A effect to play the recording in reverse
  * A slow mo effect
  * An effect to make it sound like the user is in a public place
  
## Launch
To launch the VoiceModulator run user_interface.py.  
VoiceModulator was built using a python 3.8 interpreter.  
Use command pyhton3 user_interface.py to run from terminal.  

## How To Use
To record using the VoiceModulator press the Mic button on the left.   
![Image](https://github.com/SatvirSinghPDX/VoiceModulator/blob/master/mic.png?raw=true)   
To finish recording hit the Stop button on the right.  
![Image](https://github.com/SatvirSinghPDX/VoiceModulator/blob/master/stop.png?raw=true)  
Once recording is finished press any of the effect buttons to hear the recording with the desired effect applied.  
This process can be repeated for as many recordings as the user wants, however only the most recent recording will be played.  
  
## Testing
Testing was done manually. For testing, both authors would try recording at different length and then make sure all of the effects were applied correctly to the recording.  
The shortest recording tested was 1 second and the longest was one minute.  
## Project Discussion
### What Worked
The echo, rain and public place effect all worked by overlaying other audio to the recording. This went smoothly and was simple to implement once understood.  
The slowmo and chimpunk effects used change in rates of the recording, which was implemented using the wave audio librabry.  
The pitch shifting was more complicated and took awhile to figure out. This resulted in a product that does have some artifacts in the effect recording. But it does work.  
### What Didn't Work
We were unable to get the effects to work in realtime. This was a frusturation that we didn't overcome.  
The other issue we had was rewriting the named files. To get around this we generated random 10 char strings for the filenames which is a little hacky.
### Project Satisfaction
We are somewhat satisified with the project. We felt our implementaion of the effects was well done. However we didn't meet our original project goal of having a live effect to the input. This was the aspect of the project we were most dissapointed about.
### Future Improvements
  - One thing we would like to add in the future would be giving the user the ability to choose live input, meaning they could apply effects to the live audio as they speak. This could be used with software such as Zoom or Google Hangouts.
  - Another thing we would have liked to add would be the ability to choose whether or not they want the effected audio to be saved to a file instead of doing so by default.
  - Adding some more effects would have been a nice improvement, we currently have nine.
## Sources:
  - Referenced for timer functionality: https://www.geeksforgeeks.org/create-stopwatch-using-python/  
  - Referenced for pitch shift functionality: https://stackoverflow.com/questions/43963982/python-change-pitch-of-wav-file  
  - Referenced for overlay effects: https://medium.com/better-programming/simple-audio-processing-in-python-with-pydub-c3a217dabf11
  
## License
[MIT](https://choosealicense.com/licenses/mit/)
