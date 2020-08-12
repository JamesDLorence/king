from src.battle.BattleSetup import setup_battle


def main():
    battle = setup_battle()
    battle.start(mode="terminal")


if __name__ == "__main__":
    main()
