<h1><a id="SneakerBot_0"></a>SneakerBot</h1>
<p>Problem: Very often users need to wait for shoes to be available when they are out of stock.On big sneaker releases, shoes can sell out in under a second, and so scripts are much faster than manually going through the webpage.<br>
Solution:SneakerBot, written in Python allows users to directly checkout shoes as soon as they are available</p>
<ul>
<li>Url Generation:Generating URL based on model number and size</li>
<li>Data Acquisition: Scraping using Selenium Web Driver and Beautiful Soup to retrieve available sizes.</li>
<li>Add to Cart: Adding to cart along with checkout on popup banner</li>
<li>Checkout completed with shipping option onto payment now</li>
<li>Payment Complete</li>
<li>Testing</li>
</ul>

# Usage:

#### STEP ONE
```
$ git clone https://github.com/mridulghanshala/SneakerBot
$ cd SneakerBot
$ pip install selenium 
```

#### STEP TWO
Create a config.py file in the local directory that looks similar to this for each order you are placing.
```
keys = {
    "product_name":"stan-smith-shoes",
    "product_model":"M20324",
    "first_name": "John ",
    "last_name": "Fisher",
    "street_address": "Forest Hills Dr.",
    "city":"Quebec",
    "province_code":"ON",
    "shipping":"express",
    "email": "email@gmail.com",
    "phone_number": "6789998212",
    "zip_code": "N2L 4V9",
    "card_cvv": "666",
    "expiry":"02/2023",
    "card_number": "4094439936008035"
}
```
#### STEP THREE
You may have to download the correct chromedriver for you operating system (Linux/OSX/Windows), put the chromedriver the SneakerBot directory with the script.

chromdriver: http://chromedriver.chromium.org/downloads

#### STEP FOUR
```
$ python UrlGen.py
```

