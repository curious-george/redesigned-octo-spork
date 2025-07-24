import argparse
from map import Map

def main():
    parser = argparse.ArgumentParser(description="Draw a square on the map.")
    parser.add_argument("-square", type=int, required=True, help="Size of the square to draw.")
    parser.add_argument("-x", type=int, default=0, help="x-coordinate of the top-left corner.")
    parser.add_argument("-y", type=int, default=0, help="y-coordinate of the top-left corner.")
    args = parser.parse_args()

    my_map = Map(20, 10)  # Create a default map

    # Draw the square
    for i in range(args.square):
        for j in range(args.square):
            if 0 <= args.x + i < my_map.width and 0 <= args.y + j < my_map.height:
                my_map.grid[args.y + j][args.x + i].topography = "hill"

    my_map.render()

if __name__ == "__main__":
    main()
