import scrapy

from .base_tr_spider import BaseTRSpider

#  scrapy crawl tr_dubbed -a title='Mission' -a result='d_mission.json'


class TamilDubbedSpider(BaseTRSpider):
    name = "tr_dubbed"

    def start_requests(self):
        self.process_title()

        urls = ['https://tamilblasters.vip/index.php?/forums/forum/9-dubbed-movies-bdrips-hdrips-dvdscr-hdcam-in-multi-audios/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('h4[class="ipsDataItem_title ipsContained_container"]'):
            movie_title = quote.css(
                'a span::text').extract()[0]
            movie_url = quote.css(
                'a::attr(href)').extract()[0]

            # Process movie title and url
            self.parse_movie_url(movie_title, movie_url)

          

        np = response.css('li.ipsPagination_next a::attr(href)').get()
        if np is not None:
            next_page = response.urljoin(np)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            # This section will be executed only once.
            # When there are no further page to crawl we will dump the results that we got so far into
            # json file
            self.write_result_to_file()
