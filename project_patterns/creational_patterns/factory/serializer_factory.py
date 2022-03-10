import importlib


class SerializerFactory:
    "Class to handle serializers"

    @classmethod
    def serializer(cls, obj: object, format: str):
        module = importlib.import_module("project_patterns.creational_patterns.factory")
        serializer_obj = getattr(module, f'{format}Serializer')
        instance = serializer_obj()
        obj.serialize(instance)
        return instance.to_str()
