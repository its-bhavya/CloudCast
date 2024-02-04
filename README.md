<h1>Cloudcast</h1>
<h2>Introduction</h2>
Cloudcast is a text-based game built on Python and MySQL, designed to promote education in data structures and algorithms. 
The game challenges players to match predicted weather statistics with actual recorded values using well-defined operations. 

The project is modularized into four subdivisions: 
</br>
  -**TUI** (Text User Interface)
  -**Generator** (to create and populate datasets)
  -**Judge** (for scoring)
  -**Toolkit** (for backend connectivity and helper functions).

<h2>Objective</h2>
The primary goal of Cloudcast is to engage users in a fun and educational experience, fostering an understanding of data structures and algorithms. 
Players strive to optimize their scores through basic algorithmic knowledge, making the game suitable for enthusiasts interested in text-based gaming. 
Future upgrades may expand the audience through **GUI implementation**, **additional themes**, and **enhanced dataset generation**.

<h2>Specifications</h2>
<ul>
  <li>Built on: Python 3.9 IDLE and MySQL 8.0</li>
  <li>Platform: Compatible with all platforms supporting Python 3.7+ and MySQL 8.0</li>
  <li>Features: Progress saving, dynamic game-state tracking, and real-time weather-inspired datasets</li>
  <li>Requirements: Python 3.7+, MySQL 8.0 (server only), and internet connection for API calls</li>
</ul>

<h2>Layout</h2>
<ol>
<li>**main.py**
  <ul>
  <li>Main driver program and Text User Interface</li>
  <li>Calls functions from other modules</li>
  </ul>
</li>
<li>**toolkit.py**
  <ul>
<li>Helper functions for main and scoring</li>
<li>Python-MySQL connectivity</li>
<li>Functions include data updates, table display, game saving/loading, and more</li>
</li>
<li>**scoring.py**
  <ul>
<li>Evaluates optimization scores</li>
<li>Initializes judge variables and calculates scores based on player performance</li>
</li>
<li>**gen.py**
  <ul>
<li>Creates and populates datasets with randomized values from real-time API calls</li>
<li>Handles dataset generation in the MySQL database</li>
</li>
</ol>






How to Use
Ensure Python 3.7+ and MySQL 8.0 are installed.
Connect to the internet for API calls when starting a new game.
Run main.py to launch the game.
Follow on-screen instructions to play and save progress.
Future Upgrades
Implementation of a GUI for a more user-friendly experience
Addition of diverse themes to the weather system
Increased user options for versatility
Enhancement of the random dataset generator
Contribution and Feedback
This version of Cloudcast is a well-developed prototype. Contributions, feedback, and evaluations from experts and critics are welcome. Monetization is not currently viable within the project's scope.

At the end of the day, Cloudcast aims to spark interest in the field of data structures and computing algorithms among its players.