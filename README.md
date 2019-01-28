# CloudRapper - An online music store with some social networking features 
Welcome to CloudRapper - an online music store where you can register, follow other users, add songs to your dashboard and recommend your favorite songs to other users who you follow.

Songs and Albums are added through the admin interface using the Class Based CRUD Model forms. Only superusers have the ability to add the songs and albums with the actual mp3 file. File checks are implemented using validators. Decorators are used for login_required and to check whether the logged in user is a superuser or not.

For each user, full account related settings are provided like if they want to change their name, profile-pictures, their portfolio url link and more.

The project includes following 3rd party libraries :

<p>-Django Crispy Forms (For managing and styling CRUD forms using bootstrap)</p>
<p>-Django Rest Framework (For API data interchange)</p>
<p>-Django Clean State (For file handling, deleting the files which are no longer in use)</p>
