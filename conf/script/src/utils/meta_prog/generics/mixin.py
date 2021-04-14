from utils.meta_prog.generics.data import GenericsData


class GenericClassMixin(GenericsData):

    def has_generics(self) -> bool:
        return len(self.generics_by_type_vars) > 0
