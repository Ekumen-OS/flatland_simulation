
## Usage

To start the Flatland simulation, use the provided launch file:
```
roslaunch flatland_demo flatland.launch
```

### Configuration Options

* **multi_robot**: Whether or not to launch a multi-robot simulation.
        The number of robots and their initial positions are defined in config/robots.yml.
* **world_path**: Path to world.yaml file
* **use_flatland_viz**: Show visualization, pops the flatland_viz window and publishes 
    visualization messages, either true or false.
* **use_rviz**: Works only when use_flatland_viz=true, set this to disable flatland_viz popup
* **viz_pub_rate**: Rate to publish visualization in Hz, works only when show_viz=true
* **update_rate**:  The real time rate to run the simulation loop in Hz
impify map during vector tracing: 0=None (default), 1=moderately, 2=significantly
