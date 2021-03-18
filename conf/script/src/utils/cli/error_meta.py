import abc


class ManagedErrorMeta(abc.ABCMeta, type(Exception)):
    ...
