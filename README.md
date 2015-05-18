# PyGrabbit

From the entrails of 'Skynet' comes PyGrabbit, a very clever bastard
that will not stop at anything to fulfill its purpose.

PyGrabbit is a simple URL scrapper inspired by the Ruby Grabbit
https://github.com/rlarcombe/grabbit. It will try to return the
best image(s) that represent the content on a given web page or
not.

## Installation

With pip

    pip install pygrabbit

## Usage

    >>> from pygrabbit import PyGrabbit
    >>> g = PyGrabbit('http://www.redditpics.com/psbattle-olympic-shot-put,173917')
    >>> g.images
    ['http://walnutcreekcrossfit.com/wp-content/uploads/2012/10/ashton-eaton-shot-put3.jpg']
    >>> g.title
    'PsBattle: Olympic Shot Put'
    >>> g.description
    'A tribute to reddit'

## Note

PyGrabbit is under heavy development... not. But it's very green
indeed and in alpha stage, many things will be improved, so use
it at your own peril.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request


## Contributors

* this could be you!
