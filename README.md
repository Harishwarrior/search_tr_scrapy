# search_tr

Search using movie name in tamilrockers website and this will returns the direct link.

This is for educational purpose only and is not a part of tamilrockers by any means.

## Clone the codebase to your local repository

`git clone https://github.com/Nandha1712/search_tr.git`

Code is written in python 3.x

## Read the tutorial to get to know about scrapy

<https://docs.scrapy.org/en/latest/intro/tutorial.html>

## Install the requirements to your system or virtual environment

use command `pip install -r requirements.txt`

you need to download and install visual studio build tools for scrapy to work

<https://visualstudio.microsoft.com/visual-cpp-build-tools/>

## VPN should be enabled if the website is blocked in your area

Navigate to _tamilrockers_ directory in the terminal `cd tamilrockers`

Title should be given within quotes `'sample title'`.

If `title` is not provided, crawl will fetch data for all movies.

Result parameter is optional. If not provided result will be saved as (timestamp).json

Run the command `scrapy crawl tr_bluray -a title='Kannum kannum' -a result='kk.json'`

Similarly to search for english movies:

Run the command `scrapy crawl tr_english -a title='Mission' -a result='mission.json'`

For searching tamildubbed movies:

Run the command  `scrapy crawl tr_dubbed -a title='Mission' -a result='d_mission.json'`

For searching tamil old movies:

Run the command  `scrapy crawl tr_old -a title='Old' -a result='old.json'`

## Contributions are welcomed
