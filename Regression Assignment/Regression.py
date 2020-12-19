# ML regression model for twitter prediction
import pandas as pd
import numpy as np

data_t = np.genfromtxt ('Twitter.data', delimiter=",")
data = data_t[0:2000,:]
labels = data[:,-1]
data = np.delete(data,-1,1)
n = data.shape[1]
no_of_features = n

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.80, random_state=42)

## Linear regression using sklearn
# from sklearn.linear_model import LinearRegression

# linreg = LinearRegression()
# linreg.fit(X_train, y_train)
# y_pred = linreg.predict(X_test)
# acc_lin = round(linreg.score(X_train, y_train) * 100, 2)
# print('Training accuracy = %d%%' % acc_lin)
# acc_test = round(linreg.score(X_test, y_test) * 100, 2)
# print('Test accuracy = %d%%' % acc_test)

# Neural Network using keras
from keras.optimizers import Adam, SGD
from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l2
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasClassifier
from keras.metrics import RootMeanSquaredError
from keras.callbacks import Callback, ModelCheckpoint

class EarlyStoppingByLossVal(Callback):
    def __init__(self, monitor='val_loss', value=0.001, verbose=0):
        super(Callback, self).__init__()
        self.monitor = monitor
        self.value = value
        self.verbose = verbose

    def on_epoch_end(self, epoch, logs={}):
        current = logs.get(self.monitor)
        if current is None:
            warnings.warn("Early stopping requires %s available!" % self.monitor, RuntimeWarning)

        if current < self.value:
            if self.verbose > 0:
                print("Epoch %05d: early stopping THR" % epoch)
            self.model.stop_training = True
            
callbacks = [
    EarlyStoppingByLossVal(monitor='val_loss', value=140, verbose=1),
    # EarlyStopping(monitor='val_loss', patience=2, verbose=0),
    #ModelCheckpoint(kfold_weights_path, monitor='val_loss', save_best_only=True, verbose=0),
]

lambd=0
no_of_features = data.shape[1]
model = Sequential()
model.add(Dense(no_of_features, input_dim=no_of_features, activation='linear', kernel_regularizer=l2(lambd)))
#model.add(Dense(128, activation='relu', kernel_regularizer=l2(lambd)))
#model.add(Dense(32, activation='relu', kernel_regularizer=l2(lambd)))
#model.add(Dense(32, activation='relu', kernel_regularizer=l2(lambd)))
model.add(Dense(1, activation='linear', kernel_regularizer=l2(lambd)))
optimizer = Adam(lr=0.0001) #, beta_1=0.9, beta_2=0.999
model.compile(loss='mse', optimizer=optimizer) # , metrics=['mse','mae']
model.summary()

no_of_epochs=10000
model.fit(X_train, y_train, batch_size=10, epochs=no_of_epochs,
      validation_data=(X_test, y_test),
      callbacks=callbacks)
