import re
import logging
from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocators
from parser.book_parser import BookParser

logger = logging.getLogger('Scraping.all_books_page')

class AllBooksPage:
    def __init__(self, page_contents):
        logger.debug('Parsing page content with BeautifulSoup HTML Parser')
        self.soup = BeautifulSoup(page_contents, 'html.parser')

    @property
    def books(self):
        logger.debug(f"Finding all books in the page using `{AllBooksPageLocators.BOOKS}`.")
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        logger.info(f"Found number of catalogue pages available: `{content}`.")
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: `{pages}`.')
        return pages
