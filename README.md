<h1>Cloudcast</h1>
<p style="font-family:'Courier New'">This is another paragraph.</p>
<h2>Introduction</h2>
Cloudcast is a text-based game built on Python and MySQL, designed to promote education in data structures and algorithms. 
The game challenges players to match predicted weather statistics with actual recorded values using well-defined operations.</br></br>

The project is modularized into four subdivisions: <ol>
  <li><b>TUI</b> - Text User Interface</li>
  <li><b>Generator</b> - To create and populate datasets</li> 
  <li><b>Judge</b> - For scoring</li>
  <li><b>Toolkit</b> - For backend connectivity and helper functions</li>
</ol>

<h2>Objective</h2>
The primary goal of Cloudcast is to engage users in a fun and educational experience, fostering an understanding of data structures and algorithms. 
</br></br>
Players strive to optimize their scores through basic algorithmic knowledge, making the game suitable for enthusiasts interested in text-based gaming. 
</br></br>
Future upgrades may expand the audience through:<ul>
 <li>GUI implementation</li>
 <li>Additional themes</li>
 <li>Enhanced dataset generation</li></ul>

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
<li><b>Functions Definitions</b><ul>
  <li><ins>toolkit.update</ins>(week, day, stat, val):</br>
  &emsp; updates data at specified cell to ‘val’
  </li>
  <li><ins>toolkit.display</ins>(week, day=0, stat=0):</br>
  &emsp; displays the tables in a tabular format
  </li>
  <li><ins>toolkit.exit</ins>(maxdiff=0, scoreslate=0, offset=0, moves=0,save=False):</br>
  &emsp; saves the game if requested and cleans up the environment
</li>
  <li><ins>toolkit.load</ins>():</br>
  &emsp;	returns game save variables, or -1 if save file not found
</li>
  <li><ins>toolkit.get_tables</ins>():</br>
  &emsp; returns entire datasets
</li>
  <li><ins>toolkit.get_val</ins>(week, day, stat):</br>
  &emsp; returns predicted_value and recorded_value
</li>
  <li><ins>toolkit.Connect</ins>(pwd):</br>
  &emsp; establishes connection with database, with password as ‘pwd’
</li>
</ul>
</li>
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
This version of Cloudcast is a well-developed prototype. </br></br>
Contributions, feedback, and evaluations from experts and critics are welcome.</br></br>
Monetization is not currently viable within the project's scope.
</br></br>

At the end of the day, Cloudcast aims to spark interest in the field of data structures and computing algorithms among its players.
