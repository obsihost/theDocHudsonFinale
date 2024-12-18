
1. **Ports** act as the caller to the API and are used by components to initiate transactions.
2. **Exports** serve as connectors, forwarding method calls to the appropriate implementation. Exports themselves do not implement the API; they only provide a way for ports to connect to an implementation.
3. **Imps (Implementations)** are where the actual API (such as `write()`, `put()`, or `get()`) is implemented.

### port 

- square
- used to initiate and forward packets from the lower layer in the hierarchy to the top layer
- port also called the initiator
- port is an object that has set of APIs (methods) used in the communication 
- when the API is called from the initiator the code of that API supplied by the imp will be executed  

## Analysis Port

- diamond
- used for broadcasting, sending the transaction to multiple components
- **all the receiving component have a pointer to the transaction so if one change the transaction the other components will see that change, so it is recommended to make a copy to do changes**
- 
### export

- circle
- are used to forward packets from the top layer  in the hierarchy to the lower layer'

- in other words it forwards the implementation of the API to other classes

### Imp
- used to receive packets and implement the API to process that packet
- circle

![[Pasted image 20241101162938.png]]

![[Pasted image 20241101163031.png]]

![[Pasted image 20241101163054.png]]

- any component can act as a receiver by calling the get while the sending component must implement the get API to specify what to send 
- **connect() method is called using the sending instance, such as the componentA in the previous example**
- in other word connect() is called by the instance that initiates the communication



---

# TLM 2

- to support bus-based communication TLM2 includes generic payload which is a specialized transactions used for memory mapped bus-based systems

#### **TLM1's Pass-by-Value Concept**

In UVM, TLM1 methods (e.g., `write()`, `put()`, `get()`) are conceptually described as passing data by value. This means:

1. The **sending component** calls a method (`analysis_port.write(transaction)`), and the data (`transaction`) is passed to the **receiving components**.
2. Each receiving component gets its own "copy" of the transaction in theory, so they should be independent of one another.

---

#### **SystemVerilog Reference Semantics**

In practice, SystemVerilog objects are always passed by **reference**, not by value. Here's why:

- **Objects in SystemVerilog**: Objects (like your `bus_item`) are created dynamically and stored in memory. When you pass an object as an argument to a method, what is actually passed is a **reference** (or pointer) to the object, not the object itself.
- **Implication**: If one receiver modifies the object, the changes are visible to all other receivers that share the same reference.