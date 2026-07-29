from ex0 import (
    FlameFactory,
    AquaFactory,
)

from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)

from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)

from ex2.strategies import BattleStrategy
from ex0.factories import CreatureFactory
from ex2.exceptions import InvalidStrategyError


Opponent = tuple[CreatureFactory, BattleStrategy]


def tournament(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):

                factory1, strategy1 = opponents[i]
                factory2, strategy2 = opponents[j]

                creature1 = factory1.create_base()
                creature2 = factory2.create_base()

                print("* Battle *")
                print(creature1.describe())
                print("vs.")
                print(creature2.describe())
                print("now fight!")

                strategy1.act(creature1)
                strategy2.act(creature2)

    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    tournament([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print()

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    tournament([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])


if __name__ == "__main__":
    main()
