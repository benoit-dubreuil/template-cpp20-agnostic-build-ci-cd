import utils.meta_prog.generics.data


class GenericClassMixin(utils.meta_prog.generics.data.GenericsDataMixin):

    def has_generics(self) -> bool:
        return len(self.generics_by_type_vars) > 0
