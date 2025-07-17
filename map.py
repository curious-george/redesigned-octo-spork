class PlayerUnit:
    def __init__(self, name, disposition="alert"):
        self.name = name
        self.disposition = disposition

class Cell:
    def __init__(self, topography="flat", wetness="dry", sunlight="total", player_unit=None):
        self.topography = topography
        self.wetness = wetness
        self.sunlight = sunlight
        self.player_unit = player_unit

    def render(self):
        topo_char = {
            "flat": ".",
            "hill": "n",
            "mountain": "M",
            "gorge": "g",
            "valley": "v"
        }.get(self.topography, "?")

        wet_char = {
            "dry": " ",
            "swamp": "s",
            "shallow river": "~",
            "deep river": "≈",
            "deep lake": "L",
            "ocean": "O"
        }.get(self.wetness, "?")

        sun_char = {
            "total": "*",
            "partial": "’",
            "none": " "
        }.get(self.sunlight, "?")

        player_char = " "
        if self.player_unit:
            player_char = {
                "alert": "A",
                "resting": "R",
                "scouting": "S",
                "quiet": "Q",
            }.get(self.player_unit.disposition, "?")

        return f"{topo_char}{wet_char}{sun_char}{player_char}"

class Map:
    def __init__(self, *args):
        if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            self.width = args[0]
            self.height = args[1]
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
            start_coord = self._parse_coord(args[0])
            end_coord = self._parse_coord(args[1])
            self.width = end_coord[0] - start_coord[0] + 1
            self.height = end_coord[1] - start_coord[1] + 1
        else:
            raise ValueError("Invalid arguments for Map constructor")

        self.grid = [[Cell() for _ in range(self.width)] for _ in range(self.height)]

    def _parse_coord(self, coord_str):
        col_str = ""
        row_str = ""
        for char in coord_str:
            if char.isalpha():
                col_str += char
            elif char.isdigit():
                row_str += char

        col = 0
        for char in col_str.upper():
            col = col * 26 + (ord(char) - ord('A'))

        row = int(row_str) - 1
        return col, row

    def render(self):
        # Top border
        print('┌' + '─' * (self.width * 4) + '┐')

        # Middle rows
        for row in self.grid:
            print('│' + ''.join([cell.render() for cell in row]) + '│')

        # Bottom border
        print('└' + '─' * (self.width * 4) + '┘')
