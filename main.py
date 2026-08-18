import sys
import random


def main() -> None:
    seed = None
    args = sys.argv[1:]
    if "-seed" in args or "--seed" in args:
        try:
            idx = args.index("-seed") if "-seed" in args else args.index("--seed")
            seed = int(args[idx + 1])
        except Exception:
            seed = None
    if seed is not None:
        random.seed(seed)

    from src.renderer import run_game

    run_game()


if __name__ == "__main__":
    main()
