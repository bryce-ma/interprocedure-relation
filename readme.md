# inter-procedure relation analysis for Python programs
<!-- TOC -->

- [inter-procedure relation analysis for Python programs](#inter-procedure-relation-analysis-for-python-programs)
  - [version 0.1](#version-01)
  - [version 0.2 (TODO)](#version-02-todo)
  - [Documentation & Slides](#documentation--slides)
  - [Demo](#demo)
    - [install requirments](#install-requirments)
    - [run demo from command line](#run-demo-from-command-line)
    - [or run demo with default file ./test/apple.py](#or-run-demo-with-default-file-testapplepy)
    - [run all tests](#run-all-tests)
    - [run specific test](#run-specific-test)
  - [build slides](#build-slides)

<!-- /TOC -->

## version 0.1

实现单个文件的过程间调用关系

##  version 0.2 (TODO)

支持多模块的Python项目源代码（多文件）

## Documentation & Slides

See [documentation](doc/documentation.md) and [presentation](doc/slides.pdf) under the `doc` dir.

## Demo

> Please use Python 3 to run all the tests and the demo

### install requirments

> python3 -m pip install graphviz
> python3 -m pip install astpretty

And also intall [Graphviz](https://www.graphviz.org/download/) into you local system to view the output

### run demo from command line

> python3 ./interpy/demo.py <inputfile.py>

### or run demo with default file ./test/apple.py
> python3 ./interpy/demo.py

### run all tests

> python3 -m unittest discover

### run specific test

> python3 -m unittest test.test_case

## build slides

> marp --pdf --html --allow-local-files doc/slides.md
