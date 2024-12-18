
- suppose we have 3 modules TOP, Operations , Alu 
- we have write permission only on the TOP, and we can only instantiate Operations & Alu in the top
- we want to make an Alu instance inside the Operations, HOW???
- the solution is bending (نربط) each Operations Instance with Alu Instance 

![[Pasted image 20240926024846.png]]

**Note**
        x1,x3,x2 must be declared inside the Operations Module