RED = (255, 0, 0)
BLUE = (36, 49, 168)
SAND = (253, 243, 190)
GREEN = (58, 153, 68)
BROWN = (101, 67, 33)
OFFWHITE = (250, 250, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

HEIGHTS = []
# (color, weight)

for c, w in [(BLUE, 7), (SAND, 1), (GREEN, 2), (BROWN, 1), (OFFWHITE, 0), (WHITE, 2)]:
    HEIGHTS += [c] * w