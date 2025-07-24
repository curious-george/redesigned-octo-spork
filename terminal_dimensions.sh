#!/bin/bash
# This script prints the dimensions of the terminal

rows=$(tput lines)
cols=$(tput cols)

echo "Terminal dimensions:"
echo "Rows: $rows"
echo "Columns: $cols"
