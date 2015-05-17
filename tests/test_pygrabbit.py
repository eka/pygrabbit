from functools import partial
import pytest
import vcr
from pygrabbit import PyGrabbit


use_cassette = partial(vcr.use_cassette, record_mode='new_episodes')


class TestPyGrabbitTitle:
    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_title_from_url(self):
        g = PyGrabbit('http://www.drudgereport.com')
        assert g.title.startswith('DRUDGE REPORT')

    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_title_from_og(self):
        g = PyGrabbit('http://ogp.me/')
        assert g.title == 'Open Graph protocol'

    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_title_twitter_card(self):
        g = PyGrabbit('https://dev.twitter.com/docs/cards/types/summary-card')
        assert g.title == 'Summary Card'


class TestPyGrabbitDescription:
    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_description_from_og(self):
        g = PyGrabbit('http://ogp.me/')
        assert g.description == "The Open Graph protocol enables any web page to become a rich object in a social graph."

    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_description_from_twitter_card(self):
        g = PyGrabbit("https://dev.twitter.com/docs/cards/types/summary-card")
        assert g.description == "The Summary Card can be used for many kinds of web content, from blog posts and news articles, to products and restaurants. It is designed to give the reader a preview of the content before clicking through to your website."

    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_description_from_meta(self):
        g = PyGrabbit("http://moz.com/learn/seo/meta-description")
        assert g.description == "Get SEO best practices for the meta description tag, including length and content."


class TestPyGrabbitImages:
    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_return_array(self):
        g = PyGrabbit("http://www.google.com")
        assert type(g.images) == list

    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_only_images_from_og(self):
        g = PyGrabbit("http://ogp.me/")
        assert g.images[0] == "http://ogp.me/logo.png"
        assert len(g.images) == 1

    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_return_images_from_twitter_card(self):
        g = PyGrabbit("http://momwitha.com/2013/08/having-fun-with-pictures-at-google-headquarters/")
        assert g.images[0] == "http://momwitha.com/wp-content/uploads/2013/08/Rita-in-Google-Phonebooth1.jpg"
        assert len(g.images) == 1

    # NOTE: Amazon html is a bitch
    # @vcr.use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml', record_mode='new_episodes')
    # def test_main_image_with_id_amazon(self):
    #     g = PyGrabbit.url("http://www.amazon.com/gp/product/0975277324")
    #     import ipdb;ipdb.set_trace()
    #     assert g.images[0] == "http://ecx.images-amazon.com/images/I/61dDQUfhuvL._SX300_.jpg"
    #     assert len(g.images) == 1

    @use_cassette('fixtures/vcr_cassettes/pygrabbit.yaml')
    def test_return_images_from_global_img(self):
        g = PyGrabbit("http://elixir-lang.org/")
        assert g.images[0] == "http://elixir-lang.org/images/contents/home-code.png"
        assert len(g.images) == 1

