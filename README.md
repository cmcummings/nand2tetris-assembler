# nand2tetris-assembler
Project 6 of the [Nand to Tetris](https://www.nand2tetris.org/course) course.

- Translates the "Hack" assembly language into its equivalent binary representation.
- Written in Python.





### Usage
Use `assembler.py` to generate .hack files (binaries) from .asm files (assembly code)
```
python3 assembler.py <.asm file>
```
```
Ex: python3 assembler.py examples/add/Add.asm
```
Use `comparer.py` to compare this assembler's output and the course's assembler's output.
```
python3 comparer.py <file1> <file2>
```
```
Ex: python3 comparer.py examples/add/Add.cack examples/add/Add.hack
```
Note that `assembler.py` generates `.cack` files to differentiate between this assembler's output and the course's assembler's output. 

The output file extension can be changed in `assembler.py`.
