<p align="center">
  <a href="https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004" target="_blank">
    <img src="https://www.mobileapplaunchpad.com.eg/assets/frontend/images/udacity.png" width=72>
  </a>

  <h3 align="center">
  <a href="http://devjeanie.com/udacity/movietrailers/fresh_tomatoes.html" target="_blank">
  Project: Movie Trailer Website
  </a>
  </h3>

  <p align="center">
    Site generator hosting trailers from a list of favorite movies.
    <br>
  </p>
</p>

<br>
<img src="http://www.devjeanie.com/udacity/movietrailers/fmtw.PNG" style="width:100%">



## About
Done as part of the Udacity Full-Stack Web Development Nanodegree, for the first assigned project. The source code holds a list of movies and a function for generating a webpage that allows the user to view trailers from the input movies.  

## Quick start

<h4>Source Code</h4>
You can obtain the source code by forking from this repository. <br>
You may also download the files via this link: <br>
<a href="https://www.devjeanie.com/udacity/movietrailers/MovieTrailerWebsite.zip">
MovieTrailerWebsite.zip
</a>

<h4>Prerequisite</h4>
Before you can run the code, be sure that python is installed on the machine.<br>
You can install the software here:<br>
<a href="https://www.python.org/downloads/">
Python Install Link
</a>


## Directory Contents

Within the download you'll find the following directories and files, logically grouping common assets and providing both compiled and minified variations. You'll see something like this:

```
MovieTrailerWebsite/
├── entertainment_center.py
├── media.py
├── fresh_tomatoes.py
├── stylemod.css
├── README.md
└── images/
    ├── movie-icon-27.png
    └── notFound.png
```

## Navigating the Main File: entertainment_center.py

<b>entertainment_center.py</b> will be the main file of interest to the user.<br>
Attributes and Methods of interest to the user:
```
entertainment_center.py
├── movielist - string[]
├── print_movielist() - method
└── generate_site(movies, debug) - method
    ├── movies - string[]
    └── debug - boolean
```
<br>
<h3> Editing the list of Movies </h3>
<b>movielist</b> is a string array of movie titles that is used to search for and compile the data needed to make the website. This string array can be directly manipulated within the program, or via the python shell. As the official title found online will be used in the website, case will not matter when adding entries to the array. Nonexistent titles will throw an error, so the user will be able to correct or remove the offending entry.
<br><br>
To see the python methods available for array manipulation, click here:<br>
<a href="https://docs.python.org/3/library/array.html">python docs - array</a>
<br><br>

<h3> Printing the current list of Movies </h3>
<b>print_movielist()</b> is a quick provided means to check the current list of movies in the shell. Call it either within the python file in the IDLE IDE itself or in the python shell.
<br><br>

<h3> Generate the Trailer Website </h3>
<b>generate_site(movies,debug)</b> is the method used to generate the trailer website. It takes in a string array and an optional boolean set by default to False. Once generation of the site has completed, the site will open automatically.<br><br>
<b>movies</b> - string[]<br>
The array of movie titles to be used for generating the site. You may either use the default list that comes with the python file  movielist or add in another array of your own.
<br><br>
<b>debug</b> - boolean<br>
Whether the information collected during compilation of movie data should be printed to the console for tracing/debugging purposes. Will print out the collected Title, Plot Summary, Poster Image URL, and Trailer URL for each item in the inputted movies list.
<br><br>
You may view the generated webpage at anytime by clicking on the <b>fresh_tomatoes.html</b> that has spawned inside the main directory. The directory will now look something like this:<br>

```
MovieTrailerWebsite/
├── entertainment_center.py
├── media.py
├── fresh_tomatoes.py
├── stylemod.css
├── README.md
├── fresh_tomatoes.html        #NEW
├── entertainment_center.py    #NEW
├── media.py                   #NEW
├── fresh_tomatoes.py          #NEW
└── images/
    ├── movie-icon-27.png
    └── notFound.png
```
<hr>
Jeanie Choi | April 2017
<br><br>
