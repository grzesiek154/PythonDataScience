## **Vectorization**

First, let’s talk about **[vectorization](https://simpleprogrammer.com/vectorization)**. To do that, we need to define what a **vector** is. A **vector** is nothing more than a collection of items that are all the same type—typically only in one dimension. A collection in two dimensions is often called a matrix. When talking about a generic collection with *any* number of dimensions, you can use the word *array*. 

*Note: The vocabulary will vary a little from language to language but will always mean “some collection of values.”*

In data science cases, vectors are most often numbers, but other data types are possible as well. The idea behind vectorization is that if you’re careful, you can intuitively treat vectors just like single numbers.

Here is how vector math works:

In the same way you add two numbers together, you can add two vectors together, and the operation will be performed on an element-wise basis.

```python
import numpy as np


a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 1, 1, 5, 1])


a + b
# => [2, 3, 4, 9, 6]
```

We have now “vectorized” the addition operation, making it work for vectors. The NumPy library has a whole bunch of vectorized functions, including square root, absolute value, trigonometry functions, logarithmic functions, exponential functions, and more. 

These vectorized operations help take a lot of the mental load out of working with big collections of values when you basically want to do the same thing to all of them, treating the logic like you’re just working with one number. You don’t write any loops of your own!



## **Broadcasting**

OK, so far we’ve figured out that the idea behind vectorization is to make operations between two collections of the same size and shape as intuitive as operations between two single numbers. 

But what about when the collections are *different* shapes? 

This is when we apply a concept known as **broadcasting**. **Broadcasting** is the act of extending an array to a shape that will allow it to successfully take part in a vectorized calculation. Here are the rules:

- If the two arrays are the same length in a dimension, that dimension will be operated on in an element-wise manner. 
- If one array has some number in a dimension and the other array is only size 1 in that dimension, that value will be **broadcast**, and it will be used with each item in the other array. 
- If the two arrays are different sizes and neither is size 1, broadcasting can't be performed, and an error is thrown.

It’s a [tough concept](https://simpleprogrammer.com/data-science), so I think it’s time for some examples. First, let’s say we have one array that is 4×5 (four rows and five columns) and another one that is one row of five columns. 

![vectorization and broadcasting](https://lh4.googleusercontent.com/19MHGxpS8P-1x5Btxrryi1vpNEmreVBmOpiIEeS5R-akCKikE8VUErP0zfGqJat87PH9yFPUVisgAN42Cftm2awUremzUx9w0CGCL7K78xyPzztJ3UUcEI8ghQVV3gnSBDuiF4c)

We have two dimensions to consider. In Axis 0 (the row axis), one is length 4, and the other is length 1. The rules are satisfied for broadcasting, so we broadcast!

![img](https://lh3.googleusercontent.com/JycGkyXqKd8h2fXjegOLXALm98gpwi2vR2LF8oAO3QU5DWZySzNQ77WFRZFx2pAfFy2lv6f-uvVoL0Mvt1lj3XX6iioQowCNWU0-JlduVhAkDF1ySXp_1AuKa5NltJgOzT-199o)

Now, Axis 0 matches. Checking Axis 1 (the column axis), both have five elements. Since they match, we can perform the operation.

![img](https://lh4.googleusercontent.com/vs1lE9Xo6tY-OyfwVRiMqqY9hkLNTSQQ-ZMsyonWnrstkPxX4f9lo0poBAmPmvBARwCYtvMHsJno8rdfy80JsHvKLRBNM-fbgfTsR7PS2rqll-UYF5N6OZmcuJoCfYAA7njPLT0)

Let’s look at another example that is actually simpler but seems tricky at first:

![img](https://lh3.googleusercontent.com/ij8QDNbExigCTwYy2kk9Cn0Ryqt-mRstQQgJkGn4AM2h4wUWiTFOQQBuB3M-0hQAXn0THm47-keUPxrYjj-7YTEpMpcZX3JFHCWDSSpUfDXdVsEEfxNbEyYcK23eOcMSkxBwXxs)

Just a regular number? Yes! You can think about this like a tiny 1x1x1 … array. It will be broadcast in as many axes as needed. In this case, we only need one. 

![broadcasting](https://lh5.googleusercontent.com/IW9CkPcbasCVFSYo0V63Vjc8Pgua1dFWDcA2wBUvmD21dMaX7yJYoWDL4xId91tJgnakcJKkSXevmNNVGrRwtZagl9asbYK_QzmlFtm6qkcDDbnA9tbeMcDqrR3AqGUy2DQpGEo)

OK. We’ve covered a little bit of what these concepts mean, how they work, and what they entail. But now it’s time to look at how we can use them and why we would even need to know about them. We’re going to go through an example that shows just how clean and fast they can make our data analysis code. By doing just a little bit of data-shaping setup, we can set ourselves up to knock the analysis out of the park with one simple, sweet line of logic.