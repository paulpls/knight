"""
    Colors for fancier output. Assumes the terminal is using 16 colors.

"""


class Colors:

    @staticmethod
    def color(c):
        """
            Get a color from the ones available in the dictionary.

        """
        return {
            # Common
            'R': "\033[0m",         # Reset
            'D': "\033[7;0;40m",    # Dark squares
            'L': "\033[7;1;30m",    # Light squares
            'N': "\033[7;1;37m",    # Knight
            'F': "\033[7;1;34m",    # Friendly pieces
            # Labels
            'L1': "\033[0;32m",     # 1 move away
            'L2': "\033[0;33m",     # 2 moves away
            'L3': "\033[1;31m",     # 3 moves away
            'L4': "\033[0;31m",     # 4 moves away
            'L5': "\033[0;35m",     # 5 moves away
            'L6': "\033[1;34m",     # 6 moves away
            'L7': "\033[1;30m",     # 7 moves away
            # Highlights
            'H1': "\033[7;0;42m",   # 1 move away
            'H2': "\033[7;0;43m",   # 2 moves away
            'H3': "\033[7;1;91m",   # 2 moves away
            'H4': "\033[7;0;41m",   # 2 moves away
            'H5': "\033[7;0;45m",   # 2 moves away
            'H6': "\033[7;0;44m",   # 2 moves away
            'H7': "\033[7;0;40m",   # 2 moves away
        }.get(c, None)


    @staticmethod
    def test():
        """
            Test the terminal's color output by iterating through each color escape.

        """
        for i in range(10):
            for j in range(10):
                print(f"\033[7;0;{i}{j}m<7;0;{i}{j}m>\033[0m")
                print(f"\033[7;1;{i}{j}m<7;1;{i}{j}m>\033[0m")
        # Reset color to avoid artifacts
        print(Colors.color('R'))



