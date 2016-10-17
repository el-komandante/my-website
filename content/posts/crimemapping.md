title: Mapping Crime Data with Python
date: 2016-06-24

<h1 class='post-title'>Mapping Crime Data with Python</h1>
<small>06.26.2016</small>

<h2>Introduction</h2>

Since beginning the journey of learning Python a few months ago, I've been trying to design a project that would give me an opportunity to learn more about web scraping and data analysis. An idea that came to mind was mapping crimes around Northwestern's campus using the Northwestern Police Department's crime reports. In their raw form, the page for each month is a series of horizontally-oriented tables which include the date, time, type, and address of each incident.


<h2>Scraping the Data</h2>

The data that I used was publicly available through the Northwestern Police Department's online crime log, Blotter. I made the decision to download the page for each month so that I would not have to request the pages each time I ran the program. Each incident is logged as a separate horizontally-oriented HTML table, which meant that I had to consolidate them. Fortunately, rather than parsing through each individual table using a library like pattern or BeautifulSoup, pandas has a read_html() function that converts any tables within an HTML document to a pandas DataFrame. After pivoting the axes to create a vertical table and saving the DataFrame as an Excel file, the data looked like this:

<div class='notebook-container'>
  <iframe class='notebook' src="https://s3.amazonaws.com/iframes00012/frames/data.html" style='height:565px;'></iframe>
</div>

<h2>Geocoding</h2>

There are several geocoding services that offer a limited number of API requests per day for free. I used <a href="https://geocod.io/">geocodio</a> and the <a href="https://geocoder.opencagedata.com/">OpenCage Geocoder</a>. I created a function that takes a dataframe containing a list of locations (as street addresses) and returns a list of tuples in the form (latitude, longitude).

<div class='notebook-container'>
  <iframe class='notebook' src='https://s3.amazonaws.com/iframes00012/frames/geocode.html' style='height:450px;'></iframe>
</div>

<h2>Mapping</h2>

<a href='https://github.com/python-visualization/folium'>Folium</a> is a Python wrapper for <a href='http://http://leafletjs.com/'>leaflet.js</a>, a JavaScript library for creating interactive maps. It has a clustered marker functionality that clusters GPS markers by location, which allows for quick and easy navigation of the map and prevents points from overlapping. When zoomed out, points are grouped by region and appear as the map is zoomed in. I decided to group the incidents by year to get some idea of how the locations of crime incidents were distributed over time. I wrote function to group the incidents by year and create a clustermap using their GPS coordinates.

<div class='notebook-container'>
  <iframe class='notebook' src='https://s3.amazonaws.com/iframes00012/frames/map.html' style='height: 1550px;'></iframe>
</div>

<h2>Conclusion</h2>
Looking at the map, most incidents are centered around campus and are more sparsely distributed throughout the residential area to the west. This sharp dropoff is likely the result of incidents further away from Northwestern's campus being handled by Evanston Police rather than Northwestern Police.
