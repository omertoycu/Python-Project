import imageio.v3 as iio

filenames = ["image.jpg", "image2.jpg"]
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 0.5, loop = 5)
