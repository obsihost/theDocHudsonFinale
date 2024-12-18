- If you have a SystemVerilog task that does not consume time, you should make it a void function , which is a function that does not return a value. Now it can be called from any task or function. For maximum fl exibility, any debug routine should be a void function rather than a task so that it can be called from any task or function.

- tasks are procedural block itself so we shouldn't have initial/always blocks inside 
- functions also cannot have initial or always blocks inside 


- the default direction of arguments and data type of a routine is input logic **Always declare the type and direction for every routine argument.**

- Verilog had a simple way to handle arguments: an input or inout was copied to a local variable at the start of the routine, whereas an output or inout was copied when the routine exited. No memories could be passed into a Verilog routine, only scalars.
ده معناه اني ماقدش  في ال verilog اباصي array ل routine , لكن في ال SV نقدر

 
**If any argument to your routine is something other than the default input type, specify the direction for all arguments**


===============================================================
## Return from routines ##

- **Verilog routines could only return a simple value such as a bit, integer, or vector. If you wanted to compute and return an array, there was no simple way. In System Verilog, a function can return an array, using several techniques.

#### the best 2 ways to return an array from a routine:

- passing the array by reference to the routine and the modification done on the array by the routine will affect the original array

![[Pasted image 20241009100809.png]]

- The last way for a function to return an array is to wrap the array inside of a class, and return a handle to an object


 
