board = [
    [".", ".", ".", ".", ".", "K", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", "B", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "P", "."],
    [".", ".", ".", ".", ".", ".", ".", "R"],
    [".", ".", "N", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "Q", ".", "."],
]


def coordinates_in_board(x, y):
    return x < 8 and x >= 0 and y < 8 and y >= 0


class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def possible_capture_moves(self, pieces_matrix) -> list[list]:
        posibilities_matrix = [[False] * 8 for i in range(8)]

        for direction in self._piece_movements():
            for i, j in direction:
                if not coordinates_in_board(self.x + i, self.y + j) or pieces_matrix[
                    self.x + i
                ][self.y + j] not in [".", "K"]:
                    break
                else:
                    posibilities_matrix[self.x + i][self.y + j] = True

        return posibilities_matrix

    def _piece_movements(self):
        pass


class Queen(Piece):
    def _piece_movements(self):
        directions = [
            (1, 1),
            (0, 1),
            (1, 0),
            (-1, 0),
            (-1, 1),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]
        return [
            [(i * times, j * times) for times in range(1, 8)] for i, j in directions
        ]


class Pawn(Piece):
    def _piece_movements(self):
        return [[(-1, 1)], [(-1, -1)]]


class Bishop(Piece):
    def _piece_movements(self):
        directions = [
            (1, 1),
            (-1, 1),
            (-1, -1),
            (1, -1),
        ]
        return [
            [(i * times, j * times) for times in range(1, 8)] for i, j in directions
        ]


class Rook(Piece):
    def _piece_movements(self):
        directions = [
            (0, 1),
            (-1, 0),
            (1, 0),
            (0, -1),
        ]
        return [
            [(i * times, j * times) for times in range(1, 8)] for i, j in directions
        ]


class Knight(Piece):
    def _piece_movements(self):
        return [
            [(-2, 1)],
            [(-2, -1)],
            [(2, 1)],
            [(2, -1)],
            [(1, 2)],
            [(-1, 2)],
            [(1, -2)],
            [(-1, -2)],
        ]


def create_piece(letter, x, y) -> Piece:
    if letter == "P":
        return Pawn(x, y)
    if letter == "B":
        return Bishop(x, y)
    if letter == "N":
        return Knight(x, y)
    if letter == "Q":
        return Queen(x, y)
    if letter == "R":
        return Rook(x, y)


def matrix_or(m1, m2):
    return [[m1[x][y] or m2[x][y] for y in range(8)] for x in range(8)]


def is_king_in_check(matrix):
    king_x = 0
    king_y = 0

    positions_in_danger = [[False] * 8 for i in range(8)]
    for x, row in enumerate(matrix):
        for y, letter in enumerate(row):
            if letter == ".":
                continue
            elif letter == "K":
                king_x, king_y = x, y
            else:
                piece = create_piece(letter, x, y)
                positions_in_danger = matrix_or(
                    positions_in_danger, piece.possible_capture_moves(matrix)
                )

    # print(positions_in_danger)
    return positions_in_danger[king_x][king_y]


if __name__ == "__main__":
    print(is_king_in_check(board))
