from keras.preprocessing.image import img_to_array
from keras.models import load_model
from tensorflow import keras
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np
from tensorflow.python.keras.saving.save import save_model

filename = 'test.png'

img = mpimg.imread(filename)
img = color.rgb2gray(img)
img = resize(img, (28, 28))


plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()


img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')


# TODO: ucitaj model
mlp_mnist = keras.models.load_model('model_cnn')

# TODO: napravi predikciju 
label=mlp_mnist.predict(img)

# TODO: ispis rezultat
print("------------------------")
print(np.argmax(label))

