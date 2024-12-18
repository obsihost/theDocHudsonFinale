
### Packages

- **Separate Scope**: Packages in SystemVerilog create a distinct scope for their contents (types, classes, functions, etc.). This encapsulation helps prevent naming conflicts and keeps related functionalities organized. this also done for classes, programs, functions, tasks ...etc

- **Explicit Import Required**: Because they are in a separate scope, you must explicitly import a package in any file that needs to access its contents. This is done using the `import` statement.
- **Compilation Order Matters**: Even if the package file is in the same directory, if you don't import it in the files that need its contents, those definitions won’t be recognized during compilation.

### Interfaces

- **Global Visibility**: When you declare an interface in a separate file (e.g., `Intf.sv`), it is treated as a global entity once compiled. The definitions become available across the entire simulation context, similar to Modules, Events.
- **Direct Use Without Import**: Interfaces can be used directly in any module or class without needing an explicit import or include statement, as long as the interface file is compiled as part of the overall project.
- **Included in Compilation**: When your project is compiled, if all files are included (via a build system or command line), the interface definitions are available to all files that require them.

### Summary

- **Packages**: Need to be imported in every file where their contents are used because they have a separate scope.
- **Interfaces**: Can be used directly across files without an import statement, as they are treated as globally visible once compiled.

===============================================================

### in System Verilog we cannot specify a return type for the constructor new() (even void) nor for tasks 

