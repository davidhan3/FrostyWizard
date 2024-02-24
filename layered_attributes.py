"""
GOAL:
   Create a class that implements the LayeredAttributes interface. Use your best
     judgement when it comes to design tradeoffs and implementation decisions.
   You may create any number of other classes to support your implementation.
   If you alter the given code, please maintain the intent of the original code
     and document why your alterations were necessary.
"""

from dataclasses import dataclass
from enum import Enum


class EffectOperation(Enum):
    Invalid = 0
    Set = 1
    """ Set a value, discarding any prior value. """
    Add = 2
    """ Add to the prior value. """
    Subtract = 3
    """ Subtract from the prior value. """
    Multiply = 4
    """ Multiply the prior value by the layered effect's Modification. """
    BitwiseOr = 5
    """ Perform a bitwise "or" operation. """
    BitwiseAnd = 6
    """ Perform a bitwise "and" operation. """
    BitwiseXor = 7
    """ Perform a bitwise "exclusive or" operation. """


class AttributeKey(Enum):
    NotAssessed = 0
    Power = 1
    Toughness = 2
    Loyalty = 3
    Color = 4
    Types = 5
    Subtypes = 6
    Supertypes = 7
    ManaValue = 8
    Controller = 9


@dataclass
class LayeredEffectDefinition:
    """
    Parameter struct for AddLayeredEffect(...)
    """

    # Which attribute this layered effect applies to.
    Attribute: AttributeKey

    # What mathematical or bitwise operation this layer performs.
    # See EffectOperation for details.
    Operation: EffectOperation

    # The operand used for this layered effect's Operation.
    # For example, if Operation is EffectOperation.Add, this is the
    # amount that is added.
    Modification: int

    # Which layer to apply this effect in. Smaller numbered layers
    # get applied first. Layered effects with the same layer get applied
    # in the order that they were added. (timestamp order)
    Layer: int


class LayeredAttributes:
    """
    Any object that implements this interface has a set of "base" attributes
    that represent the default state of that object. However, the game engine
    may apply one or more "layered effects" to modify those attributes. An
    object's "current" attributes are always equal to the base attributes
    with all layered effects applied, in the proper order. Any change to the
    base attribute or layered effects should immediately be reflected in the
    current attribute.
    """

    def set_base_attribute(self, attribute: AttributeKey, value: int) -> None:
        """
        Set the base value for an attribute on this object. All base values
        default to 0 until set. Note that resetting a base attribute does not
        alter any existing layered effects.

        Args:
            attribute: The attribute being set.
            value: The new base value.
        """
        pass

    def get_current_attribute(self, attribute: AttributeKey) -> int:
        """
        Return the current value for an attribute on this object. Will
        be equal to the base value, modified by any applicable layered
        effects.

        Args:
            attribute: The attribute being read.

        Returns:
            The current value of the attribute, accounting for all layered effects.
        """
        pass

    def add_layered_effect(self, effect: LayeredEffectDefinition) -> None:
        """
        Applies a new layered effect to this object's attributes. See
        LayeredEffectDefinition for details on how layered effects are
        applied. Note that any number of layered effects may be applied
        at any given time. Also note that layered effects are not necessarily
        applied in the same order they were added. (see LayeredEffectDefinition.Layer)

        Args:
            effect: The new layered effect to apply.
        """
        pass

    def clear_layered_effects(self) -> None:
        """
        Removes all layered effects from this object. After this call,
        all current attributes will be equal to the base attributes.
        """
        pass
