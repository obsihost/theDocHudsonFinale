
## 5 important regions ##

	1- Active (blocking assignment)
	2- In-active region (#0)
	3-NBA (<=)
	4- Reactive region (all procedural code in program block scheduled here)
	5- Re-NBA (all non-blobking assignment in program blocks <= scheduled here)


![[Pasted image 20241006150801.png]]

===============================================================
### Program construct ###

- هدف ال program block انه يمنع ال Racing بينما هدف ال clocking block هو ال synchronization 

- بالنسبه لل Program block كل ال statements اللي جواه بيتم اعتبارها في ال Re-active region يعني
بعد ما ال module (DUT) يكون خلص حساباته 
- بمعني ان ال test bench مش بيقدر ي sample ولا ي drive السيجنالز الا بعد ما ال DUT يخلص دنيته و ده بيمنع ال Racing 

- **events in the Observed and Reactive regions can trigger further design events in the Active region in the current cycle.

- the program block, running in the Reactive region, generates the stimulus written at a slightly higher level of abstraction, using cycle-by-cycle timing instead of worrying about individual clock edges. that is applied to the DUT, which is then evaluated in the Active region during the same time slot. The DUT evaluates its logic and drives its outputs, which are the inputs to the testbench through the clocking blocks. These are then sampled in the Postponed region and the cycle repeats.

- #### you can remember this by imagining that the clocking block inserts a synchronizer between the design and testbench

- ### Always Blocks not Allowed in a Program Block 
	- a testbench (Program block) has the steps of initialization, stimulate and respond to the design, and then wrap up simulation. An always block that runs continuously would not work.
-


===============================================================

### Immediate assertion ###

- as normal if conditions it is evaluated and executed in the active region

===============================================================