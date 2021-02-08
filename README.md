# Puzzle
A Python programme for checking if the logic puzzle playing field is ready to start the game.
# Usage
The board contains white and colored cells. Colored ones contain numbers from 1 to 9. These numbers shouldn't be repeated in rows, columns and blocks. At the entrance to the main function is a board that contains a list of 9 lines.
```python
import puzzle

puzzle.validate_board([
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]) #returns False
```