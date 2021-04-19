import abc
import types
from typing import Callable, Optional, Type, Union

import utils.error.cli_exit
import utils.error.format
import utils.error.meta
import utils.error.status


# noinspection PyAbstractClass
class ManagedErrorMixin(utils.error.format.BaseFormattedErrorMixin, utils.error.status.EncodedErrorMixin, utils.error.cli_exit.ExitCLIErrorMixin,
                        metaclass=utils.error.meta.ErrorMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# TODO : functools -> wraps ?
class ManageClass:

    def __new__(cls, decorated_cls: Optional[type] = None, error_formatter_cls: Type[utils.error.format.BaseFormattedErrorMixin] = utils.error.format.FormattedErrorMixin,
                encoded_error_status: Optional[utils.error.status.ErrorStatus] = None) -> Union[type, Callable[[Optional[type]], type]]:
        # noinspection PyAbstractClass
        class DecoratedManagedErrorAPIMixin(error_formatter_cls, ManagedErrorMixin):

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            if encoded_error_status is not None:
                @staticmethod
                def get_error_status() -> utils.error.status.ErrorStatus:
                    return encoded_error_status

        def create_managed_cls(unmanaged_cls: type) -> type:
            managed_class_namespace = {
                '__module__': __name__ if unmanaged_cls.__module__ is None else unmanaged_cls.__module__,
            }

            user_attrs_to_copy = {attr_name: attr_val for (attr_name, attr_val) in unmanaged_cls.__dict__.items() if not (attr_name.startswith('__') and attr_name.endswith('__'))}
            managed_class_namespace.update(user_attrs_to_copy)

            managed_class = types.new_class(unmanaged_cls.__qualname__,
                                            bases=(DecoratedManagedErrorAPIMixin, unmanaged_cls),
                                            kwds={'metaclass': utils.error.meta.ErrorMeta},
                                            exec_body=lambda ns: ns.update(managed_class_namespace))

            def __init__(self, *args, **kwargs):
                # noinspection PyArgumentList
                super(managed_class, self).__init__(*args, **kwargs)

            setattr(managed_class, '__init__', __init__)

            return managed_class

        if decorated_cls is not None:
            return create_managed_cls(decorated_cls)
        else:
            def wrapper(wrapped_decorated_cls):
                return ManageClass(wrapped_decorated_cls, error_formatter_cls, encoded_error_status)

            return wrapper
