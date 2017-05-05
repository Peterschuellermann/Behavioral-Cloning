import csv
import cv2
import numpy as np
import sys # required for floyd argument

# import the driving log as csv
lines = []
floyd = 0
data_path = '../CarND-P3-Data/'

# enable floyd mode for different datapath
if "floyd" in sys.argv:
    # floyd = 1
    data_path = '/input/'
    print("floydmode activated!")


with open(data_path + 'driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)      # skip the first line
    for line in reader: 
        lines.append(line)


# import all images from the available data 
# and append them to arrays for easier use
images = []
measurements = []
for line in lines:
    source_path = line[0]
    filename = source_path.split('/')[-1]
    current_path = data_path + 'IMG/' + filename
    image = cv2.imread(current_path)
    images.append(image)
    measurement = float(line[3])
    measurements.append(measurement)


# convert the image and measurements array
# to serve as training data
X_train = np.array(images)
Y_train = np.array(measurements)


# todo: preprocessing

# todo: split data


from keras.models import Sequential
from keras.layers import Flatten, Dense, Conv2D



model = Sequential()

# input shape for normalized images
model.add(Flatten(input_shape=(160,320,3)))

# Convolution 24@31x98
#model.add(Conv2D(24, 5, 5, input_shape=(160,320,3)))

# Convolution 36@14x47
#model.add(Conv2D(32, 5, 5))


# Convolutioin 48@5x22
#model.add(Conv2D(48, 3, 3))


# Convolution 64@3x20
#model.add(Conv2D(60, 3, 3))


# Convolution 64@1x18
#model.add(Conv2D(60, 3, 3))


# Flatten
#model.add(Flatten())

# Fully connected 1164 neurons
#model.add(Dense(1164))


# Fully connected 100 neurons
#model.add(Dense(100))


# Fully connected 50 neurons
#model.add(Dense(50))


# Fully connected 10 neurons (?)
#model.add(Dense(10))


# output vehicle control
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, Y_train, validation_split=0.2, shuffle=True)

model.save('model.h5')
