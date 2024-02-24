from layered_attributes import LayeredEffectDefinition, EffectOperation


class Layer:
    effects = []

    def __init__(self, attribute: str):
        self.base_value = 0
        self.effects = []
        self.attribute = attribute

    """
    Sets the base value for the layer.
    """

    def set_base(self, new_base: int) -> None:
        self.base_value = new_base

    """
    Iterates over the layer and computes all effects into a single value.
    """

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

    """
    Adds an effect to the correct spot within the layer. This is done by iterating over the current effects and slotting
    the new effect in the appropriate sorted position
    """

    def add_effect(self, effect: LayeredEffectDefinition) -> None:
        if effect.Operation == EffectOperation.Set:
            self.add_effect_set(effect)
        else:
            self.add_effect_notset(effect)

    def add_effect_notset(self, effect: LayeredEffectDefinition) -> None:
        # Since a set operation overrides all effects before it there's no point in adding an effect before it
        if len(self.effects) > 0 and self.effects[0].Operation == EffectOperation.Set and self.effects[0].Layer > effect.Layer:
            return

        spot = -1
        for i in range(len(self.effects)):
            if self.effects[i].Layer > effect.Layer:
                spot = i
                break

        if spot == -1:
            self.effects.append(effect)
        else:
            self.effects.insert(spot, effect)

    def add_effect_set(self, effect: LayeredEffectDefinition) -> None:
        if effect.Operation != EffectOperation.Set:
            return # consider throwing an exception here since this should never happen.
        while len(self.effects) > 0:
            if self.effects[0].Layer > effect.Layer:
                self.effects.insert(0, effect)
                return
            else:
                self.effects.pop(0)
        self.effects.append(effect)

    """
    Clears all effects from the layer. Base value stays the same.
    """

    def clear(self) -> None:
        self.effects.clear()

    """
    Returns the number of effects in this layer.
    """

    def size(self):
        return len(self.effects)

    """
    to string, return none if layer is empty.
    """

    def to_string(self) -> str:
        to_string = ""

        definition: LayeredEffectDefinition
        for effect in self.effects:
            to_string += "[Op={}, Mod={}, Layer={}] ".format(effect.Operation, effect.Modification, effect.Layer)

        return None if to_string == "" else to_string
