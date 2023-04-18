#https://github.com/ranahaani/GNews
from gnews import GNews
from tqdm import tqdm
import json
from datetime import timedelta, datetime
import argparse

parser = argparse.ArgumentParser(description='Process arguments for crawling news')
parser.add_argument('--keywords', type=str, nargs='+',
                    help='A list of keywords that you want to crawl')
parser.add_argument('--start_date', type=str,
                    help='The starting date. Should be in the specific format --> Year/Month/Day')
parser.add_argument('--output_file', type=str, default="output.jsonl",
                    help='The output file. Default is output.jsonl')
parser.add_argument('--end_date', type=str,
                    help='The end date. Notice that the news on this day will also be crawled. Should be in the specific format --> Year/Month/Day')
parser.add_argument('--country', type=str, default="United States",
                    help='The country of the news. Not sure whether this feature really works, though. Check https://github.com/ranahaani/GNews#supported-countries for more details.')
parser.add_argument('--language', type=str, default="english",
                    help='The language of the news. Not sure whether this feature really works, though. Check https://github.com/ranahaani/GNews#supported-languages for more details.')



def main():
    # Parse arguments
    args = parser.parse_args()
    # Parse date and time
    # We will have to crawl data per day in this time period because the Gnews.get_news can at most get 100 news at a time.
    # I've checked that there're usually less than 100 news per day when we specify some keywords but may need to double check it for your case.
    start_date = datetime.strptime(args.start_date, "%Y/%m/%d")    
    end_date = datetime.strptime(args.end_date, "%Y/%m/%d")
    one_day = timedelta(days=1)
    # Maintain a set of URLs. There might be duplicate news being retrieved, we check whether the news url alread exist in this set.
    # If already exist(duplicate), we discard it.
    url_set = set()
    source_name_set = set()
    # Final output list
    output_jsonl = []
    # For showing stats
    stats = {
        "Total News" : None,
        "Total News Sources" : None,
        "Total News w/ Article" : 0,
    }
    # Start crawling news day by day
    for i in tqdm(range((end_date-start_date).days+1)):
        next_day = start_date + one_day
        # Crawl one day at a time
        google_news = GNews(start_date=(start_date.year, start_date.month, start_date.day), end_date=(next_day.year, next_day.month, next_day.day))
        google_news.country = args.country
        google_news.language = args.language
        # Crawl news by each keyword
        for keyword in args.keywords:
            # Retrieve a list of news based on current keyword
            covid_news = google_news.get_news(keyword)
            for news in covid_news:
                # Check whether each news already exist using url_set 
                if news['url'] in url_set:
                    continue
                # New news, update to url_set
                url_set.add(news['url'])
                source_name_set.add(news['publisher']['title'])
                # Try to get news article
                article=google_news.get_full_article(news['url'])
                # Check whether we can crawl the article
                if not (article is None): # Have article
                    news_dict = {
                        "source_url": news['url'],
                        "source_name": news['publisher']['title'],
                        "title": news["title"],
                        "publish_time": news['published date'],
                        "content": [line for line in article.text.split("\n") if line != ""],
                        "img": list(article.images)
                    }
                    stats["Total News w/ Article"] +=1
                else:
                    news_dict = {
                        "source_url": news['url'],
                        "source_name": news['publisher']['title'],
                        "title": news["title"],
                        "publish_time": news['published date'],
                        "content": [],
                        "img": []
                    }
                output_jsonl.append(news_dict)
        start_date = next_day
    # Write file
    with open(args.output_file, "w") as F:
        json.dump(output_jsonl, F, indent=2)
    print(f"Successfully write file to {args.output_file}")
    # Print stats
    stats["Total News"] = len(output_jsonl)
    stats["Total News Sources"] = len(source_name_set)
    for k, v in stats.items():
        print(f"{k}: {v}")
        
if __name__ == "__main__":
    main()
    