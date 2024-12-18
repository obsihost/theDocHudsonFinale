
### separation of declaration and construction

- By separating declaration and construction, you gain **control** over when and how objects are created. You can declare the handle early (perhaps when you create the testbench), but you don’t need to create the object until you actually need it.
- This allows you to use conditional logic, configuration settings, or other runtime information to decide **what type** of object to create or when exactly to create it, doesn't waste memory by only using it when it is needed.

### separation of construction and Randomization

- By separating construction and randomization, you allow for **modification** of the object’s properties before randomization. For example, you might want to set certain fields to fixed values or apply specific constraints based on the test scenario **before** randomizing the rest of the fields.
- It also allows you to work with **blueprints** or **templates**. For instance, you might have a base transaction object that is partially configured, and you create copies of it to apply specific changes or constraints before randomization. This approach aligns with the "blueprint pattern," where you stamp new objects based on a predefined template (blueprint) and then customize or randomize them further.


===============================================================
## why do we push a new copy to the queue ?

![[Pasted image 20241012034145.png]]

### 1- to solve the classic OOP mailbox bug

##### what happens if we push the same reference every time to the queue without creating a copy

- If you modify the object (e.g., update its fields or randomize it), **all** the references in the mailbox will point to this **modified** object, not the version that was initially put into the mailbox.
- As a result, if your testbench retrieves objects from the mailbox expecting them to be different transactions, it will instead receive the same object with possibly the most recent modifications.

### 2- to benefit form the randc variables charactristics

##### when we push a new copy and keep the original copy (blueprint) to be randomized again and again the history of the randc variables are kept and continued


===============================================================

## Phases of the testbench

![[Pasted image 20241012040410.png]]

![[Pasted image 20241012040428.png]]


- now if we want to inject bad transactions we only need to change the blueprint (may be change some constraints)
![[Pasted image 20241012044925.png]]


![[Pasted image 20241012045025.png]]


**Note that if you define a constraint in an extended class with the same name as one in the base class, the extended constraint replaces the base one. This allows you to change the behavior of existing constraints.
