# 2017-09-20 Error Analysis

_Jon Betti_

## Problem 1

a. For the 1 sigma range:

- _i_ has a 1 sigma range of `[15.464, 15.514]` so the measured value is outside the 1 sigma range.

- _ii_ has a 1 sigma range of `[1.21x10^-3, 1.23x10^-3]` so the measured value is within the 1 sigma range.

- _iii_ has a 1 sigma range of `[2.82x10^6, 2.88x10^6]` so the measured value is outside the 1 sigma range.

b. For the 2 sigma range:

- _i_ has a 2 sigma range of `[15.439, 15.539]` so the measured value is outside the 2 sigma range.

- _ii_ has a 2 sigma range of `[1.2x10^-3, 1.24x10^-3]` so the measured value is within the 2 sigma range.

- _iii_ has a 2 sigma range of `[2.79x10^6, 2.91x10^6]` so the measured value is outside the 2 sigma range.

## Problem 2

Used `python` to calculate these:

```python
mean = lambda it: (sum(it)/len(it))
stddev = lambda it: (sum([(x - mean(it))**2 for x in it])/(len(it)-1))**0.5
```

Log:

```python
>>> mean = lambda it: (sum(it)/len(it))
>>> stddev = lambda it: (sum([(x - mean(it))**2 for x in it])/(len(it)-1))**0.5
>>> v_1_L = [92.6, 90.0, 91.5, 93.1, 93.3, 94.0, 92.1, 92.7, 93.0]
>>> mean(v_1_L)
92.47777777777779
>>> stddev(v_1_L)
1.1702326454361303
>>> v_2_L = [161.3, 162.0, 161.5, 160.0, 161.7, 162.2, 161.5, 160.9, 161.4]
>>> mean(v_2_L)
161.3888888888889
>>> stddev(v_2_L)
0.645066749345451
>>> s_L = [100.0, 100.1, 99.8, 99.9, 100.0, 100.5, 100.2, 99.8, 100.1]
>>> mean(s_L)
100.04444444444444
>>> stddev(s_L)
0.21858128414340022
```

a.

- The mean of `v_1` is `92.4777`. The standard deviation of `v_1` is `1.1702`. The variance of `v_1` is `1.3693`.

- The mean of `v_2` is `161.3888`. The standard deviation of `v_2` is `0.6450`. The variance of `v_2` is `0.4160`.

- The mean of `s` is `100.0444`. The standard deviation of `s` is `0.2185`. The variance of `s` is `0.0477`.

b.

Log:

```python
>>> (mean(v_2_L)**2 - mean(v_1_L)**2) / (2 * mean(s_L))
87.4323115652303
>>> ((2 * stddev(v_2_L) / mean(v_2_L))**2 + \
...   (2 * stddev(v_1_L) / mean(v_1_L))**2 + \
...   (stddev(s_L) / mean(s_L))**2)**0.5
0.026630661727250145
>>> ((2 * stddev(v_2_L) / mean(v_2_L))**2 + \
...   (2 * stddev(v_1_L) / mean(v_1_L))**2 + \
...   (stddev(s_L) / mean(s_L))**2)**0.5 \
...   * (mean(v_2_L)**2 - mean(v_1_L)**2) / (2 * mean(s_L))
2.328380313325188
```

`a = 87.4323`, the relative error is `0.0266`, and the absolute error is `2.3283`.

## Problem 3

```python
area = lambda a, b, d: (a*b - d*d*(0.75**0.5))
error_area = lambda a, error_a, b, error_b, d, error_d: \
  ((error_a * b)**2 + (a * error_b)**2 + 3*(d * error_d)**2)**0.5
```

Log:

```python
>>> area = lambda a, b, d: (a*b - d*d*(0.75**0.5))
>>> area(2.25, 1.30, 0.55)
2.6630273153552073
>>> error_area = lambda a, error_a, b, error_b, d, error_d: \
...   ((error_a * b)**2 + (a * error_b)**2 + 3*(d * error_d)**2)**0.5
>>> error_area(2.25, 0.03, 1.30, 0.03, 0.55, 0.03)
0.08303011501858829
>>> error_area(2.25, 0.03, 1.30, 0.03, 0.55, 0.03) / area(2.25, 1.30, 0.55)
0.031178844670436034
```

The measured area of the region based on the values given is `2.6630`.

The absolute error of the area is calculated with the error propagation formula: taking the derivative of the area by each variable and squaring it, multiplying this by the error (variance, so std dev squared) for the variable, summing the results, and taking the square root. This value is `0.0830`.

The relative error is the absolute error divided by the area value: `0.0311`.

# Problem 4

```python
measurements = [12, 10, 14, 16, 14]
mean = lambda it: (sum(it)/len(it))
stddev = lambda it: (sum([(x - mean(it))**2 for x in it])/(len(it)-1))**0.5
```

Log:

```python
>>> measurements = [12, 10, 14, 16, 14]
>>> mean = lambda it: (sum(it)/len(it))
>>> stddev = lambda it: (sum([(x - mean(it))**2 for x in it])/(len(it)-1))**0.5
>>> mean(measurements)
13.2
>>> stddev(measurements)
2.2803508501982757
```

a. The mean is `13.2 mm`

b. The standard deviation is `2.2803 mm`

# Problem 5

```python
rel_err = lambda m, error_m, e, error_e, h, error_h: \
  ((error_m / m)**2 + (4 * error_e / e)**2 + (2 * error_h / h)**2)**0.5
# simplified
rel_err = lambda relative_error_m, relative_error_e, relative_error_h: \
  (relative_error_m**2 + (4 * relative_error_e)**2 + \
  (2 * relative_error_h)**2)**0.5
```

Log:

```python
>>> rel_err = lambda m, error_m, e, error_e, h, error_h: \
...   ((error_m / m)**2 + (4 * error_e / e)**2 + (2 * error_h / h)**2)**0.5
>>> # simplified
... rel_err = lambda relative_error_m, relative_error_e, relative_error_h: \
...   (relative_error_m**2 + (4 * relative_error_e)**2 + \
...   (2 * relative_error_h)**2)**0.5
>>> rel_err(0.001, 0.002, 0.0001)
0.00806473806146238
```

The variables that don't have errors associated with them factor out of the equation for relative error. The result is expressed in terms of the relative errors of the variables. The relative error for the values given is `0.00806`.

# Problem 6

a and b.

![Graph with error bars](https://plot.ly/~jonnrb/63.png)

[Link to graph](https://plot.ly/~jonnrb/63/)

c.

Slope: `40.06 +/- 0.15`

Standard deviation: `0.5744`

d.

![Graph without error data](https://plot.ly/~jonnrb/65.png)

[Link to graph](https://plot.ly/~jonnrb/65/)

Slope `40.129 +/- 0.077`

Standard deviation: `0.5567`

The error taken into account is less and this affects the result. The standard deviation is lower and the error on the slope is lower.

e.

```python
s, L, A = 40.06, 1.07, 0.01
s_err, L_err, A_err = 0.15, 0.03, 0.05
cond = L / A / s
cond_err = ((s_err / s)**2 + (L_err / L)**2 + (A_err / A)**2)**0.5 * cond
```

Log:

```python
>>> s, L, A = 40.06, 1.07, 0.01
>>> s_err, L_err, A_err = 0.15, 0.03, 0.05
>>> cond = L / A / s
>>> cond_err = ((s_err / s)**2 + (L_err / L)**2 + (A_err / A)**2)**0.5 * cond
>>> cond
2.6709935097353967
>>> cond_err
13.355181257234447
```

Conductivity: `2.6709 +/- 13.3551`

## Problem 7

The error can be calculated by expressing `C_n` as a function of `V`. If `C_0` and `V_0` are precise, then the error propagation is only due to `V`. The result is the derivative of the function times the error in `V`.

```python
C_n = lambda V: (C_0 * V_0 / (V_0 + n * V))
C_n_err = lambda V, V_err: (n * V_err * C_0 * V_0 / ((V_0 + n * V)**2))
```

## Problem 8

![Graph of data](https://plot.ly/~jonnrb/67.png)

[Link to graph](https://plot.ly/~jonnrb/67/)

`s_0 = 0.3002 +/- 0.0030`

`v_0 = 0.869 +/- 0.033`

`g = 9.75 +/- 0.17`
