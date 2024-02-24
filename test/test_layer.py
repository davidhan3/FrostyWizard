import unittest

from layer import Layer
from layered_attributes import LayeredEffectDefinition, AttributeKey, EffectOperation


class TestLayer(unittest.TestCase):
    add5_layer10 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Add, Modification=5,
                                           Layer=10)
    sub3_layer7 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Subtract,
                                          Modification=3, Layer=7)
    mul6_layer4 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Multiply,
                                          Modification=6, Layer=4)
    and44_layer5 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.BitwiseAnd,
                                           Modification=44, Layer=5)
    add2_layer5 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Add,
                                          Modification=2, Layer=5)
    mul3_layer5 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Multiply,
                                          Modification=3, Layer=5)
    add1_layer15 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Add, Modification=1,
                                           Layer=15)

    def test_add_effects_simple(self):
        layer = Layer("power")
        layer.add_effect(effect=self.sub3_layer7)
        layer.add_effect(effect=self.add5_layer10)

        self.assertEqual(2, layer.size())
        self.assertEqual(self.sub3_layer7, layer.effects[0])
        self.assertEqual(self.add5_layer10, layer.effects[1])

    def test_add_effects_different_layers(self):
        layer = Layer("power")
        layer.set_base(2)
        layer.add_effect(effect=self.add5_layer10)
        layer.add_effect(effect=self.and44_layer5)
        layer.add_effect(effect=self.sub3_layer7)
        layer.add_effect(effect=self.mul6_layer4)
        layer.add_effect(effect=self.add2_layer5)
        layer.add_effect(effect=self.mul3_layer5)
        layer.add_effect(effect=self.add1_layer15)

        self.assertEqual(7, layer.size())
        self.assertEqual(self.mul6_layer4, layer.effects[0])
        self.assertEqual(self.and44_layer5, layer.effects[1])
        self.assertEqual(self.add2_layer5, layer.effects[2])
        self.assertEqual(self.mul3_layer5, layer.effects[3])
        self.assertEqual(self.sub3_layer7, layer.effects[4])
        self.assertEqual(self.add5_layer10, layer.effects[5])
        self.assertEqual(self.add1_layer15, layer.effects[6])
        self.assertEqual(45, layer.get_value())

    def test_set_base(self):
        layer = Layer("power")
        layer.set_base(3)
        layer.add_effect(effect=self.add5_layer10)
        layer.add_effect(effect=self.sub3_layer7)

        self.assertEqual(5, layer.get_value())

    def test_get_value(self):
        layer = Layer("power")
        layer.add_effect(effect=self.add5_layer10)
        layer.add_effect(effect=self.sub3_layer7)

        self.assertEqual(2, layer.get_value())

    def test_clear(self):
        layer = Layer("power")
        layer.add_effect(effect=self.add5_layer10)
        layer.add_effect(effect=self.add5_layer10)
        layer.add_effect(effect=self.add5_layer10)
        layer.add_effect(effect=self.add5_layer10)

        self.assertEqual(4, layer.size())
        layer.clear()
        self.assertEqual(0, layer.size())


if __name__ == '__main__':
    unittest.main()
