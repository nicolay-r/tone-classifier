import numpy as np
import logging


# TODO: pass here the output filepath based on the parameter from argv.
def train_network(model, X, y, output, reg_lambda=10e-2, min_reg_lambda=10e-7,
                  callback=None, epoch_delta=1, batch_size=8, epochs_count=20):
    """
    Train neural network model, based on the 'train' set.

    Arguments:
    ---------
        model : RNNTheano
            neural network model which will be trained
        X : np.ndarray
            array of sentences. Each sentence presented as embedding vector
            of the size which corresponds to the 'model' input
        y : np.array
            describes the class of each sentence presented in 'X' dataset
        reg_lambda : float
            regression parameter for sgd.
        callback : func
            callback which calls every certain amount of 'epoch_delta'
        epoch_delta: int
            amount of epochs will be passed before 'callback' has been called.
        batch_size: int
            batch size.
        epochs_count: int
            amount of epochs.
        output : str
            output filepath where to store the model.
    Returns:
    -------
        None
    """
    i_rl = reg_lambda
    rl_div = 0.5

    logging.info("batch size: %f" % (batch_size))
    logging.info("epochs count: %f" % (epochs_count))
    logging.info("batch size: %f" % (batch_size))

    epoch = 0
    while epoch < epochs_count:

        logging.info('epoch: %s' % (epoch))

        p = np.random.permutation(len(X))
        X = X[p]
        y = y[p]

        for i in range(len(X) / batch_size):

            start = i * batch_size

            Xb = X[start:(start + batch_size)]
            yb = y[start:(start + batch_size)]

            p_loss = model.calculate_loss(Xb, yb)
            model.sgd_step(Xb, yb, reg_lambda)
            c_loss = model.calculate_loss(Xb, yb)
            while (c_loss >= p_loss and reg_lambda > min_reg_lambda):
                # logging.info("current_loss: %f" % (c_loss))
                # logging.info("rollback sgd_step, lost=%f. reg_lambda=%f" %
                #             (c_loss, reg_lambda))

                model.rollback_step(reg_lambda)
                reg_lambda *= rl_div
                model.apply_step(reg_lambda)
                c_loss = model.calculate_loss(Xb, yb)

            logging.info("reg_lambda: %f" % (reg_lambda))

            if (reg_lambda < min_reg_lambda):
                reg_lambda = i_rl
                logging.info("reset reg_lambda: %f to %f" % (reg_lambda, i_rl))

            p_loss = c_loss

        logging.info('save model: %s' % (output))
        model.save(output)

        epoch += 1

        if (epoch % epoch_delta == 0 and callback is not None):
            callback()
