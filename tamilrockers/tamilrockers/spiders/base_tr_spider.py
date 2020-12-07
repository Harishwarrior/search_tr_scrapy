from abc import ABC
from datetime import datetime
import scrapy

from .common_util import get_normalized_movie_title, write_to_json_file


class BaseTRSpider(scrapy.Spider, ABC):
    """
    Base class for searching based on movie title in tamil rockers.
    """
    complete_detail = {}
    title = ""
    result = ""

    def process_title(self):
        if self.title is not None and len(self.title) > 0:
            self.title = str(self.title).lower()

        if self.result is None or len(self.result) == 0:
            self.result = "{}".format(datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))

        if not self.result.endswith(".json"):
            self.result = "{}.json".format(self.result)

    def parse_movie_url(self, movie_title, movie_url):
        lower_case_title = str(movie_title).lower()
        n_movie_title = get_normalized_movie_title(lower_case_title)

        # Current movie does not match the search title
        if self.title is not None and self.title not in n_movie_title:
            return

        if n_movie_title not in self.complete_detail.keys():
            self.complete_detail[n_movie_title] = {}

        self.complete_detail[n_movie_title][movie_title] = movie_url

    def write_result_to_file(self):
        result_file = "{}".format(self.result)
        write_to_json_file(self.complete_detail, result_file)
        print("Result file is present at {}".format(result_file))
