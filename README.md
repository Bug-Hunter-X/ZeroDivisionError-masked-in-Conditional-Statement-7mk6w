# ZeroDivisionError Masked in Conditional Statement

This repository demonstrates a subtle error in Python where a `ZeroDivisionError` is masked within a conditional statement.

The code in `bug.py` attempts to handle the case where the input `a` is zero, but due to an error in logic, it still results in a `ZeroDivisionError`.  The solution in `bugSolution.py` shows how to correctly handle this condition to prevent the exception.

## How to Reproduce

1. Clone this repository.
2. Run `bug.py` with an input of `a=0`. You'll observe a `ZeroDivisionError`. 
3. Run `bugSolution.py` to see the corrected version.