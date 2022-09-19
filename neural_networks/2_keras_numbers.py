# Распознование рукописных цифр
# MNIST - база данных образцов рукописного написания цифр, идет вместе с Keras
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist  # 60k - обучающая выборка 10k - тестовая выборка
import keras
from keras.layers import Dense, Flatten

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Станадр
x_train = x_train / 255
x_test = x_test / 255

y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)

# отображение первых 25 изображений из обучающей
plt.figure(figsize=(10, 5))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.xticks([])
    plt.imshow(x_train[i], cmap=plt.cm.binary)

plt.show()

model = keras.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
print(model.summary())
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2)
model.evaluate(x_test, y_test_cat)

n = 111
x = np.expand_dims(x_test[n], axis=0)
result = model.predict(x)
print(result)
print(f'Распознанная цифра {np.argmax(result)}')

plt.imshow(x_test[n], cmap=plt.cm.binary)
plt.show()

predict = model.predict(x_test)
predict = np.argmax(predict, axis=1)

print(predict.shape)
print(predict[:20])
print(y_test[:20])

mask = predict == y_test
print(mask[:10])
x_false = x_test[~mask]
y_false = x_test[~mask]

print(x_false.shape)

# Вывод первых 25 неверных результатов
plt.figure(figsize=(10, 5))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x_false[i], cmap=plt.cm.binary)

plt.show()
