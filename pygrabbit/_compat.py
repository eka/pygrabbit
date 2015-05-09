import six

if six.PY2:
    from urlparse import urljoin
if six.PY3:
    from urllib.parse import urljoin