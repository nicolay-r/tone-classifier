import theano
import numpy as np
import theano.tensor as T


class RNNTheano:

    def __init__(self, hl_size, i_size, bptt_truncate=-1):
        x = T.matrix(name='x')
        y = T.ivector(name='y')

        # Model implementation
        out_size = 3
        U = np.random.uniform(-np.sqrt(1.0/i_size), np.sqrt(1.0/i_size),
                              (hl_size, i_size))
        V = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (out_size, hl_size))
        W = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (hl_size, hl_size))
        self.U = theano.shared(U.astype(theano.config.floatX), name='U')
        self.V = theano.shared(V.astype(theano.config.floatX), name='V')
        self.W = theano.shared(W.astype(theano.config.floatX), name='W')

        self.dU = theano.shared(U.astype(theano.config.floatX), name='dU')
        self.dV = theano.shared(V.astype(theano.config.floatX), name='dV')
        self.dW = theano.shared(W.astype(theano.config.floatX), name='dW')

        def forward_prop_step(xt, o, st_prev, U, W, V):
            s_next = T.tanh(U.dot(xt) + W.dot(st_prev))
            o_next = T.nnet.softmax(V.dot(s_next))[0]
            return [o_next, s_next]

        [o, s], updates = theano.scan(
                forward_prop_step,
                # iterate through ivector 'x'
                sequences=x,
                # use the full backpropagation (for T.grad)
                truncate_gradient=bptt_truncate,
                # initial output state, which computed recurently
                outputs_info=[
                    dict(initial=T.zeros(out_size)),
                    dict(initial=T.zeros(hl_size))],
                non_sequences=[self.U, self.W, self.V],
                strict=True)

        # Check the forward propagation function
        # f = theano.function(inputs=[x], outputs=results, updates=updates)

        cost = T.sum(T.nnet.categorical_crossentropy(o, y))

        dU = T.grad(cost, self.U)
        dV = T.grad(cost, self.V)
        dW = T.grad(cost, self.W)

        reg_lambda = T.scalar(name='reg_lambda')

        # Functions
        self.forward_propagation = theano.function(inputs=[x], outputs=[o[-1]])
        self.calculate_loss = theano.function(inputs=[x, y], outputs=cost)
        self.sgd_step = theano.function(
                inputs=[x, y, reg_lambda],
                updates=[(self.U, self.U - reg_lambda * dU),
                         (self.W, self.W - reg_lambda * dW),
                         (self.V, self.V - reg_lambda * dV),
                         (self.dU, dU),
                         (self.dW, dW),
                         (self.dV, dV)])

    def rollback_step(self, reg_lambda):
        self.U.set_value(self.U.get_value() + reg_lambda * self.dU.get_value())
        self.W.set_value(self.W.get_value() + reg_lambda * self.dW.get_value())
        self.V.set_value(self.V.get_value() + reg_lambda * self.dV.get_value())
