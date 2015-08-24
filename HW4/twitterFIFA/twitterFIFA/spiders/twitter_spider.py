__author__ = 'Safyre'
#https://twitter.com/search?q=%23FIFAWWC%20%23GER%20OR%20%23USA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CAN%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20%20lang%3Aen%20since%3A2015-06-06%20until%3A2015-07-07
import scrapy
from twitterFIFA.items import TwitterfifaItem
import os
import time
import re
from scrapy.crawler import CrawlerProcess

class FIFASpider(scrapy.Spider):
    name = "tFIFA"
    allowed_domains = ["twitter.com"]

    start_url =  "https://twitter.com/search?q=%23FIFAWWC%20%23GER%20OR%20%23USA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CAN%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23CHN%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23THA%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-06%20until%3A2015-07-07&src=typd&lang=en"
    start_urls = [start_url]

    # Create string variables for reloading new tweets by tweet ids
    max_tweet_id = ""
    min_tweet_id = ""
    id_range = ""
    append_tag_str = '&max_position=TWEET-'

    page_count = 0

    #def parse(self, response):
    #    for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
    #        url = response.urljoin(href.extract())
    #        yield scrapy.Request(url, callback=self.parse_dir_contents)

    def load_page(self, response):
        #min_idx = str(20+(20*self.page_count))
        self.max_tweet_id = response.xpath("//div[contains(@class, 'original-tweet')]/@data-tweet-id").extract()[0]
        self.min_tweet_id = response.xpath("//div[contains(@class, 'original-tweet')]/@data-tweet-id").extract()[-1]
        self.id_range = self.min_tweet_id + '-' + self.max_tweet_id
        return self.id_range

    def parse(self, response):
        self.id_range = self.load_page(response)
        print "range of ids ", self.id_range, "\n"
        # add the range to create a new url
        next_url = self.start_url + self.append_tag_str + self.id_range

        print "Next URL to scrape is: " + next_url
        time.sleep(2)
        self.page_count += 1
        print "On Page... ", self.page_count

        for sel in response.css('.stream-container'):
            # Tweets are in descending order
            # Create an item for each group of 20 tweets that loads
            tweet_texts = ""
            tweet_div = sel.xpath("//div[contains(@class, 'original-tweet')]")
            for i in range(len(tweet_div)):
                item = TwitterfifaItem()

                # Tweet text is split across multiple rows, need to concat them all.
                text_tree_div = tweet_div[i].xpath("//div[@class='content']/p[contains(@class, 'js-tweet-text')]")[i]
                tweet_text = ""
                for text in text_tree_div.xpath('descendant-or-self::text()').extract():
                    tweet_text += text.encode('utf8')
                #print tweet_text, '\n'
                item['tweet_texts']    = tweet_text

                ## grab the dates for each tweet
                tweet_date = tweet_div.xpath(".//div[@class = 'content']/div[@class = 'stream-item-header']/small[@class = 'time']/a[contains(@class, 'tweet-timestamp')]/@title").extract()[i]
                #print tweet_date
                item['tweet_date'] = tweet_date

                user_id    = tweet_div.xpath("//@data-screen-name").extract()[i]
                print user_id.encode('unicode-escape')
                item['tweet_userid'] = user_id
                yield item

        yield scrapy.Request(url=next_url, callback=self.parse)



        #for sel in response.css('.stream-container'):
            # Tweets are in descending order
            # Create an item for each group of 20 tweets that loads
        #    item = TwitterfifaItem()
        #    item['page_texts']    = sel.xpath("//p[contains(@class, 'TweetTextSize') and contains(@class, 'js-tweet-text') and contains(@class, 'tweet-text')]/text()").extract()
        #    item['page_linktxts'] = sel.xpath("//p[contains(@class, 'TweetTextSize') and contains(@class, 'js-tweet-text') and contains(@class, 'tweet-text')]/a/b/text()").extract()
        #    item['page_links']    = sel.xpath("//p[contains(@class, 'TweetTextSize') and contains(@class, 'js-tweet-text') and contains(@class, 'tweet-text')]/a/@href").extract()
                #tweet_texts           = sel.xpath("//p[contains(@class, 'js-tweet-text')]/text()").extract()
                #tweet_texts  = sel.xpath("//p[contains(@class, 'js-tweet-text')]/descendant-or-self::text()").extract() #[i.replace(', ,', " ") for i in tweet_texts]
        #    tweet_texts = ""
        #    tweet_div = sel.xpath("//div[contains(@class, 'original-tweet')]")
        #    for i in range(len(tweet_div)):
        #        text_tree_div = tweet_div[i].xpath("//div[@class='content']/p[contains(@class, 'js-tweet-text')]")[i]
        #        tweet_text = ""
        #        for text in text_tree_div.xpath('descendant-or-self::text()').extract():
        #            tweet_text += text.encode('unicode-escape')
        #        print tweet_text
        #        tweet_texts += tweet_text + " ; "
        #    item['tweet_texts'] = tweet_texts
                #item['max_id']        = sel.xpath('//@data-max-position').extract()
                #item['min_id']        = sel.xpath('//@data-max-position').extract()
        #    item['page_dates']    = sel.xpath("//div/span[@class = 'metadata']/span/text()").extract()
        #    yield item
        #yield scrapy.Request(url=next_url, callback=self.parse)


    #def parse(self, response):
    #    filename = response.url.split("/")[-2] + '.html'
    #    with open(filename, 'wb') as f:
    #        f.write(response.body)

## run the Crawler from python script

#process = CrawlerProcess({
#    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#})
#process.crawl(FIFASpider)
#process.start()
