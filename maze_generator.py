import argparse
# from src.maze_builder_interface import MazeBuilderInterface
from src.algorithms_collection import algorithms_list


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--rows', action='store', type=int, help="""
                         integer containing the number of rows on the maze""")
    parser.add_argument('-c', '--columns', action='store', type=int, help="""
                        integer containing the number of columns on the
                        maze""")
    parser.add_argument(
        '--algorithm', choices=range(len(algorithms_list)), default=0,
        type=int, help="""Select the type of algorithm for maze
            construction:\n\t1. Backtracker\n\tRandomized kruskal""")
    parser.add_argument('--gui', action='store_true',
                        help=""" run a pygame gui""")

    return parser.parse_args()


def main() -> None:
    args: argparse.Namespace = parse_arguments()

    columns: int = args.columns
    rows: int = args.rows

    gui: bool = args.gui
    algorithm_id: int = args.algorithm

    if gui:
        print('gui')
    else:
        if algorithm_id >= len(algorithms_list):
            raise IndexError(
                f"Algorithm selected not recognized: {algorithm_id}")
        maze_builder = algorithms_list[algorithm_id](columns, rows)
        maze_builder.build()

        print(maze_builder, end="")


if __name__ == '__main__':
    main()
