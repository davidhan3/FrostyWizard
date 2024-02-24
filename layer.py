from layered_attributes import LayeredEffectDefinition, EffectOperation


class Layer:
    effects = []

    def __init__(self, attribute: str):
        self.base_value = 0
        self.effects = []
        self.attribute = attribute

    def set_base(self, new_base: int) -> None:
        self.base_value = new_base

    def get_value(self) -> int:
        value = self.base_value

        val: LayeredEffectDefinition
        for val in self.effects:
            if val.Operation == EffectOperation.Set:
                value = val.Modification
            elif val.Operation == EffectOperation.Add:
                value += val.Modification
            elif val.Operation == EffectOperation.Subtract:
                value -= val.Modification
            elif val.Operation == EffectOperation.Multiply:
                value *= val.Modification
            elif val.Operation == EffectOperation.BitwiseAnd:
                value &= val.Modification
            elif val.Operation == EffectOperation.BitwiseOr:
                value |= val.Modification
            elif val.Operation == EffectOperation.BitwiseXor:
                value ^= val.Modification

        return value

    def add_effect(self, effect: LayeredEffectDefinition) -> None:
        spot = -1
        for i in range(len(self.effects)):
            if self.effects[i].Layer > effect.Layer:
                spot = i
                break

        if spot == -1:
            self.effects.append(effect)
        else:
            self.effects.insert(spot, effect)

        return

    def clear(self) -> None:
        self.effects.clear()

    def size(self):
        return len(self.effects)

    def to_string(self):
        to_string = ""

        definition: LayeredEffectDefinition
        for effect in self.effects:
            to_string += "[Op={}, Mod={}, Layer={}] ".format(effect.Operation, effect.Modification, effect.Layer)

        return None if to_string == "" else to_string
