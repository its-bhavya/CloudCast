<h1>Cloudcast</h1>
<h2>Introduction</h2>
Cloudcast is a text-based game built on Python and MySQL, designed to promote education in data structures and algorithms. 
The game challenges players to match predicted weather statistics with actual recorded values using well-defined operations. 

The project is modularized into four subdivisions: 
<ul>
  <li><b>TUI</b> - Text User Interface</li>
  <li><b>Generator</b> - To create and populate datasets</li> 
  <li><b>Judge</b> - For scoring</li>
  <li><b>Toolkit</b> - For backend connectivity and helper functions</li>
</ul>

<h2>Objective</h2>
The primary goal of Cloudcast is to engage users in a fun and educational experience, fostering an understanding of data structures and algorithms. </br>
Players strive to optimize their scores through basic algorithmic knowledge, making the game suitable for enthusiasts interested in text-based gaming. </br>
Future upgrades may expand the audience through:<ol>
 <li>GUI implementation</li>
 <li>Additional themes</li>
 <li>Enhanced dataset generation</li></ol>

<h2>Specifications</h2>
<ul>
  <li>Built on: Python 3.9 IDLE and MySQL 8.0</li>
  <li>Platform: Compatible with all platforms supporting Python 3.7+ and MySQL 8.0</li>
  <li>Features: Progress saving, dynamic game-state tracking, and real-time weather-inspired datasets</li>
  <li>Requirements: Python 3.7+, MySQL 8.0 (server only), and internet connection for API calls</li>
</ul>

<h2>Layout</h2>
<ol>
<li><b>main.py</b>
  <ul>
  <li>Main driver program and Text User Interface</li>
  <li>Calls functions from other modules</li>
  </ul>
</li>
<li><b>toolkit.py</b>
  <ul>
<li>Helper functions for main and scoring</li>
<li>Python-MySQL connectivity</li>
<li>Functions include data updates, table display, game saving/loading, and more</li>
  </ul>
</li>
<li><b>scoring.py</b>
  <ul>
<li>Evaluates optimization scores</li>
<li>Initializes judge variables and calculates scores based on player performance</li> 
  </ul>
</li>
<li><b>gen.py</b>
  <ul>
<li>Creates and populates datasets with randomized values from real-time API calls</li>
<li>Handles dataset generation in the MySQL database</li>
  </ul>
</li>
</ol>

<H2>How to Use</H2>
<ul>
  <li>Ensure Python 3.7+ and MySQL 8.0 are installed.</li>
  <li>Connect to the internet for API calls when starting a new game.</li>
  <li>Run main.py to launch the game.</li>
  <li>Follow on-screen instructions to play and save progress.</li>
</ul>

<h2>Future Upgrades</h2>
<ul>
  <li>Implementation of a GUI for a more user-friendly experience</li>
  <li>Addition of diverse themes to the weather system</li>
  <li>Increased user options for versatility</li>
  <li>Enhancement of the random dataset generator</li>
</ul>

<h2>Contribution and Feedback</h2>
This version of Cloudcast is a well-developed prototype. </br>
Contributions, feedback, and evaluations from experts and critics are welcome.</br>
Monetization is not currently viable within the project's scope.
</br></br>

At the end of the day, Cloudcast aims to spark interest in the field of data structures and computing algorithms among its players.
