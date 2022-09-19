import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.layers import Dense

# Пример из документации, перевод градусов Цельсия в градусы Фаренгейта с использованием НС

c = np.array([-40, -10, 0, 8, 15, 22, 38])
f = np.array([-40, 14, 32, 46, 59, 72, 100])

model = keras.Sequential()  # Создает модель многослойной неронной сети

# Dense создает слой нейронов полносвязной нейронной сети
# параметры: units(1) - сколько нейоронов, input_shape(1,) - сколько будет входов, bias создается автоматически
# activation='linear' - активационная функция
model.add(Dense(units=1, input_shape=(1,), activation='linear'))  # добавляем первый слой через add
# Теперй НС нужно скомпилировать и указать критерии качества и способ оптимизации алгоритма градиентного спуска
model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))  # Прописать про Adam etc
# mean_squared_error - средний квадрат ошибок
# Adam(0.1) - 0.1 шаг сходимости данного алгоритма

history = model.fit(c, f, epochs=500, verbose=False)
# c - входные значения, f - выходные значения
# epochs - число эпох и на каждой итерации будем вычислять критерий качества mean_squared_error
# verbose=False не выводить служебную информацию обучения НС

plt.plot(history.history['loss'])  # loss - содержит критейри качества mean_squared_error для каждой эпохи
plt.grid(True)
plt.show()

print(model.predict([100]))  # подаем значение, те тест и получаем на выходе выходные значение
# в действительности мы бы хотели увидеть значение 212 (100*1,8+32 = 212)
# НС показывает близкие значения, что оечнь хорошо
print(model.get_weights())  # возвратит все веса для нашей модели
# [array([[1.8283157]], dtype=float32), array([28.449743], dtype=float32)]
