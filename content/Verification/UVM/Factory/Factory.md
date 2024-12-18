

- factory is a place where things are made-up, also it is capable of producing new versions (updated versions) of the products

- in UVM factory is a centralized Location which creates class instances for you, so we don't call the class constructor by ourselves any more, the factory do it.

- It enables polymorphism and facilitates reusability by decoupling the creation of objects from their specific types.

- so all classes types must be registered in the factory, and then we create instances from our classes using a create() method called from the factory

- why we do that, because factory can maintain a type override list, so whenever we want to override an object to be of type one of its child the factory will modify all it's instances without our modifications in the code 

- factory return class instance 

- so we need to register the all the possible Classes in the factory, this is done by one of these 
```
	`uvm_object_utils(type);
	`uvm_component_utils(type);
```
- trohese macs also defines the create method for the passed class name to instantiate it when needed

![[Pasted image 20241018150056.png]]
- ال type_id ماهو الا Object من النوع uvm_object_registry/uvm_component_registry اللي بدوره يبحتوي علي ال create() method
- يبقا جوه ال class بتاعي اللي عايز اعمله registering في ال factory  هحط  واحده من ال macros اللي قولنا عليها علي حسب ال class من النوع object ولا uvm_component 
- ولما اجي اعمل منه instance مش هستخدم ال constructor بقا لا هستخدم ال create method 
- كده انا اقدر في اي وقت اغير نوع ال packet لاي class تاني بسهوله باني اغير ال arg بتاع ال macro