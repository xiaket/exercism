#!/usr/bin/env python
#encoding=utf8

BLACK = 'B'
WHITE = 'W'
NONE = "N"


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @property
    def neighbours(self):
        return [
            (self.x - 1, self.y), (self.x + 1, self.y),
            (self.x, self.y - 1), (self.x, self.y + 1),
        ]

    @property
    def rep(self):
        return (self.x, self.y)

    def is_neighbour(self, other):
        return (other.x, other.y) in self.neighbours

    def __repr__(self):
        return "<P({}, {}, {})".format(self.x, self.y, self.color)


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, b):
        self.map = {}
        self.rows = len(b)
        self.columns = len(b[0])
        for x in range(self.columns):
            for y in range(self.rows):
                self.map[(x, y)] = Point(x, y, b[y][x])

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not ((0 <= x < self.columns) and (0 <= y < self.rows)):
            raise ValueError("Invalid input, {}, {}, {}, {}".format(x, y,
                                                                self.columns,
                                                                self.rows))

        start = self.map[(x, y)]
        if start.color != " ":
            return NONE, set([])

        cache = set([start])
        color = None
        while True:
            new = set([])
            for item in cache:
                for i, j in item.neighbours:
                    if (i, j) not in self.map:
                        continue
                    neighbour = self.map[(i, j)]
                    if neighbour.color == " " and neighbour not in cache:
                        new.add(neighbour)

                    if neighbour.color == " ":
                        continue
                    if color is None:
                       color = neighbour.color
                    elif color != neighbour.color:
                        color = NONE
                        continue
            if not new:
                break
            cache = cache | new

        if color == 'W':
            color = WHITE
        elif color == 'B':
            color = BLACK
        else:
            color = NONE
        return color, {p.rep for p in cache}

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        result = {WHITE: set([]), BLACK: set([]), NONE: set([])}
        for (y, x) in self.map:
            #print("y, x", y, x)
            scanned = set([]).union(*[s for s in result.values()])
            #print("scan", scanned)
            #print(result)
            if (x, y) in scanned:
                continue
            color, ter = self.territory(y, x)
            #print("y, x", y, x, color, ter)
            if ter:
                result[color] = result[color] | ter
            #print("after", result)
        return result
