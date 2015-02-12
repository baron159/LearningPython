__author__ = 'Scott'

from urllib import request as req

loc = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=1&e=12&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'

def download_file(url):
    response = req.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

download_file(loc)
