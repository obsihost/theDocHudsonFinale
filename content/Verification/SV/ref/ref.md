
- In SystemVerilog, you can specify that an argument is passed by reference, rather than copying its value. This argument type, ref

- كل اللي بتعمله ال ref انها بتباصي refrence (address) بيشاور علي ال Variable نفسه بدل ما تاخد copy منه و تباصيها لل function 
- **ref ports must be connected to variables (reg bit logic .. etc) not nets(wire, tri-state ... etc) nor constant values nor expressions
 
- مميزات ال <span style="color:rgb(255, 0, 0)">ref argument type (Direction)</span> <span style="color:rgb(255, 0, 0)"></span>:
	- it pass the argument to a routine by reference which means it not copies the value o the function stack, but it pass the address (reference) of the original version of the variable
	- a task can modify a variable and is instantly seen by the calling function.

**in order to pass a ref argument to a routine it must be automatic routine**

**Always use ref when passing arrays to a routine for best performance. If you don’t want the routine to change the array values, use the const ref type, which causes the compiler to check that your routine does not modify the array.**

**SystemVerilog allows you to pass array arguments without the ref direction, but the array is copied into the stack of that routine, which an expensive operation for all but the smallest arrays.**
