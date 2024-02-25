import unittest

from layered_attributes import LayeredEffectDefinition, AttributeKey, EffectOperation, LayeredAttributes
from layered_attributes_impl import LayeredAttributesImpl


class TestLayerImpl(unittest.TestCase):
    power_add_5_layer_2 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Add,
                                                  Modification=5, Layer=2)
    power_sub_3_layer_1 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Subtract,
                                                  Modification=3, Layer=1)
    color_mul_18_layer_7 = LayeredEffectDefinition(Attribute=AttributeKey.Color, Operation=EffectOperation.Multiply,
                                                   Modification=18, Layer=7)
    color_add_4_layer_0 = LayeredEffectDefinition(Attribute=AttributeKey.Color, Operation=EffectOperation.Add,
                                                  Modification=4, Layer=0)
    mana_sub_8_layer_3 = LayeredEffectDefinition(Attribute=AttributeKey.ManaValue, Operation=EffectOperation.Subtract,
                                                 Modification=8, Layer=3)

    def test_interface_implementation(self):
        self.assertTrue(issubclass(LayeredAttributesImpl, LayeredAttributes))

    def test_base_state(self):
        impl = LayeredAttributesImpl()

        for key in AttributeKey:
            self.assertEqual(0, impl.get_current_attribute(key))

    def test_set_base(self):
        impl = LayeredAttributesImpl()
        impl.add_layered_effect(self.power_add_5_layer_2)
        impl.add_layered_effect(self.power_sub_3_layer_1)
        self.assertEqual(2, impl.get_current_attribute(AttributeKey.Power))

        impl.set_base_attribute(AttributeKey.Power, 10)
        self.assertEqual(12, impl.get_current_attribute(AttributeKey.Power))

    def test_add_effects_different_attributes(self):
        impl = LayeredAttributesImpl()

        impl.set_base_attribute(AttributeKey.Power, 10)
        impl.set_base_attribute(AttributeKey.Color, 2)
        impl.set_base_attribute(AttributeKey.ManaValue, 50)
        impl.set_base_attribute(AttributeKey.Toughness, 3)

        impl.add_layered_effect(self.power_add_5_layer_2)
        impl.add_layered_effect(self.power_sub_3_layer_1)
        impl.add_layered_effect(self.color_mul_18_layer_7)
        impl.add_layered_effect(self.color_add_4_layer_0)
        impl.add_layered_effect(self.mana_sub_8_layer_3)

        self.assertEqual(2, impl.attributes[AttributeKey.Power].size())
        self.assertEqual(2, impl.attributes[AttributeKey.Color].size())
        self.assertEqual(1, impl.attributes[AttributeKey.ManaValue].size())

        self.assertEqual(12, impl.get_current_attribute(AttributeKey.Power))
        self.assertEqual(108, impl.get_current_attribute(AttributeKey.Color))
        self.assertEqual(42, impl.get_current_attribute(AttributeKey.ManaValue))
        self.assertEqual(3, impl.get_current_attribute(AttributeKey.Toughness))

    def test_clear_all_layers(self):
        impl = LayeredAttributesImpl()

        impl.add_layered_effect(self.power_add_5_layer_2)
        impl.add_layered_effect(self.color_add_4_layer_0)
        impl.add_layered_effect(self.mana_sub_8_layer_3)

        self.assertEqual(5, impl.get_current_attribute(AttributeKey.Power))
        self.assertEqual(4, impl.get_current_attribute(AttributeKey.Color))
        self.assertEqual(-8, impl.get_current_attribute(AttributeKey.ManaValue))

        impl.clear_layered_effects()

        for key in AttributeKey:
            self.assertEqual(0, impl.get_current_attribute(key))


if __name__ == '__main__':
    unittest.main()
