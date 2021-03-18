import abc


class ErrorMeta(abc.ABCMeta, type(Exception)):
    ...
