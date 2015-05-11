from ._compat import *
import requests
from lxml import html


headers = {'User-agent': 'PyGrabbit 0.1'}

class PyGrabbit:
    @staticmethod
    def url(url):
        g = PyGrabbit(url)
        return g

    def __init__(self, url):
        self.url = url
        self._tree = None
        try:
            res = requests.get(url, headers=headers)
            self._content = res.text
            self._tree = html.fromstring(self._content)
        except requests.ConnectionError:
            pass

    def _image_absolute_uri(self, image_path):
        return urljoin(self.url, image_path)

    @property
    def title(self):
        res = None

        if self._tree is not None:
            res = self._tree.xpath("//meta[@property='og:title']/@content")
            # TODO: DRY
            if res:
                res = res[0].strip()
                return res
            res = self._tree.xpath("//meta[@name='twitter:title']/@content")
            if res:
                res = res[0].strip()
                return res
            res = self._tree.xpath("//title")
            if res:
                res = res[0].text.strip()
                return res
        return res



    @property
    def description(self):
        res = None
        if self._tree is not None:
            res = self._tree.xpath("//meta[@property='og:description']/@content")
            if res:
                res = res[0].strip()
                return res
            res = self._tree.xpath("//meta[@name='description']/@content")
            if res:
                res = res[0].strip()
                return res
        return res

    @property
    def images(self):
        res = []

        if self._tree is not None:
            og = self._tree.xpath('//meta[@property="og:image"]/@content')

            twitter = self._tree.xpath('//meta[@name="twitter:image:src"]/@content')

            main = self._tree.xpath('//img[@id="main-image" or @id="prodImage"]/@src')

            global1 = self._tree.xpath("//img[not(ancestor::*[contains(@id, 'sidebar') or contains(@id, 'comment') or contains(@id, 'footer') or contains(@id, 'header')]) and ancestor::*[contains(@id, 'content')]]/@src")

            global2 = self._tree.xpath("//img[not(ancestor::*[contains(@id, 'sidebar') or contains(@id, 'comment') or contains(@id, 'footer') or contains(@id, 'header')])]/@src")

            global3 = self._tree.xpath("//img/@src")

            res = og or twitter or main or global1 or global2 or global3
            res = [self._image_absolute_uri(x) for x in res]
        return res


