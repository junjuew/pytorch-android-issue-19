# Debugging

pytorch-android issue: https://github.com/pytorch/android-demo-app/issues/19.
DNN model definition is in [transformer_net.py](transformer_net.py)

## How to Use

To trace and serialize the model:

```
# the serialized model is saved to serialized.pt
python trace.py
```

To load and use the model in C++, first download [pytorch's C++ lib](https://pytorch.org/cppdocs/installing.html) to a dir named libtorch.

```
mkdir build
cmake -DCMAKE_PREFIX_PATH=<path to the clone dir>/libtorch ..
make
./load ../serialized.pt
```
