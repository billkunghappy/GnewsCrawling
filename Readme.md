# Crawl news from google news. A quick guide.
> We are using the Gnews package and include some basic scripts. You can follow the instructions on the original github page, too.
## Getting started
**From the original github page, you can download the package using 'pip install gnews' but this will download the old package which have several bugs.**
**Install the package using git clone instead.**
	1. Clone the repository https://github.com/ranahaani/GNews.git
	2. Run 'pip install ./Gnews'
	3. Install newspaper3k by 'python3 -m pip install newspaper3k'
	4. You're set!
## Scripts
1. RetrieveNewsByKeyword.py
> This file is to retrieve news and its article from a list of keywords in a specific time period.
> Run: 'python3 RetrieveNewsByKeyword.py'
> Example output format:
'''
[
  {
    "source_url": "https://news.google.com/rss/articles/CBMigQFodHRwczovL3d3dy5uaWguZ292L25ld3MtZXZlbnRzL25ld3MtcmVsZWFzZXMvaW52ZXN0aWdhdGlvbmFsLWNoYWRveDEtbmNvdi0xOS12YWNjaW5lLXByb3RlY3RzLW1vbmtleXMtYWdhaW5zdC1jb3ZpZC0xOS1wbmV1bW9uaWHSAQA?oc=5&hl=en-US&gl=US&ceid=US:en",
    "source_name": "National Institutes of Health (.gov)",
    "title": "Investigational ChAdOx1 nCoV-19 vaccine protects monkeys ... - National Institutes of Health (.gov)",
    "publish_time": "Fri, 15 May 2020 07:00:00 GMT",
    "content": [
      "Investigational ChAdOx1 nCoV-19 vaccine protects monkeys against COVID-19 pneumonia",
      "Study provided data for clinical testing to commence.",
      "NIAID",
      "What",
      "A single dose of ChAdOx1 nCoV-19, an investigational vaccine against SARS-CoV-2, has protected six rhesus macaques from pneumonia caused by the virus, according to National Institutes of Health scientists and University of Oxford collaborators. SARS-CoV-2 is the virus that causes COVID-19. The researchers posted their data to the preprint server bioRxiv. The findings are not yet peer-reviewed but are being shared to assist the public health response to COVID-19. Based on these data, a Phase 1 trial of the candidate vaccine began on April 23 in healthy volunteers in the United Kingdom.",
      "The vaccine was developed at the University of Oxford Jenner Institute. It uses a replication-deficient chimpanzee adenovirus to deliver a SARS-CoV-2 protein to induce a protective immune response. ChAdOx1 has been used to develop investigational vaccines against several pathogens, including a closely related coronavirus that causes Middle East respiratory syndrome (MERS). The scientists quickly adapted the platform to SARS-CoV-2 when the first cases of COVID-19 emerged. They showed that the vaccine rapidly induced immune responses against SARS-CoV-2 in mice and rhesus macaques. They then conducted vaccine efficacy testing on the macaques at NIAID\u2019s Rocky Mountain Laboratories (RML) in Hamilton, Montana. Six animals that received the investigational vaccine 28 days before being infected with SARS-CoV-2 were compared with three control animals that did not receive the vaccine. The vaccinated animals showed no signs of virus replication in the lungs, significantly lower levels of respiratory disease and no lung damage compared to control animals.",
      "Oxford University has entered into a partnership with UK-based global biopharmaceutical company AstraZeneca for the further development, large-scale manufacture and potential distribution of the vaccine.",
      "Article",
      "N van Doremalen et al. Single dose ChAdOx1 nCoV-19 vaccination reduces SARS-CoV-2 replication and prevents pneumonia in rhesus macaques.",
      "Who",
      "Vincent Munster, Ph.D., chief of the Virus Ecology Unit in NIAID\u2019s Laboratory of Virology, is available to comment on this study.",
      "Contact",
      "To schedule interviews, please contact Ken Pekoc, (301) 402-1663, kpekoc@niaid.nih.gov.",
      "This press release describes a basic research finding. Basic research increases our understanding of human behavior and biology, which is foundational to advancing new and better ways to prevent, diagnose, and treat disease. Science is an unpredictable and incremental process \u2014 each research advance builds on past discoveries, often in unexpected ways. Most clinical advances would not be possible without the knowledge of fundamental basic research.",
      "NIAID conducts and supports research\u2014at NIH, throughout the United States, and worldwide\u2014to study the causes of infectious and immune-mediated diseases, and to develop better means of preventing, diagnosing and treating these illnesses. News releases, fact sheets and other NIAID-related materials are available on the NIAID website.",
      "About the National Institutes of Health (NIH): NIH, the nation's medical research agency, includes 27 Institutes and Centers and is a component of the U.S. Department of Health and Human Services. NIH is the primary federal agency conducting and supporting basic, clinical, and translational medical research, and is investigating the causes, treatments, and cures for both common and rare diseases. For more information about NIH and its programs, visit www.nih.gov.",
      "NIH\u2026Turning Discovery Into Health\u00ae"
    ],
    "img": [
      "https://www.nih.gov/sites/default/files/styles/featured_media_breakpoint-medium/public/news-events/news-releases/2020/20200515-covid.jpg?itok=R9dwxvHV&timestamp=1589573345",
      "https://www.nih.gov/sites/default/files/news-events/news-releases/2020/20200515-covid.jpg",
      "https://news.google.com/sites/all/themes/nih/images/nih-logo-color.png"
    ]
  }
]
'''
2. RetrieveNewsArticleByURL.py
> This file is to retrieve news and its article from a list of urls.
> Using Multi-Processing can speed it up a lot. However, query the server rapidly can lead to ip being banned. We recommend setting the process number to **<= 4**.
> Run: 'python3 RetrieveNewsArticleByURL.py URLs.json'

