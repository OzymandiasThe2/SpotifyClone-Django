# SpotifyClone-Django
Made using Django, this was made for the group's final project in Database Systems.

## Documentation 

### Technical Overview of Database Web Application:

For our final project, we have decided to create a Spotify clone web application. Its name is Napster 2.0. Named after the notorious audio streaming, and peer-to-peer file-sharing site from 20 years ago.

#### Features and Uses:
Napster 2.0 is a feature-rich music-streaming web application. It functions similarly to music streaming sites such as Spotify, but with one major change. You bring your own music. Users can create their own albums, and fill them up with songs that they upload to their accounts. Each user can favourite songs, in order to curate and organize their music. Additionally, users can personalize their profiles by uploading their own profile pictures on the profile page. Napster 2.0 also has the ability to share music with other users through the use of links. Each song uploaded to the site is given an ID, and by sharing the link with that ID, anyone can share music with others. This makes it a versatile platform for listening to your music, regardless of where you got it from.

#### Step-by-step instructions:

To begin using Napster 2.0, you must first create yourself a user account. This can be done by following the instructions on the login page to reach the registration page. Here you can create your account, to do so you must provide a username and a password, providing an email is optional. No two usernames can be the same. If you do choose to provide an email address, then it will only accept one that is valid.

Now that you have created your account, you are ready to use the service. However, if you ever need to edit your account info, that can be done by navigating to the profile section on the top menu bar. Here you have the option to change your username and email address. You can also upload a photo to use as your profile picture if you want to personalize your page.

You can begin by creating a personal album for your music, this will function much like a playlist on a service like Spotify. To create an Album, simply click the “Add an Album” button. You will then need to provide some information about the album, such as the artist's name, the album’s title, as well as the genre. You then also must provide an image file to use as the album cover art. Once that is added, simply click the “Submit” button, and your album will be created. After creating your first album, the creation of any subsequent albums can be done from the top menu bar.

Once you have created an album, you can now begin adding songs to it. While in the page for your album, simply click the “Add Song” button. From here, you just need to provide the Song’s name, as well as the audio file. Once the song has been uploaded, you will see it both within the album it is a part of, as well as in the songs tab. When viewed through the album, the song will have three options associated with it. The first is to play the song, which will open up another tab and play the selected song. The other options are to favourite the song, as well as delete it. If you choose to favourite the song, it will appear in the list of favourites under the songs tab.
Once you have added some Albums and Songs to your profile, you can use the search bar at the top of the page to quickly find a certain album or song. 
Additionally, due to the open-sharing nature of the original Napster, we emulated the sharing trait, by allowing users to share albums that they have created by viewing the album information on the album you want, copying the address which should be displayed as “shriji10.pythonanywhere.com/X/” where X is some number assigned to that album. Then you can send that link to a friend or whoever you want to share and, as long as they have an account, can also view and access your music album through shared links. Napster 2.0 was designed entirely around its slogan – Piracy for a new age. 

Another useful feature is for users to change their settings. After a user has logged in, in the top right corner of the navbar, they can click on the profile button and have access to their account information. This page has a form that allows for them to change/add/remove their profile image, as well as change their username and email address. By default, the user has the Napster 2.0 logo as their profile picture and can change it to look like whatever they want. This change will then be seen on the homepage as your new profile picture will replace the Napster logo that was part of the “Z’s Albums” where Z is the user’s username. 


### ER Diagram
![image](https://user-images.githubusercontent.com/62310972/168929292-77ea9a37-c62d-4b5f-ae0d-953023ff9e56.png)

### Overview of Technologies Used:
- HTML
- CSS
- PYTHON
- SQLite3
- Django backend 
- GitHub storage
- PythonAnywhere Hosting
- Libraries:
  - jQuery 
  - Font-awesome 
  - Bootstrap
  - Django-crispy-forms



## Selfhosting the website
- clone the repo
- the manage.py should already be able to run the server

## Troubleshooting: 
Make sure you have proper django version, the porject uses Django 4.0.4
  - ```python -m django --version```
If you made any changes to the models then you'll have to make migrations in order to update the db
  - ```./manage.py makemigrations```
  - ```./manage.py migrate```


# License and Uses

All code invovled with project are created by: Shriji Shah 

Reviewed by project partners: Ryan Manzie, Noah Morin, Blake Whiting

As this was made for a academic project, you cannot copy or plagiarize the code/images used.
