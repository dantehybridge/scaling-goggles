import imageio.v3 as iio

frames = []
images = []

for i in range(13):
    frames.append(f"./frames/Frame_{i + 1}.png")

for frame in frames:
    images.append(iio.imread(frame))

iio.imwrite('./result/spongebob_drinks_water_with_pinky_finger_up.gif', images, duration = 100, loop = 0)
