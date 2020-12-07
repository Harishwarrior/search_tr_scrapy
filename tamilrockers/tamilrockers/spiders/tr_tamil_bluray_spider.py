import scrapy

from .base_tr_spider import BaseTRSpider

#  scrapy crawl tr_bluray -a title='Kannum kannum' -a result='kk.json'


class TamilBluRaySpider(BaseTRSpider):
    name = "tr_bluray"

    def start_requests(self):
        self.process_title()

        urls = ['https://tamilrockers.ws/index.php/forum/116-tamil-bluray-hd-movies/page-1?'
                'prune_day=100&sort_by=Z-A&sort_key=start_date&topicfilter=all']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('tr[class="__topic  expandable"]'):
            movie_title = quote.css(
                'td.col_f_content h4 a span::text').extract()[0]
            movie_url = quote.css(
                'td.col_f_content h4 a::attr(href)').extract()[0]

            # Process movie title and url
            self.parse_movie_url(movie_title, movie_url)

        np = response.css('li.next a::attr(href)').get()
        if np is not None:
            next_page = response.urljoin(np)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            # This section will be executed only once.
            # When there are no further page to crawl we will dump the results that we got so far into
            # json file
            self.write_result_to_file()
