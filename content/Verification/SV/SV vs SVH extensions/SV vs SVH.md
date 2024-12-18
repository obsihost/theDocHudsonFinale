

![[Pasted image 20241216121257.png]]

### **When to Use `.sv` vs. `.svh`**

- Use `.sv` for **functional code** that defines modules, interfaces, or testbenches.
- Use `.svh` for **reusable definitions** or **configuration** that multiple `.sv` files will include.

### **Practical Considerations**

- **Avoid cyclic dependencies**: Be cautious when including `.svh` files to prevent circular inclusions.
- **Organize headers logically**: Keep macros and global parameters in `.svh` files for consistency and maintainability.
- **Simulator behavior**: Some simulators might not distinguish between `.sv` and `.svh`, but following the convention makes your project more maintainable and readable.

-  you **must explicitly include `.svh` files** using the include directive, even if they are in the same directory as the`.sv`file. The SystemVerilog compiler does not automatically process`.svh`files unless they are explicitly included. This is because`.svh`files are considered **header files**, and they are not standalone compilable units like`.sv` files.