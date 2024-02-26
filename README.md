# Layered Attributes

```
FrostyWizard
├── test                            # Unit tests for project   
│   ├── test_layer.py 
│   ├── test_layer_impl.py
│   └── ...
│── layered_attributes.py           # Provided interface class
│── layered_attributes_impl.py      # Implementation of interface class
│── layer.py                        # Helper class for implementation class
│── main.py                         # terminal application for interacting with implementation. This isn't part of the 
                                      assigment just helpful for visualization.
│── ...
```

### Running locally

To try out the LayeredAttributes you can run the main.py or use make run to start the test app. Test app will display the attributes, base values,
as well as effects sorted by layer and order of insertion.

```
> make run
```

##### Set the base value for an attribute

```
NotAssessed: base=[0] effects:
Power: base=[2] effects:            <-----
Toughness: base=[0] effects:
Loyalty: base=[0] effects:
Color: base=[0] effects:
Types: base=[0] effects:
Subtypes: base=[0] effects:
Supertypes: base=[0] effects:
ManaValue: base=[0] effects:
Controller: base=[0] effects:


1. Set base value for attribute
2. Add effect
3. Compute value for attribute
4. Clear all effects
5. Exit

Enter Operation: 1
Enter attribute key and new base value, ex: 'power,2': power,2
```

#### Add an effect

```
NotAssessed: base=[0] effects:
Power: base=[0] effects:            
Toughness: base=[0] effects:
Loyalty: base=[0] effects:
Color: base=[0] effects:
Types: base=[0] effects:
Subtypes: base=[0] effects:
Supertypes: base=[0] effects:
ManaValue: base=[0] effects: [Op=Subtract, Mod=2, Layer=0] [Op=Add, Mod=6, Layer=5] <---
Controller: base=[0] effects:


1. Set base value for attribute
2. Add effect
3. Compute value for attribute
4. Clear all effects
5. Exit

Enter Operation: 2
Enter effect to add, ex: mana,set,3(modification),5(layer): mana,subtract,2,0
```