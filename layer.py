from layered_attributes import LayeredEffectDefinition, EffectOperation


class Layer:

    def __init__(self, attribute: str):
        self.base_value = 0
        self.effects = []
        self.attribute = attribute
        self.cached_value = self.base_value

    def set_base(self, new_base: int) -> None:
        """
        Sets the base value for the layer.

        Args:
            new_base: new base value for this layer
        """
        self.base_value = new_base
        self.cached_value = self.recalculate_value()

    def get_value(self) -> int:
        """
        Returns the pre-computed cache value for this layer.
        """
        return self.cached_value

    def recalculate_value(self) -> int:
        """
        Iterates over all effects and computes their value. This function is called every time a new effect is added or
        the base value changes to save on compute time.

        Returns:
            computed values of all effects in this layer
        """
        value = self.base_value

        effect: LayeredEffectDefinition
        for effect in self.effects:
            if effect.Operation == EffectOperation.Set:
                value = effect.Modification
            elif effect.Operation == EffectOperation.Add:
                value += effect.Modification
            elif effect.Operation == EffectOperation.Subtract:
                value -= effect.Modification
            elif effect.Operation == EffectOperation.Multiply:
                value *= effect.Modification
            elif effect.Operation == EffectOperation.BitwiseAnd:
                value &= effect.Modification
            elif effect.Operation == EffectOperation.BitwiseOr:
                value |= effect.Modification
            elif effect.Operation == EffectOperation.BitwiseXor:
                value ^= effect.Modification

        return value

    def add_effect(self, effect: LayeredEffectDefinition) -> None:
        """
        Adds an effect to this layer. Later functions will iterate over the effects list until it finds the proper position
        for the effect to be placed in. After adding the effect we will recompute the value of all the layers and save the
        cached value

        Args:
            effect: the effect to be added
        """
        spot = -1
        for i in range(len(self.effects)):
            if self.effects[i].Layer > effect.Layer:
                spot = i
                break

        if spot == -1:
            self.effects.append(effect)
        else:
            self.effects.insert(spot, effect)
        self.cached_value = self.recalculate_value()

    def clear(self) -> None:
        """
        Clears all effects from the layer. Assumption is that the base value stays the same.
        """
        self.effects.clear()
        self.cached_value = self.base_value

    def size(self) -> int:
        """
        Returns the number of effects in this layer. Used for testing currently but might be useful later.
        """
        return len(self.effects)

    def to_string(self) -> str:
        """
        to string, used for the console interaction.
        """
        to_string = "{}: base=[{}] effects: ".format(self.attribute, self.base_value)

        definition: LayeredEffectDefinition
        for effect in self.effects:
            to_string += "[Op={}, Mod={}, Layer={}] ".format(effect.Operation.name, effect.Modification, effect.Layer)

        return None if to_string == "" else to_string
