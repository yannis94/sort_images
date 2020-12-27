# Clean your uploads folder (Wordpress)

Got a Wordpress with hundreds of pics and I wanna sort all useless images and delete them in the DB.

I know that some plugins aleready exist but 

	- Kind of scared to let plugin delete things in the database
	- The challenge !
	- Trying to understand a little bit more how Wordpress is build.

I list few steps to solve that challenge.

## 1/ Create a list with all used images

With [Screaming Frog](https://www.screamingfrog.co.uk/) I have a list with all used images on every page of the web site (the one I want to keep).
Saved this list as *used_images.txt*

## 2/ Create a list with all images (with the useless one too)

All images pushed on Wordpress are stored in the uploads directory, with multiple other directories inside (date hierarchy like **./uploads/2019/11/** for exemple).
I wrote a script in python call **partOne.py** for that task. 
One thing to keep in mind, Wordpress save your pic in multiple format (for thumbnail etc..) but store your pic in the database only with the main path.
 
###### Exemple :
> You push *my_pics.png*, Wordpress save this pic in multiple format like *my_pics-250x250.png* or *my_pics-1024x645.png* in the **uploads** folder but it will be stored as http://yourdomain.com/wp-content/uploads/2020/12/my_pics.png only, in the database.

So the bubbleSort function is here to group all declinate pics and keep the one we want.

At the end of this script, we got a new file create, *all_images.txt*


## 3/ Find the useless images

This task is realised in **partTwo.py**. Juste a simple function that have two arguments, the two lists (all_images and used images). 
This function return an array composed by all the useless pics.


## 4/ Create a SQL script wich delete only useless pics & create a new folder wich keep only the pics you want

This [article](https://www.h3xed.com/web-development/how-to-bulk-delete-all-images-in-wordpress-media-library-and-database) helps me understand where and how you can delete images in the DB. But I recommand to play a little bit with it in local for a better undestanding.

Here is the script that you have to run. It is called partFinal.py and it create two things : 
- script.sql wich is the file that you will run in your database.
- a new uploads directory wich contain only the used images called new_uploads.

## Manual / how to use it

To run **partFinal.py** you need your uploads folder (from your Wordpress) and the list of all the pics that you want to keep, name this file : *used_images.txt*.
If you want to try, you can find an **uploads** folder and a **used_images.txt** for you.

:warning: Do not forget to backup your Wordpress before do anything
