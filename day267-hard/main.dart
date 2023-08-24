import 'dart:math';

final matrix = [
  '...K....'.split(""),
  '........'.split(""),
  '.B......'.split(""),
  '......P.'.split(""),
  '.......R'.split(""),
  '..N.....'.split(""),
  '........'.split(""),
  '.....Q..'.split(""),
];


void main(List<String> args) {
  List<Piece> pieces = List.empty(growable: true);
  for (var x = 0; x < matrix.length; x++) {
    for (var y = 0; y < matrix[x].length; y++) {
      var letter = matrix[x][y];
      if (letter != ".") {
        pieces.add(Piece.fromLetter(letter, x, y));
      }
    }
  }
  final king = pieces.firstWhere((element) => element is King);
  pieces.remove(king);
  final checkingPieces = pieces.where((it) => it.check(king));
    if(checkingPieces.isNotEmpty) {
      print("Check");
      checkingPieces.forEach((it) => it.printMatrix(king));
    }
}

Set<Point<int>> diagonnally(Point<int> coordinates, int offset) {
  return {
    coordinates + Point(1, 1) * offset,
    coordinates + Point(-1, 1) * offset,
    coordinates + Point(1, -1) * offset,
    coordinates + Point(-1, -1) * offset,
  };
}
Set<Point<int>> vertically(Point<int> coordinates, int offset) {
  return { Point(coordinates.x, offset)};
}
Set<Point<int>> horizontally(Point<int> coordinates, int offset) {
  return { Point(offset, coordinates.y) };
}

abstract class Piece {
  final Point<int> coordinates;

  Piece({required this.coordinates});

  Set<Point<int>> get possibleMoves;

  factory Piece.fromLetter(String letter, int x, int y) {
    switch (letter) {
      case 'K':
        return King(coordinates: Point(x, y));
      case 'Q':
        return Queen(coordinates: Point(x, y));
      case 'B':
        return Bishop(coordinates: Point(x, y));
      case 'N':
        return Knight(coordinates: Point(x, y));
      case 'R':
        return Rook(coordinates: Point(x, y));
      default:
        return Pawn(coordinates: Point(x, y));
    }
  }

  void printMatrix(Piece target) {
    for (var x = 0; x < 8; x++) {
      var row = "";
      for (var y = 0; y < 8; y++) {
        var point = Point(x, y);
        if (point == coordinates) {
          row += runtimeType.toString().substring(0, 1);
        } else if (possibleMoves.contains(point)) {
          row += point == target.coordinates ? "#" : "x";
        } else if (point == target.coordinates) {
          row += "K";
        } else {
          row += ".";
        }
      }
      print(row);
    }
  }

  bool check(Piece target) => possibleMoves.contains(target.coordinates);

  @override
  String toString() {
    return runtimeType.toString() + "\t@ <$coordinates>";
  }
}

class King extends Piece {
  King({required super.coordinates});

  @override
  Set<Point<int>> get possibleMoves => Set();
}

class Queen extends Piece {
  Queen({required super.coordinates});

  @override
  Set<Point<int>> get possibleMoves {
    var points = <Point<int>>{};
    for (var i = 0; i < 8; i++) {
      points.addAll(diagonnally(coordinates, i));
      points.addAll(horizontally(coordinates, i));
      points.addAll(vertically(coordinates, i));
    }
    return points..remove(coordinates);
  }
}

class Bishop extends Piece {
  Bishop({required super.coordinates});

   @override
  Set<Point<int>> get possibleMoves {
    var points = <Point<int>>{};
    for (var i = 0; i < 8; i++) {
      points.addAll(diagonnally(coordinates, i));
    }
    return points..remove(coordinates);
  }
}

class Rook extends Piece {
  Rook({required super.coordinates});

   @override
  Set<Point<int>> get possibleMoves {
    var points = <Point<int>>{};
    for (var i = 0; i < 8; i++) {
      points.addAll(horizontally(coordinates, i));
      points.addAll(vertically(coordinates, i));
    }
    return points..remove(coordinates);
  }
}

class Knight extends Piece {
  Knight({required super.coordinates});

  @override
  Set<Point<int>> get possibleMoves => {
    coordinates + Point(2, 3),
    coordinates + Point(2, -3),
    coordinates + Point(3, 2),
    coordinates + Point(3, -2),
    coordinates + Point(-2, 3),
    coordinates + Point(-2, -3),
    coordinates + Point(-3, 2),
    coordinates + Point(-3, -2),
  };
}

class Pawn extends Piece {
  Pawn({required super.coordinates});

  @override
  Set<Point<int>> get possibleMoves => {
        this.coordinates + Point(-1, -1),
        this.coordinates + Point(-1, 1),
      };
}
