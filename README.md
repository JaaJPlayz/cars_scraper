# carScraper

## Official repository
<a href="https://github.com/JaaJPlayz/cars_scraper">cars_scraper</a> on Github

## Stacks
- Python 3.8+
## Project description
<p>carScrapper is a tool designed to scrape car images for a Trump Cards Game.
It uses the <a href='https://images.google.com/'>Google Images</a> website to search for cars and download their images.
</p>

## Project details
The app reads the car names from a JSON file called `cars_data.json` and searches for them on Google Images.
It then uses **BeautifulSoup** to scrape the given URL and retrieve the img src from the first image found. After that, it downloads the image and saves it to the `images` folder naming them with the car name and adding the `.jpg` extension.

<details>
<summary>
<strong>Beautiful Soup</strong>
</summary>
  <p> Found at: <a href ='https://code.launchpad.net/beautifulsoup/'>Beautiful Soup</a></p>
  <p> Source can be found <a href ='https://git.launchpad.net/beautifulsoup/'>here</a></p>
  <p> Documentation can be found <a href ='https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html'>here</a></p>
</details>

## Requirements
<p>Python 3.8+</p>
<p>Beautiful Soup ^4.12.3</p>

## Getting started
* Install dependencies
```
- Create your virtual environment with: python3 -m venv venv
- Activate your virtual environment with: source .venv/bin/activate
- Install the dependencies with: pip install -r dev-requirements.txt
```
* Build and run
```
python3 src/index.py
```
## To-do
- Try to download more than one image
- Try to download the highest resolution image
- Add a GUI
