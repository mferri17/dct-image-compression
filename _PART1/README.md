# PyDCT
> An implementation of the Discrete Cosine Transform Type-II in Python.

Project 2 (part 1) for the *Methods of Scientific Computation* course for the MSc in Computer Science at University of Milano-Bicocca.

## Brief
The project aims to implement the Discrete Cosine Transform Type-II, and compare its time complexity against a library's implementation (which supposingly uses a Fast Fourier Transform behind the scenes). The comparison will be held against `scipy`'s implementation.

#
## Prerequisites

* Python 3.0 or greater
* Scipy

## Installation
```sh
$ git clone https://github.com/Dodicin/pydct
$ cd pydct
$ pip install -r requirements.txt
```

## Structure
The file `pydct.py` contains an implementation of the Discrete Cosine Transform Type II for 1D arrays and 2D matrices, using numpy for data structures.

The file `test.py` contains the standard tests which have been given in the project.

The file `compare.py` outputs the time taken for both `scipy` and `pydct`'s DCT implementations applied to randomly generated matrices of increasing size. The data is outputted in `data/data.csv`.

#
## Authors

- **Nassim Habbash** (808292) - [dodicin](https://github.com/dodicin)
- **Marco Ferri** (807130) - [mferri17](https://github.com/mferri17)