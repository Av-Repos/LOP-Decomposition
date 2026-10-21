# Fourier Transform–Based Instance Decomposition of the Linear Ordering Problem 🧩

This repository provides an efficient implementation of the Fourier transform (FT)–based instance decomposition of Linear Ordering Problem (LOP) instances. Given a LOP instance with the format

```text
n
b_11 ...  b_1n
.    .    .
.    .    .
.    .    .
b_n1 ...  b_nn
```

the software generates two sub-instances corresponding to the individual Fourier components of the original objective function:

* **p.dat** — Contains the contribution associated with the **(n-1,1)** irreducible representation.
* **h.dat** — Contains the contribution associated with the **(n−2,1,1)** irreducible representation.

Each generated sub-instance has the same dimension as the original LOP instance.

To apply the decomposition, just execute:

`python3 main.py`

and follow the instructions.

## Dependencies ⚙️

The software has been tested with

* Python 3.12.2
  * numpy 2.3.4
