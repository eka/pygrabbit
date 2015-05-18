import pytest
import vcr
from pygrabbit import PyGrabbit


@pytest.fixture
def grab():
    @vcr.use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml',
                      record_mode='new_episodes')
    def make_grabbit(url):
        return PyGrabbit.url(url)
    return make_grabbit


class TestPyGrabbitTitle:
    def test_title_from_url(self, grab):
        g = grab('http://www.drudgereport.com')
        assert g.title.startswith('DRUDGE REPORT')

    def test_title_from_og(self, grab):
        g = grab('http://ogp.me/')
        assert g.title == 'Open Graph protocol'

    def test_title_twitter_card(self, grab):
        g = grab('https://dev.twitter.com/docs/cards/types/summary-card')
        assert g.title == 'Summary Card'


class TestPyGrabbitDescription:
    def test_description_from_og(self, grab):
        g = grab('http://ogp.me/')
        assert g.description == "The Open Graph protocol enables any web page to become a rich object in a social graph."

    def test_description_from_twitter_card(self, grab):
        g = grab("https://dev.twitter.com/docs/cards/types/summary-card")
        assert g.description == "The Summary Card can be used for many kinds of web content, from blog posts and news articles, to products and restaurants. It is designed to give the reader a preview of the content before clicking through to your website."

    def test_description_from_meta(self, grab):
        g = grab("http://moz.com/learn/seo/meta-description")
        assert g.description == "Get SEO best practices for the meta description tag, including length and content."


class TestPyGrabbitImages:
    def test_return_array(self, grab):
        g = grab("http://www.google.com")
        assert type(g.images) == list

    def test_only_images_from_og(self, grab):
        g = grab("http://ogp.me/")
        assert g.images[0] == "http://ogp.me/logo.png"
        assert len(g.images) == 1

    def test_return_images_from_twitter_card(self, grab):
        g = grab("https://dev.twitter.com/cards/types/summary-large-image")
        assert g.images[0] == "https://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3.png"
        assert len(g.images) == 1

    # NOTE: Amazon html is a bitch
    # @vcr.use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml', record_mode='new_episodes')
    # def test_main_image_with_id_amazon(self):
    #     g = PyGrabbit.url("http://www.amazon.com/gp/product/0975277324")
    #     import ipdb;ipdb.set_trace()
    #     assert g.images[0] == "http://ecx.images-amazon.com/images/I/61dDQUfhuvL._SX300_.jpg"
    #     assert len(g.images) == 1

    def test_return_images_from_global_img(self, grab):
        g = grab("http://elixir-lang.org/")
        assert g.images[0] == "http://elixir-lang.org/images/contents/home-code.png"
        assert len(g.images) == 1

