import os
from typing import Optional

from layered_attributes import LayeredEffectDefinition, AttributeKey, EffectOperation
from layered_attributes_impl import LayeredAttributesImpl


def parse_effect(usr_input: str) -> Optional[LayeredEffectDefinition]:
    split = usr_input.split(",")
    if len(split) != 4:
        raise Exception("Invalid number of inputs, expected 4 but got {}".format(len(split)))

    return LayeredEffectDefinition(Attribute=parse_attribute(split[0].strip()),
                                   Operation=parse_operation(split[1].strip()),
                                   Modification=parse_modification(split[2]),
                                   Layer=parse_layer(split[3]))


def parse_set_attribute_base(usr_input: str):
    split = usr_input.split(",")
    if len(split) != 2:
        raise Exception("Invalid number of inputs, expected 4 but got {}".format(len(split)))
    return [parse_attribute(split[0]), parse_modification(split[1])]


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

    # Pushes up anything that might already be in the terminal. Just running clear doesn't seem to work.
    for i in range(100):
        print()

    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            impl.print()
            print(
                "\n1. Set base value for attribute \n2. Add effect \n3. Compute value for attribute \n4. Clear all effects \n5. Exit\n")

            operation_input = input("Enter Operation: ").lower().strip()
            if operation_input == "exit":
                exit(0)

            if "1" == operation_input:
                set_base_input = input("Enter attribute key and new base value, ex: 'power,2': ").lower().strip()
                set_base_operation = parse_set_attribute_base(set_base_input)
                impl.set_base_attribute(set_base_operation[0], set_base_operation[1])
            elif "2" == operation_input:
                effect_input = input("Enter effect to add, ex: mana,set,3(modification),5(layer): ").lower().strip()
                effect = parse_effect(effect_input)
                impl.add_layered_effect(effect)
            elif "3" == operation_input:
                get_input = input("Enter attribute key: ").lower().strip()
                attribute_key = parse_attribute(get_input)
                computed_value = impl.get_current_attribute(attribute_key)
                result_message = "\n{} computed value: {}".format(attribute_key.name, computed_value)
                print(result_message)
                input()
            elif "4" == operation_input:
                impl.clear_layered_effects()
            else:
                print("\n!!! Invalid command [{}] !!!".format(operation_input))
                input()

        except Exception as e:
            error_message = str(e)
            print("\n!!! error [{}] !!!".format(error_message))
            input()
