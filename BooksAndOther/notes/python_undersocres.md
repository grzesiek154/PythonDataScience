The various meanings and naming conventions around single and double underscores (“dunder”) in Python, how name mangling works and  how it affects your own Python classes.

![The Meaning of _ and __ Underscores in Python](https://dbader.org/static/figures/python-underscores.png)

Single and double underscores have a meaning in Python variable and  method names. Some of that meaning is merely by convention and intended  as a hint to the programmer—and some of it is enforced by the Python  interpreter.

If you’re wondering *“What’s the meaning of single and double underscores in Python variable and method names?”* I’ll do my best to get you the answer here.

In this article I’ll discuss the following five underscore patterns  and naming conventions and how they affect the behavior of your Python  programs:

- Single Leading Underscore: `_var`
- Single Trailing Underscore: `var_`
- Double Leading Underscore: `__var`
- Double Leading and Trailing Underscore: `__var__`
- Single Underscore: `_`

At the end of the article you’ll also find a brief “cheat sheet”  summary of the five different underscore naming conventions and their  meaning, as well as a short video tutorial that gives you a hands-on  demo of their behavior.

Let’s dive right in!

## 1. Single Leading Underscore: `_var`

When it comes to variable and method names, the single underscore  prefix has a meaning by convention only. It’s a hint to the  programmer—and it means what the Python community agrees it should mean, but it does not affect the behavior of your programs.

The underscore prefix is meant as a *hint* to another  programmer that a variable or method starting with a single underscore  is intended for internal use. This convention is [defined in PEP 8](http://pep8.org/#descriptive-naming-styles).

This isn’t enforced by Python. Python does not have strong  distinctions between “private” and “public” variables like Java does.  It’s like someone put up a tiny underscore warning sign that says:

> “Hey, this isn’t really meant to be a part of the public interface of this class. Best to leave it alone.”

Take a look at the following example:

```
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
```

What’s going to happen if you instantiate this class and try to access the `foo` and `_bar` attributes defined in its `__init__` constructor? Let’s find out:

```
>>> t = Test()
>>> t.foo
11
>>> t._bar
23
```

You just saw that the leading single underscore in `_bar` did not prevent us from “reaching into” the class and accessing the value of that variable.

That’s because the single underscore prefix in Python is merely an  agreed upon convention—at least when it comes to variable and method  names.

**However, leading underscores do impact how names get imported from modules.** Imagine you had the following code in a module called `my_module`:

```
# This is my_module.py:

def external_func():
    return 23

def _internal_func():
    return 42
```

Now if you use a *wildcard import* to import all names from the module, Python will *not* import names with a leading underscore (unless the module defines an [`__all__` list](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package) that overrides this behavior):

```
>>> from my_module import *
>>> external_func()
23
>>> _internal_func()
NameError: "name '_internal_func' is not defined"
```

By the way, [wildcard imports should be avoided](http://pep8.org/#imports) as they make it unclear which names are present in the namespace. It’s  better to stick to regular imports for the sake of clarity.

Unlike wildcard imports, regular imports are not affected by the leading single underscore naming convention:

```
>>> import my_module
>>> my_module.external_func()
23
>>> my_module._internal_func()
42
```

I know this might be a little confusing at this point. If you stick  to the PEP 8 recommendation that wildcard imports should be avoided,  then really all you need to remember is this:

> *Single underscores are a Python naming convention indicating a  name is meant for internal use. It is generally not enforced by the  Python interpreter and meant as a hint to the programmer only.*

## 2. Single Trailing Underscore: `var_`

Sometimes the most fitting name for a variable is already taken by a keyword. Therefore names like `class` or `def` cannot be used as variable names in Python. In this case you can append a single underscore to break the naming conflict:

```
>>> def make_object(name, class):
SyntaxError: "invalid syntax"

>>> def make_object(name, class_):
...     pass
```

In summary, a single trailing underscore (postfix) is used by  convention to avoid naming conflicts with Python keywords. This  convention is [explained in PEP 8](http://pep8.org/#descriptive-naming-styles).

## 3. Double Leading Underscore: `__var`

The naming patterns we covered so far received their meaning from  agreed upon conventions only. With Python class attributes (variables  and methods) that start with double underscores, things are a little  different.

A double underscore prefix causes the Python interpreter to rewrite  the attribute name in order to avoid naming conflicts in subclasses.

This is also called *name mangling*—the interpreter changes  the name of the variable in a way that makes it harder to create  collisions when the class is extended later.

I know this sounds rather abstract. This is why I put together this little code example we can use for experimentation:

```
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23
```

Let’s take a look at the attributes on this object using the [built-in `dir()` function](https://docs.python.org/3/library/functions.html#dir):

```
>>> t = Test()
>>> dir(t)
['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', '_bar', 'foo']
```

This gives us a list with the object’s attributes. Let’s take this list and look for our original variable names `foo`, `_bar`, and `__baz`—I promise you’ll notice some interesting changes.

- The `self.foo` variable appears unmodified as `foo` in the attribute list.
- `self._bar` behaves the same way—it shows up on the class as `_bar`. Like I said before, the leading underscore is just a *convention* in this case. A hint for the programmer.
- However with `self.__baz`, things look a little different. When you search for `__baz` in that list you’ll see that there is no variable with that name.

So what happened to `__baz`?

If you look closely you’ll see there’s an attribute called `_Test__baz` on this object. This is the *name mangling* that the Python interpreter applies. It does this to protect the variable from getting overridden in subclasses.

Let’s create another class that extends the `Test` class and attempts to override its existing attributes added in the constructor:

```
class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'
```

Now what do you think the values of `foo`, `_bar`, and `__baz` will be on instances of this `ExtendedTest` class? Let’s take a look:

```
>>> t2 = ExtendedTest()
>>> t2.foo
'overridden'
>>> t2._bar
'overridden'
>>> t2.__baz
AttributeError: "'ExtendedTest' object has no attribute '__baz'"
```

Wait, why did we get that `AttributeError` when we tried to inspect the value of `t2.__baz`? Name mangling strikes again! It turns out this object doesn’t even have a `__baz` attribute:

```
>>> dir(t2)
['_ExtendedTest__baz', '_Test__baz', '__class__', '__delattr__',
 '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__gt__', '__hash__', '__init__', '__le__',
 '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', '_bar', 'foo', 'get_vars']
```

As you can see `__baz` got turned into `_ExtendedTest__baz` to prevent accidental modification:

```
>>> t2._ExtendedTest__baz
'overridden'
```

But the original `_Test__baz` is also still around:

```
>>> t2._Test__baz
42
```

Double underscore name mangling is fully transparent to the  programmer. Take a look at the following example that will confirm this:

```
class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled

>>> ManglingTest().get_mangled()
'hello'
>>> ManglingTest().__mangled
AttributeError: "'ManglingTest' object has no attribute '__mangled'"
```

Does name mangling also apply to method names? It sure does—name mangling affects *all* names that start with two underscore characters (“dunders”) in a class context:

```
class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()

>>> MangledMethod().__method()
AttributeError: "'MangledMethod' object has no attribute '__method'"
>>> MangledMethod().call_it()
42
```

Here’s another, perhaps surprising, example of name mangling in action:

```
_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled

>>> MangledGlobal().test()
23
```

In this example I declared a global variable called `_MangledGlobal__mangled`. Then I accessed the variable inside the context of a class named `MangledGlobal`. Because of name mangling I was able to reference the `_MangledGlobal__mangled` global variable as just `__mangled` inside the `test()` method on the class.

The Python interpreter automatically expanded the name `__mangled` to `_MangledGlobal__mangled` because it begins with two underscore characters. This demonstrated  that name mangling isn’t tied to class attributes specifically. It  applies to any name starting with two underscore characters used in a  class context.

**Now this was a lot of stuff to absorb.**

To be honest with you I didn’t write these examples and explanations  down off the top of my head. It took me some research and editing to do  it. I’ve been using Python for years but rules and special cases like  that aren’t constantly on my mind.

Sometimes the most important skills for a programmer are “pattern  recognition” and knowing where to look things up. If you feel a little  overwhelmed at this point, don’t worry. Take your time and play with  some of the examples in this article.

Make these concepts sink in enough so that you’ll recognize the  general idea of name mangling and some of the other behaviors I showed  you. If you encounter them “in the wild” one day, you’ll know what to  look for in the documentation.

## ⏰ Sidebar: What’s a “dunder” in Python?

I’ve you’ve heard some experienced Pythonistas talk about Python or watched a few conference talks you may have heard the term *dunder*. If you’re wondering what that is, here’s your answer:

Double underscores are often referred to as [“dunders”](https://nedbatchelder.com/blog/200605/dunder.html) in the Python community. The reason is that double underscores appear  quite often in Python code and to avoid fatiguing their jaw muscles  Pythonistas often shorten “double underscore” to “dunder.”

For example, you’d pronounce `__baz` as “dunder baz”. Likewise `__init__` would be pronounced as “dunder init”, even though one might think it  should be “dunder init dunder.” But that’s just yet another quirk in the naming convention.

It’s like a *secret handshake* for Python developers 🙂

## 4. Double Leading and Trailing Underscore: `__var__`

Perhaps surprisingly, name mangling is *not* applied if a name *starts and ends* with double underscores. Variables surrounded by a double underscore  prefix and postfix are left unscathed by the Python interpeter:

```python
class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42

>>> PrefixPostfixTest().__bam__
42
```

However, names that have both leading and trailing double underscores are reserved for special use in the language. This rule covers things  like `__init__` for object constructors, or `__call__` to make an object callable.

These *dunder methods* are often referred to as *magic methods*—but many people in the Python community, including myself, [don’t like that](http://www.pixelmonkey.org/2013/04/11/python-double-under-double-wonder).

It’s best to stay away from using names that start and end with  double underscores (“dunders”) in your own programs to avoid collisions  with future changes to the Python language.

## 5. Single Underscore: `_`

Per convention, a single standalone underscore is sometimes used as a name to indicate that a variable is temporary or insignificant.

For example, in the following loop we don’t need access to the running index and we can use “`_`” to indicate that it is just a temporary value:

```python
>>> for _ in range(32):
...     print('Hello, World.')
```

You can also use single underscores in unpacking expressions as a  “don’t care” variable to ignore particular values. Again, this meaning  is “per convention” only and there’s no special behavior triggered in  the Python interpreter. The single underscore is simply a valid variable name that’s sometimes used for this purpose.

In the following code example I’m unpacking a `car` tuple into separate variables but I’m only interested in the values for `color` and `mileage`. However, in order for the unpacking expression to succeed I need to  assign all values contained in the tuple to variables. That’s where “`_`” is useful as a placeholder variable:

```python
>>> car = ('red', 'auto', 12, 3812.4)
>>> color, _, _, mileage = car

>>> color
'red'
>>> mileage
3812.4
>>> _
12
```

Besides its use as a temporary variable, “`_`” is a special variable in most Python REPLs that represents the result of the last expression evaluated by the interpreter.

This is handy if you’re working in an interpreter session and you’d  like to access the result of a previous calculation. Or if you’re  constructing objects on the fly and want to interact with them without  assigning them a name first:

```python
>>> 20 + 3
23
>>> _
23
>>> print(_)
23

>>> list()
[]
>>> _.append(1)
>>> _.append(2)
>>> _.append(3)
>>> _
[1, 2, 3]
```

## 📓 Python Underscore Naming Patterns – Summary

Here’s a quick summary or “cheat sheet” of what the five underscore patterns I covered in this article mean in Python:

| Pattern                                    | Example   | Meaning                                                      |
| ------------------------------------------ | --------- | ------------------------------------------------------------ |
| **Single Leading Underscore**              | `_var`    | Naming convention indicating a name is meant for internal use.  Generally not enforced by the Python interpreter (except in wildcard  imports) and meant as a hint to the programmer only. |
| **Single Trailing Underscore**             | `var_`    | Used by convention to avoid naming conflicts with Python keywords. |
| **Double Leading Underscore**              | `__var`   | Triggers name mangling when used in a class context. Enforced by the Python interpreter. |
| **Double Leading and Trailing Underscore** | `__var__` | Indicates special methods defined by the Python language. Avoid this naming scheme for your own attributes. |
| **Single Underscore**                      | `_`       | Sometimes used as a name for temporary or insignificant variables  (“don’t care”). Also: The result of the last expression in a Python  REPL. |