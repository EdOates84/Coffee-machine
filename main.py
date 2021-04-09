import sys
import json

from coffee_machine import CoffeeMachine


if __name__ == "__main__":
    with open(sys.argv[1]) as json_file:
        coffee_machine = CoffeeMachine(json.load(json_file))
        coffee_machine.run()