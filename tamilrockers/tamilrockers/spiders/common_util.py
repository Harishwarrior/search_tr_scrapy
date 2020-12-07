import re
import json

YEAR_REGEX_1 = r"\(([0-9_]{4})\)"
YEAR_REGEX_2 = r"\[([0-9_]{4})\]"


def split_year_from_title(title, regex_pattern=YEAR_REGEX_1):
    regex_match = re.search(regex_pattern, title)

    if regex_match is None:
        return title

    matched = regex_match.group(1)
    idx = title.index(matched)
    if idx < 1:
        return title

    normalized_title = title[0: idx - 1].strip()
    return normalized_title


def get_normalized_movie_title(complete_title_info):
    """
    Normalizes the movies title.
    If the movie title is
    Alaipayuthey (2000) [Tamil - 720p Untouched TRUE HD AVC - x264 - DD2.0 (224kbps) - 3.8GB - ESubs]

    This function will return Alaipayuthey
    This function will try to fetch the movie name by splitting on the year

    :param complete_title_info: Movie title to be normalized
    :return: the title of the movie alone by stripping the un necessary parts.
    """
    # Try to split the title based on year. If Year is enclosed by braces like (2012)
    normalized = split_year_from_title(complete_title_info, YEAR_REGEX_1)
    if normalized != complete_title_info:
        return normalized

    # If Year is enclosed by braces like [2012]
    normalized = split_year_from_title(complete_title_info, YEAR_REGEX_2)
    return normalized


def write_to_json_file(details, result_file):
    """
    Writes the result to a json file
    :param details: Contains the extracted information in the crawl process
    :param result_file: File path of the result file
    """
    json_result_file = open("{}".format(result_file), "w")
    try:
        json_result_file.write(json.dumps(details, indent=4, sort_keys=True))
        json_result_file.close()
    except Exception as exp:
        print("Error while writing results to file. {}".format(exp))
        json_result_file.close()
