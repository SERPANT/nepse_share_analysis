#!/bin/bash
cd scraper-daemon

source ./venv/bin/activate

cd src/Share_scrapy/Share_scrapy/spiders

echo "-------------------------------------: Start Weekly"
scrapy runspider share_spider.py -a category="NonLifeInsurance" -a time_val="W"
echo "-------------------------------------: Completely Weekly"

echo "-------------------------------------: Start Monthly"
scrapy runspider share_spider.py -a category="NonLifeInsurance" -a time_val="M"
echo "-------------------------------------: Completely Monthly"

echo "-------------------------------------: Start Yearly"
scrapy runspider share_spider.py -a category="NonLifeInsurance" -a time_val="Y"
echo "-------------------------------------: Completely Yearly"

echo "-------------------------------------: Start Daily"
scrapy runspider share_spider.py -a category="NonLifeInsurance" -a time_val="D"
echo "-------------------------------------: Completely Daily"

echo "-------------------------------------: Start Quaterly"
scrapy runspider share_spider.py -a category="NonLifeInsurance" -a time_val="Q"
echo "-------------------------------------: Completely Quaterly"
