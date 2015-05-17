from ._compat import urljoin
import requests
from lxml import html


class PyGrabbit:
    headers = {'User-agent': 'PyGrabbit 0.1'}

    def __init__(self, url):
        self.url = url
        self._tree = None
        self._content = requests.get(url, headers=self.headers).text
        self._tree = html.fromstring(self._content)

    def _image_absolute_uri(self, image_path):
        return urljoin(self.url, image_path)

    def select(self, *queries):
        for query in queries:
            node = self._tree.xpath(query)
            if node:
                return node
        return []

    @property
    def title(self):
        text = self.select(
            "//meta[@property='og:title']/@content",
            "//meta[@name='twitter:title']/@content",
            )
        if text:
            return text[0].strip()

        res = self.select("//title")
        if res:
            res = res[0].text.strip()
            return res

    @property
    def description(self):
        text = self.select(
            "//meta[@property='og:description']/@content",
            "//meta[@name='description']/@content",
            )
        if text:
            return text[0].strip()

    @property
    def images(self):
        nodes = self.select(
            '//meta[@property="og:image"]/@content',
            '//meta[@name="twitter:image:src"]/@content',
            '//img[@id="main-image" or @id="prodImage"]/@src',
            "//img[not(ancestor::*[contains(@id, 'sidebar') or contains(@id, 'comment') or contains(@id, 'footer') or contains(@id, 'header')]) and ancestor::*[contains(@id, 'content')]]/@src",
            "//img[not(ancestor::*[contains(@id, 'sidebar') or contains(@id, 'comment') or contains(@id, 'footer') or contains(@id, 'header')])]/@src",
            "//img/@src",
            )
        return [self._image_absolute_uri(k) for k in nodes]
