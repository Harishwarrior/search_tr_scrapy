import scrapy

from .base_tr_spider import BaseTRSpider

#  scrapy crawl tr_english -a title='Mission' -a result='mission.json'


class EnglishHDRIPSpider(BaseTRSpider):
    name = "tr_english"

    def start_requests(self):
        self.process_title()

        urls = [
            'https://tamilrockers.ws/index.php/tutorials/category/6-english-hd-bd-rips-with-subtitle/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('tr[class="__article"]'):
            movie_title = quote.css('td.col_f_content h4 a::text').get()

            dummy_string = "- started "
            if dummy_string in movie_title:
                idx = movie_title.index(dummy_string)
                movie_title = str(movie_title[:idx]).strip()
            movie_url = quote.css('td.col_f_content h4 a::attr(href)').extract()[0]

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
