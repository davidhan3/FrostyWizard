from layer import Layer
from layered_attributes import AttributeKey, LayeredEffectDefinition, LayeredAttributes


class LayeredAttributesImpl(LayeredAttributes):

    attributes = {}

    def __init__(self):
        for key in AttributeKey:
            self.attributes[key] = Layer(key.name)

    def set_base_attribute(self, attribute: AttributeKey, value: int) -> None:
        attribute[AttributeKey].base_value = value
        return

    def get_current_attribute(self, attribute: AttributeKey) -> int:
        if attribute in self.attributes:
            return self.attributes[attribute].get_value()
        return 0

    def add_layered_effect(self, effect: LayeredEffectDefinition) -> None:
        if effect.Attribute in self.attributes:
            layer = self.attributes[effect.Attribute]
            layer.add_effect(effect)
        return

    def clear_layered_effects(self) -> None:
        for key in AttributeKey:
            self.attributes[key].clear()
        return

    def print(self):
        for key in self.attributes:
            name = key
            to_string = self.attributes[key].to_string()
            print("{}: {}".format(name, to_string))
        print("")
