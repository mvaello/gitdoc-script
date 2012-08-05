from  bs4 import BeautifulSoup
import urllib2

# Getting all links from http://git-scm.com/book/es

f = urllib2.urlopen('http://git-scm.com/book/es')
html_doc = f.read()

soup = BeautifulSoup(html_doc)

# Fetching TOC links and storing links into a list
def fetch_links(s):
    links = []
    for line in s.find("ol", {"class": "book-toc"}).find_all('a'):
        links.append('http://git-scm.com'+ line.get('href'))

    return links

# Trimming unnecesary html tags in the chapter
def trim_chapter(c):
    trim = c.find(id="nav").decompose()
    return c.find(id="content")

# Getting content of each chapter
def fetch_chapter_content(s):
    chapter = []
    for content in fetch_links(s):
        nf = urllib2.urlopen(content)
        #chapter = BeautifulSoup(nf.read())
        print type(fetch_links)
        chapter.append(trim_chapter(BeautifulSoup(nf.read())))
        return chapter

print fetch_chapter_content(soup)

# def build_book(file_format):
#     print get_chapter_content()
