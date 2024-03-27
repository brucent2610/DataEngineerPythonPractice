# Introduction PEP8

**Ref:https://peps.python.org/pep-0008/**

**Python Enhancement Proposal (PEP):** A design document providing information to the python community or describing a new feature for python or its processes or environment.

# Overview of PEP8 Rules

**It's about style, not about program correctness**

- Format: Lay-out of code and comments
- Whitespace/punctuation: Indentation, quotes, operators,...
- Naming: Classes, functions, variables,...

**Note**

- Consistency with a style guide is important
- Consistency within a project is more important
- Consistency within a module or function is the most important

# Review PEP8

## Layout

- Indentation: 4 spaces per level
- Max. line length 79 characters
- 2 lines between top-level functions and classes
- 1 line between methods inside a class
- Use of spaces in expressions

## Imports

- Should be on separate lines
- Three groups, separated by blank lines

1. Standard library
2. Third-party libraries
3. Local application/library

## Naming

- Modules: short, lowercase names
- Classes: CapitalizedNaming
- Functions: lowercase_with_underscore
- Constants: ALL_CAPS
- Non-public names start with underscore

## Documentation

- Docstrings for all public modules, functions, classes and methods
- Guidelines for documentation are in PEP257

## Tools: Checkers

**pycodestyle:**

- check PEP8 rules
  **flake8**

- PEP8
- code smells
- complexity
  **pylint**

- very flexible, can check many things
- PEP8 checks are not as complete

## Tools: Fixing

**black**

- code formatter
  **reorder-python-import**

## Automation

- Most of these tools are used best in an automated workflow (CI/CD)
- A very popular option is to use the pre-commit framework (https://pre-commit.com)

# Document Your Project
