
#### agent could be active (its driver and monitor components sends/receive transactions) or passive (only monitor is working)
- the agent specific configuration objects tell us these information about the agent

**because every thing in the environment is configurable so, the env components gets it's configurations first then send configurations to the agent**

- بدل ما كنت بخزن ال vif في ال config_db لا انا هحطه جوه ال configuration object و معاه شوية configurations تانيه خاصة بال agent & environment و جواهم بقا هستدعي ال object ده من الداتا بيز واخد منه ال vif و اديه لل monitor , driver 

- مين بقا اللي بي set ال configuration object في الداتا بيز ؟؟  ال Test component بي set object لكل env و ال env بت set واحد لكل agent

**env component  may also have a set of default sequences (a sequence is a patterns of sequence items)  (not recommended)**
- the env configuration object tell us these info about the env, the conf. object also tell us what type of coverage collector we shall use in this env and whether we shall instantiate a  scoreboard or not, and also provide info from the vritual sequences to the sequencer 

**Test Component do the following :**
	1- instantiate the env
	2- configure the env
	3- start sequence(s) to run using the env
	4- can utilize the factory to change env components types
	5- can also use the configuration object to change env components
	ال Test بيتحكم في ال Components type من خلال ال Factory عن طريق :
```uvm
old_coverage_collector::type_id::set_type_override(new_coverage_collector::get_type());
```
كده انا غيرت نوع ال Coverage Collector من غير ما اعمل اي حاجه في الكود بتاع ال env


- now we have many components, phases will help us managing the execution and work flow of these components

- start simulation phase used to open log files and other similar operations
- all phases methods are functions except the run_phase() it is a task since it consumes time

- note that the Test doesn't have a connect phase since it only instantiate the env and record configurations into the db 

![[Pasted image 20241030133255.png]]
- the argument phase that each phase method takes is to tell the method which phase we are currently in