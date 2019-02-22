// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/add/Add.asm

// Computes R0 = 2 + 3  (R0 refers to RAM[0])

@2
D=A
@3
D=D+A
@0
M=D
D
// Testing
@32767
AMD=D+A;JMP
0;JGT
0;JEQ
0;JGE
0;JLT
0;JNE
0;JLE
0;JMP
1;JMP

(20)
@20
0;JMP

(HELP)
@HELP