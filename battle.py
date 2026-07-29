from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(
    flame_factory: CreatureFactory,
    aqua_factory: CreatureFactory,
) -> None:
    print("Testing battle")

    fire = flame_factory.create_base()
    water = aqua_factory.create_base()

    print(fire.describe())
    print("vs.")
    print(water.describe())
    print("fight!")
    print(fire.attack())
    print(water.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
