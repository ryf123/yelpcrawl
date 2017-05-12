import re
import urllib2
import csv


def get_url(url):
    # read from url
    try:
        response = urllib2.urlopen(url)
        return response.read()
    except:
        return ""



def extract_email(s):
    # extract email from string
    regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    m = re.findall(regex, s)
    return m if m else []


def read_csv(filename):
    with open(filename, 'r') as f:
        reader =  csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)
        return rows


def find_emails():
    filename = "./data/restaurant-94066.csv"
    urls = read_csv(filename)
    for url in urls:
        url = "http://"+url[0]
        emails = extract_email(get_url(url))
        if len(emails) > 0:
            print "email:" + "; ".join(emails)

if __name__ == '__main__':
    find_emails()