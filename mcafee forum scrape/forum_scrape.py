"""
Forum Scrapper

Author: Guiyang

Go to the mcafee forum and scape all the comments with category and date.

"https://community.mcafee.com/t5/forums/recentpostspage/post-type/thread/category-id/mcafee-consumer/page/1"
"""
import time
import csv
import urllib
from BeautifulSoup import BeautifulSoup

class data_scrapper(object):
    def __init__(self):
        base_url = "https://community.mcafee.com/t5/forums/recentpostspage/post-type/thread/category-id/mcafee-consumer/page/"
        self.url_list = [base_url + str(i) for i in xrange(1, 101)]

    def extract_title(self, url):
        f = urllib.urlopen(url)
        html = f.read()
        list_comments_url = []
        soup = BeautifulSoup(html)
        for each_a in soup.findAll('a', {"class": "page-link lia-link-navigation lia-custom-event"}, href=True):
            list_comments_url.append("https://community.mcafee.com" + each_a['href'])
        return list_comments_url

    def extract_page(self, url):
        f = urllib.urlopen(url)
        html = f.read()

        # category
        path_start = html.find('"path" : ')
        path_end = html.find('"', path_start + 11)
        path = html[path_start + 10:path_end]

        # language
        lg_start = html.find('"profile.language" : ')
        lg_end = html.find('"', lg_start + 22)
        language = html[lg_start + 22:lg_end]

        # date
        dt_start = html.find('<span class="local-date">')
        dt_end = html.find("</span>", dt_start)
        date = html[dt_start:dt_end]

        if not date:
            dt_start = html.find('2018-')
            date = html[dt_start:dt_start + 10]

        # content
        content = None
        soup = BeautifulSoup(html)
        for div in soup.findAll('div', {"class": "lia-message-body-content"}):
            content = div.getText()

        product, title = self.path_parser(path)
        if product and title and language and date and content:
            return [product, title, date, language, content]
        else:
            return None

    def path_parser(self, path_string):
        start = path_string.find("Board:")
        end = path_string.find("/", start)
        product = path_string[start + 6: end]

        start = path_string.find("Message:")
        title = path_string[start + 8:]

        return product, title

    def cleanup(self, msg):
        soup = BeautifulSoup(msg)
        return soup.getText().encode('utf-8').strip()

    def store_to_file(self, msg_list, location):
        with open(location, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(msg_list)

    def run(self):
        for url in self.url_list:
            print "extract from: ", url
            for page in self.extract_title(url):
                print "extract page: ", page
                # [product, title, content, date, language]
                page_content = self.extract_page(page)
                if page_content:
                    try:
                        cleaned_data = [self.cleanup(i) for i in page_content]
                        self.store_to_file(cleaned_data, "C:\Users\ghan\Documents\data.csv")
                        print "data wrote:", cleaned_data
                        time.sleep(10)
                    except Exception as e:
                        print "scrape failed: {}".format(e)
                        pass


if __name__ == "__main__":
    A = data_scrapper()
    A.run()