#!/bin/bash
cd scraper-daemon

source ./venv/bin/activate

cd src/Share_scrapy/Share_scrapy/spiders

echo "-------------------------------------: Start Weekly"
scrapy runspider share_spider.py -a category="Manufacturing" -a time_val="W"
echo "-------------------------------------: Completely Weekly"
