
- these are the two customization mechanisms used in UVM, Test can use one of them to modify components types without changing the env code 

### config_db performance

- the config_db can have a substantial impact on the performance so its recommended to be as efficient as possible (try to avoid *), and minimizes the no. of set() and get() calls

- an example to minimizes the no. of set() and get() calls the agent get its configuration and instead of set it again and do get in the driver/monitor the agent may set them directly after the driver & monitor built 