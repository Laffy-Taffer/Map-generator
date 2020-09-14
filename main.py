import noise
from settings import *
from random import randint
from PIL import Image, ImageDraw

# shifts the view in a random direction
shiftx = randint(-10000, 10000)  
shifty = randint(-10000, 10000)

# Creates image and prepares for drawing
out = Image.new("RGB", (imgwidth, imgheight))
d = ImageDraw.Draw(out)


# Get highest and lowest points of the map to normalize the heightmap
def gethighlow():
	l = h = (noise.snoise2(((0 + shiftx) / freq), ((0 + shifty) / freq), octave)+1)/2
	for x in range(imgwidth):
		for y in range(imgheight):
			i = (noise.snoise2(((x + shiftx) / freq), ((y + shifty) / freq), octave)+1)/2
			if i > h:
				h = i
			if i < l:
				l = i
	h = (h - l)
	return h, l


# Get value of a coordinate and return a value between 0 and 1 (normalized thanks to gethighlow)
def getheight(coordx, coordy):
	coordinate = (noise.snoise2(((coordx + shiftx) / freq), ((coordy + shifty) / freq), octave) + 1) / 2
	return ((coordinate-lo)*(highweight/hi))**lowweight


hi, lo = gethighlow()
for x in range(imgwidth):
	for y in range(imgheight):
		v = getheight(x, y) * (len(HEIGHTS)-1)
		# Map height value to color
		color = WHITE
		for height in range(len(HEIGHTS)-1):
			if height <= v < height + 1:
				color = HEIGHTS[height]
				break

		d.point((x, y), fill=color)

out.save('noisetest.png')
