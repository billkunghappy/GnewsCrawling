#https://github.com/ranahaani/GNews
from gnews import GNews
from tqdm import tqdm
import json
from datetime import timedelta,date
from multiprocessing import Process, Pool
import argparse

parser = argparse.ArgumentParser(description='Process arguments for crawling news')
parser.add_argument('--url_list', type=str, nargs='+',
                    help='A list of urls that you want to crawl. Should specify url_list or url_list_file.')
parser.add_argument('--url_list_file', type=str,
                    help='The file of url_list. Should be a txt file with a url in each line. Should specify url_list or url_list_file.')
parser.add_argument('--output_file', type=str, default="output.jsonl",
                    help='The output file. Default is output.jsonl')
parser.add_argument('--num_workers', type=int, default=1,
                    help='The number of multi-processing workers. Notice that rapid query to server may lead to IP being banned.')
parser.add_argument('--country', type=str, default="United States",
                    help='The country of the news. Not sure whether this feature really works, though. Check https://github.com/ranahaani/GNews#supported-countries for more details.')
parser.add_argument('--language', type=str, default="english",
                    help='The language of the news. Not sure whether this feature really works, though. Check https://github.com/ranahaani/GNews#supported-languages for more details.')

def get_article_by_url(url):
    google_news = GNews()
    article=google_news.get_full_article(url)
    # Can get article
    if not (article is None):
        # get a list of news from article to get meta_data
        news = google_news.get_news(article.title)
        news_dict = {
            "source_url": url,
            "source_name": news[0]['publisher']['title'] if len(news) > 0 else "",
            "title": article.title,
            "publish_time": news[0]['published date'] if len(news) > 0 else "",
            "content": [line for line in article.text.split("\n") if line != ""],
            "img": list(article.images)
        }
        # have_articles +=1
    else:
        news_dict = {
            "source_url": url,
            "source_name": "",
            "title": "",
            "publish_time": "", # Can't get it here
            "content": [],
            "img": []
        }
    return news_dict


def main():
    # Parse arguments
    args = parser.parse_args()
    # Check url_list and url_list_file
    assert (args.url_list is not None) or (args.url_list_file is not None), "Error. Should specify either 'url_list' or 'url_list_file' !!"
    assert not ((args.url_list is not None) and (args.url_list_file is not None)), "Error. Should only specify one of the 'url_list' or 'url_list_file' !!"
    # Load url_list
    if args.url_list is not None:
        url_list = args.url_list
    if args.url_list_file is not None:
        url_list = [line.strip() for line in open(args.url_list_file, "r").readlines()]
    # Final output list
    output_jsonl = []
    # For showing stats
    stats = {
        "Total News" : None,
        "Total News Sources" : None,
        "Total News w/ Article" : 0,
    }
    # Retrieving
    with Pool(args.num_workers) as p:
        output_jsonl = list(tqdm(p.imap(get_article_by_url, url_list)))
    # Write file
    with open(args.output_file, "w") as F:
        json.dump(output_jsonl, F, indent=2)
    # Showing stats
    source_set = set()
    for news in output_jsonl:
        if news['content'] != []:
            stats["Total News w/ Article"]+=1
        print(news['source_name'])
        source_set.add(news['source_name'])
    # Remove empty source
    source_set.remove("")
    stats["Total News"] = len(output_jsonl)
    stats["Total News Sources"] = len(source_set)
    for k, v in stats.items():
        print(f"{k}: {v}")
    

if __name__ == '__main__':
    main()
    