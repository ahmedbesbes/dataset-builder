 <img src="https://storage.googleapis.com/ultralytics/logo/logoname1000.png" width="160">

# Introduction

This directory contains Flickr image-scraping software developed by Ultralytics LLC, and **is freely available for redistribution under the GPL-3.0 license**. For more information please visit https://www.ultralytics.com.

# Requirements

Python 3.7 or later with all of the `pip install -U -r requirements.txt` packages including:
- `flickrapi`

# Install
```bash
git clone https://github.com/ultralytics/flickr_scraper
cd flickr_scraper
pip install -U -r requirements.txt
```

# Use

1. Request a Flickr API key: https://www.flickr.com/services/apps/create/apply

2. Write your API key and secret in `flickr_scraper.py` L9-L10:
```python
key = ''
secret = ''
```

3. Search for up to `n` images, and optionally `--download`. URLs are printed to screen and downloaded images are saved in `flickr_scraper/images`. Note that image downloads may be subject to Flickr rate limits and other limitations. See https://www.flickr.com/services/developer/api/ for full information.

```bash
$ python3 flickr_scraper.py --search 'honeybees on flowers' --n 10 --download

0/10 https://live.staticflickr.com/1/393202_ce844e9fd4_o.jpg
1/10 https://farm8.staticflickr.com/7428/27138770446_6618c10ffb_b.jpg
2/10 https://live.staticflickr.com/4571/37795143414_8ccae77768_o.jpg
3/10 https://live.staticflickr.com/1732/27535176747_78b83536af_o.jpg
4/10 https://live.staticflickr.com/331/18765122504_ea8c9ea6ce_o.jpg
5/10 https://live.staticflickr.com/1919/44312457665_6f7b6c2c42_o.jpg
6/10 https://farm4.staticflickr.com/3597/3359921429_fc86a7519e_b.jpg
7/10 https://farm9.staticflickr.com/8643/15916201194_063f4b42d4_b.jpg
8/10 https://live.staticflickr.com/8045/29760999676_e71c938283_o.jpg
9/10 https://farm6.staticflickr.com/5814/22006609284_d36e206712_b.jpg
Done.
All images saved to /Users/glennjocher/PycharmProjects/flickr_scraper/images/honeybees_on_flowers/
```
<img src="https://user-images.githubusercontent.com/26833433/75074332-4792c600-54b0-11ea-8c98-22acf58ba8e7.jpg" width="">

# Cite

[![DOI](https://zenodo.org/badge/242235660.svg)](https://zenodo.org/badge/latestdoi/242235660)

# Contact

**Issues should be raised directly in the repository.** For additional questions or comments please email Glenn Jocher at glenn.jocher@ultralytics.com or visit us at https://contact.ultralytics.com.
