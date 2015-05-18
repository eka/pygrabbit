from functools import update_wrapper


class cached_attribute(object):
    def __init__(self, getter):
        self.attr = getter.__name__
        self.getter = getter
        update_wrapper(self, getter)

    def __get__(self, instance, klass):
        if instance is None:
            return self
        rv = self.getter(instance)
        instance.__dict__[self.attr] = rv
        return rv
