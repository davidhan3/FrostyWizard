from layered_attributes import LayeredAttributes, LayeredEffectDefinition, AttributeKey, EffectOperation
from layered_attributes_impl import LayeredAttributesImpl


def parse_input(usr_input: str) -> LayeredEffectDefinition:
    print(usr_input)
    split = usr_input.split(",")
    if len(split) != 4:
        print("Invalid number of inputs, expected 4 but got {}".format(len(split)))

    try:
        return LayeredEffectDefinition(Attribute=parse_attribute(split[0].strip()),
                                       Operation=parse_operation(split[1].strip()),
                                       Modification=parse_modification(split[2]),
                                       Layer=parse_layer(split[3]))
    except Exception as e:
        print(str(e))
        return None


def parse_attribute(usr_input: str) -> AttributeKey:
    for key in AttributeKey:
        if key.name.lower() == usr_input:
            return key
    raise Exception("Invalid attribute key [{}] provided".format(usr_input))


def parse_operation(usr_input: str) -> EffectOperation:
    for key in EffectOperation:
        if key.name.lower() == usr_input:
            return key
    raise Exception("Invalid operation [{}] provided".format(usr_input))


def parse_modification(user_input: str) -> int:
    try:
        return int(user_input)
    except ValueError:
        raise Exception("Modification amount is not an integer")


def parse_layer(user_input: str) -> int:
    try:
        return int(user_input)
    except ValueError:
        raise Exception("layer value is not an integer")


if __name__ == "__main__":
    impl = LayeredAttributesImpl()

    # effect0 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Add, Modification=5, Layer=2)
    # effect1 = LayeredEffectDefinition(Attribute=AttributeKey.Power, Operation=EffectOperation.Set, Modification=2, Layer=2)

    while True:
        impl.print()
        operation_input = input("Enter Operation: ").lower().strip()
        if operation_input == "exit":
            exit(0)

        if "add" == operation_input:
            effect_input = input("Enter effect to add: ").lower().strip()
            effect = parse_input(effect_input)
            impl.add_layered_effect(effect)
        elif "get" == operation_input:
            effect_input = input("Enter attribute key: ").lower().strip()
            print(impl.get_current_attribute(AttributeKey.Power))
        else:
            print("invalid command")
        print("blank")
