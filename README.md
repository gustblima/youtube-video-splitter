# youtube-video-splitter
Using a csv as an input, extract portions of youtube videos and convert to gif (optional)


Edit the file input.csv adding one row per video or region that you want to extract


# Input    
  ### url
  Url from youtube
  >Example: `https://www.youtube.com/watch?v=jNQXAC9IVRw`
    
    
  ### timestamps
  The timestamp of the regions that you want to capture represented by `HH:MM:SS-HH:MM:SS`, it can have multiples timestamp separated by semicolon. Or you can duplicate the row and add another timestamp.
  >Example: `00:01:00-00:02-00;00:02:00-00:03:00`. This will generated two videos as output.
  
  
  ### convert_to_gif 
  It's `y` or `n`, if 'y' each extracted region of the video will be converted to gif format. 
  >Example: `y`. All the regions extracted with this row will be saved as gif
 
  
