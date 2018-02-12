import tensorflow as tf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os 

if "DISPLAY" not in os.environ:
    # remove Travis CI Error
    matplotlib.use('Agg')

def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    # noise term prevents the zero division
    return numerator / (denominator + 1e-7)

def predict(file):
    # train Parameters
    seq_length = 6
    data_dim = 1
    hidden_dim = 12 # 내 맘대로 정해도 됨
    output_dim = 1
    learning_rate = 0.05
    iterations = 1000
    layer_num=3

    # train Data: Open, High, Low, Volume, Close
    origin_xy = np.loadtxt('train.csv', delimiter=',', skiprows=1, usecols=range(1,8))
    xy = MinMaxScaler(origin_xy)
    x = xy[:,:-1]
    y = xy[:,-1]
    x = x.reshape(-1,seq_length,data_dim)
    y = y.reshape(-1,data_dim) 

    # train/validation split
    train_size = int(len(y) * 0.7)
    test_size = len(y) - train_size
    trainX, validX = np.array(x[0:train_size]), np.array(x[train_size:])
    trainY, validY = np.array(y[0:train_size]), np.array(y[train_size:])

    #test data
    test_x=np.loadtxt(file, delimiter=',', skiprows=1, usecols=range(1,7))
    test_x = test_x.reshape(-1,seq_length, data_dim)
    
    # input place holders
    X = tf.placeholder(tf.float32, [None, seq_length, data_dim])
    Y = tf.placeholder(tf.float32, [None, 1])

    # build a LSTM network
    cells=[]
    for _ in range(layer_num):
        cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_dim, state_is_tuple=True, activation=tf.tanh)
        #cell = tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=0.7)
        cells.append(cell)

    cell = tf.contrib.rnn.MultiRNNCell(cells)
    outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
    Y_pred = tf.contrib.layers.fully_connected(outputs[:, -1], output_dim, activation_fn=None)  # We use the last cell's output

    # cost/loss
    loss = tf.reduce_sum(tf.square(Y_pred - Y))  # sum of the squares
    # optimizer
    optimizer = tf.train.AdamOptimizer(learning_rate)
    train = optimizer.minimize(loss)

    # RMSE
    targets = tf.placeholder(tf.float32, [None, 1])
    predictions = tf.placeholder(tf.float32, [None, 1])
    rmse = tf.sqrt(tf.reduce_mean(tf.square(targets - predictions)))

    sess=tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)

    # Training step
    for i in range(iterations):
        _, step_loss = sess.run([train, loss], feed_dict={X: trainX, Y: trainY})
        print("[step: {}] loss: {}".format(i+1, step_loss))

    # validation step
    valid_predict = sess.run(Y_pred, feed_dict={X: validX})
    rmse_val = sess.run(rmse, feed_dict={targets: validY, predictions: valid_predict})
    revised_rmse = rmse_val*(origin_xy.max()-origin_xy.min()+1e-7) + origin_xy.min()
    print("RMSE: {}".format(revised_rmse))

    # Plot predictions
    plt.plot(validY)
    plt.plot(valid_predict)
    plt.xlabel("Time Period")
    plt.ylabel("Temperature")
    plt.show()
    
    #test step
    test_predict = sess.run(Y_pred, feed_dict={X: test_x})
    prediction_list = []
    for i in test_predict:
        revised_pred = i[0]*(origin_xy.max()-origin_xy.min()+1e-7) + origin_xy.min()
        prediction_list.append(revised_pred)
    return prediction_list

def write_result(predictions):
    # You don't need to modify this function.
    with open('result.csv', 'w') as f:
        f.write('Value\n')
        for l in predictions:
            f.write('{}\n'.format(l))


def main():
    # You don't need to modify this function.
    predictions = predict('test.csv')
    write_result(predictions)


if __name__ == '__main__':
    # You don't need to modify this part.
    main()