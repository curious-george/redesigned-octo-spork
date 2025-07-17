from map import Map, PlayerUnit

if __name__ == "__main__":
    my_map = Map(10, 5)

    # Add some features to the map
    my_map.grid[1][1].topography = "hill"
    my_map.grid[1][1].wetness = "shallow river"
    my_map.grid[1][1].sunlight = "partial"
    my_map.grid[1][1].player_unit = PlayerUnit("Player 1", "alert")

    my_map.grid[2][2].topography = "mountain"
    my_map.grid[2][2].wetness = "deep lake"
    my_map.grid[2][2].sunlight = "none"
    my_map.grid[2][2].player_unit = PlayerUnit("Player 2", "resting")

    my_map.grid[3][3].topography = "valley"
    my_map.grid[3][3].wetness = "swamp"
    my_map.grid[3][3].sunlight = "total"
    my_map.grid[3][3].player_unit = PlayerUnit("Player 3", "scouting")

    my_map.render()
