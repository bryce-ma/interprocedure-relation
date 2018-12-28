# InterPy

> inter-procedure relation analysis for Python programs

<!-- TOC -->

- [InterPy](#interpy)
  - [Four passes](#four-passes)
  - [TODOs](#todos)

<!-- /TOC -->

## Four passes

![](passes.png)

## TODOs

InterPy can not statically determine the types of return values from a method(or funcition), can in some simple cases but not in some complex cases, because of the DYNAMIC typing feature of Python. So we need type annotations or type inference to get the type information in order to solve this. Need to do this afterwards.

The current vesion, `0.1`, support single python file analysis only. We can solve this through handling the `import` syntax. Need to do this afterwards.




