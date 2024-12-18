
- In General when declaring a variable as Static, that means it will remain in its memory for the entire simulation time (it will not be de-allocated)

 - و بالتالي مشكلة ال static routines اني لو عملت اكتر من call لنفس ال routine ان كل ال calls دي هيشتغلو في نفس ال memory space 
the simulator will not create separate stack for each call but he will reserve a shared memory space that used by all all calls 
-وبالتالي ده يؤدي ان يحصل
conflict between the different calls occurred concurrently because they share the same copies of local variables 

- In Verilog-1995, if you tried to call a task from multiple places in your testbench, the local variables shared common, static storage, and so the different threads stepped on each other’s values. In Verilog-2001 you can specify that tasks, functions, and modules use automatic storage, which causes the simulator to use the stack for local variables.


===============================================================
## Automatic solve the problem ##

- if we declared a routine as automatic the simulator will create a separated stack for each routine call even if the calls occurred concurrently , that will prevent the conflict happens in case of static routines


**In SystemVerilog, routines still use static storage by default, for both modules and program blocks. You should always make program blocks (and their routines) use automatic storage by putting the automatic keyword in the program statement.**


===============================================================

## Initialization of Variables in static routine

- when you try to initialize a local variable in a declaration, as it is actually initialized before the start of simulation **(during the elaboration phase)**. The general solution is to avoid initializing a variable in a declaration to anything other than a constant. Use a separate assignment statement to give you better control over when initialization is done.

### example that produces incorrect behavior ###
```
function static int calculate_value(); 
	int x = $random; // Initialization in declaration (executed one)
	return x + 5;
endfunction
```

 - المشكله ان في ال static routines احنا قولنا ان كل routine بيكون لها memory space و ال space ده بيكون shared بين كل ال calls بتاعت ال routine و بالتالي اي variable جوه ال routine بيتعرف (declared) مره واحده فقط في ال elaboration phase
 - بعض ال simulators بيديلك error في الحلاه دي
 

- طب ايه الحل ؟ في حلين 
- اولهم اني افصل ال declaration عن ال initialization  ده هيخلي مع كل call ال inهtialization يتنفذ
```
function static int compute_value();
	int x;           //occure in elaboration
	x = some_signal; //occure in simulation not elaboration
	x + 5;
endfunction
```

- تاني حل اني اخلي ال routine او ال block (program/module) يكون automatic 
- ده هيخلي ال declaration يحصل مع كل call مش مره واحده في ال elaboration زي ال static

```
function autonatic int compute_value();
	int x;           //executed for each call
	x = some_signal; //executed for each call
	x + 5;
endfunction
```
