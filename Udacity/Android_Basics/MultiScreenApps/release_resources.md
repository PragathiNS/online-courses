### MediaPlayer

1. When other button is clicked
2. When the app goes to the background - 
it's good practice to release resources when we are done with the MediaPlayer which is true during onStop().


Audio Focus
1. Pause the sound when a call comes and resume once the call is completed.
2.RequestAudioFocus(), releaseAudioFocus() 
