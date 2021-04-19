# Consider using the dataclasses package

# TODO : functools -> wraps ?
# From https://stackoverflow.com/a/33800620/2924010
def auto_repr(cls):
    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__repr__ = __repr__
    return cls


# TODO : functools -> wraps ?
# From https://stackoverflow.com/a/33800620/2924010
def auto_str(cls):
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % item[1] for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls
