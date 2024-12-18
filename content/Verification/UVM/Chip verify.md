
- ###### System Verilog allows a base class handle to point to a dreived class instance for flexibility this is useful in Factory pattern as follows :

![[Pasted image 20241023094710.png]]
![[Pasted image 20241023094737.png]]

![[Pasted image 20241023094921.png]]
bb 
- what is the difference between TLM and RTL Modelling?

- UVM doesn't overwhelm  the verification engineer by many things like handshaking between driver & sequencer, or how sequence_item (transaction) applied by the driver to the DUT , these things done under the hood 

- the idea behind UVM is to enhance flexibility and reuse code so that the same testbench can be configured in different ways to build different components    

- why we shouldn't define the verification components directly in the Test class without Env?
	- this requires the test case writer to know how to configure the verification components
	- tests are not reusable because they rely on a specific verification components (Env) structure
	-  changing in the topology of the verification components (Env) requires updating many test files (test cases) 