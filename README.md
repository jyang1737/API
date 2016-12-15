
# Live Song and Prosper

### This site takes your images and returns a song about them. Perfect for the bar-mitzvah slide show or the ideal musical birthday card. 

## How it Works: <br>
   1. A user either upload an image or pastes a link to an image from the home page. <br>
   2. The user is either redirected to an error page or to a page, with background colors similiar to the ones in the image, that lists the words correspodning to the image and songs that contained such words. <br>
   3. The user can click on each song to view the author and lyrics of each song. <br>
   
A secret key file called secretdata.txt needs to be stored in the root directory. Contact a developer if you wish to obtain this file.   
   
### Note:
To make upload functionality work, we used the poster module to encode file data. The files are included in utils, so not pip is neccessary.
   
Full lyrics for every song are not always availble, as the copyright varies from song to song.
   
## Instalation
   1. start a virtual enviroment with flask installed
   2. $ python app.py   
   
## Known Bugs: 
   Sometimes and unreproducibly, a broken pipe error will occur. To fix this, resart the flask app and reload the page. We were unable to isolate the cause of this error
   
   If a file is over 16mb, it redirects to a blank page. Press back to go to the homepage and reuplaod a smaller file 

   
