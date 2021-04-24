__all__ = ['ManagedErrorMixin',
           'ManageClass']

import types
from typing import Callable, Optional, Type, Union

from .cli_exit import *
from .format import *
from .status import *


class ManagedErrorMixin(BaseFormattedErrorMixin, EncodedErrorMixin, ExitCLIErrorMixin,
                        metaclass=ErrorMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# TODO : functools -> wraps ?
class ManageClass:

    def __new__(cls, decorated_cls: Optional[type] = None, error_formatter_cls: Type[BaseFormattedErrorMixin] = FormattedErrorMixin,
                encoded_error_status: Optional[ErrorStatus] = None) -> Union[type, Callable[[Optional[type]], type]]:
        class DecoratedManagedErrorAPIMixin(error_formatter_cls, ManagedErrorMixin):

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            if encoded_error_status is not None:
                @staticmethod
                def get_error_status() -> ErrorStatus:
                    return encoded_error_status

        def create_managed_cls(unmanaged_cls: type) -> type:
            managed_class_namespace = {
                '__module__': __name__ if unmanaged_cls.__module__ is None else unmanaged_cls.__module__,
            }

            user_attrs_to_copy = {attr_name: attr_val for (attr_name, attr_val) in unmanaged_cls.__dict__.items() if not (attr_name.startswith('__') and attr_name.endswith('__'))}
            managed_class_namespace.update(user_attrs_to_copy)

            managed_class = types.new_class(unmanaged_cls.__qualname__,
                                            bases=(DecoratedManagedErrorAPIMixin, unmanaged_cls),
                                            kwds={'metaclass': ErrorMeta},
                                            exec_body=lambda ns: ns.update(managed_class_namespace))

            def __init__(self, *args, **kwargs):
                super(managed_class, self).__init__(*args, **kwargs)

            setattr(managed_class, '__init__', __init__)

            return managed_class

        if decorated_cls is not None:
            return create_managed_cls(decorated_cls)
        else:
            def wrapper(wrapped_decorated_cls):
                return ManageClass(wrapped_decorated_cls, error_formatter_cls, encoded_error_status)

            return wrapper
