## Flatland simulation for multi-robot

## :green_book: Description
This repository contains a Flatland simulation using ROS Melodic to spawn and control multiple robots. Rosbags can be recorded for each simulated instance and replayed to control multiple robots.


### :rocket: Usage

### Prepare your workspace

This container has a submodule dependency on the Flatland simulator repo, before running, make sure to sync your submodules:

```sh
git submodule update --init --recursive
```

#### Building image and running container
The package is built to run inside a Docker container that ensures all dependencies and requirements are met. To build the docker image run:
```sh
./docker/build.sh
```
A specific image name can be set using:

```sh
./docker/build.sh -i my_fancy_image_name
```
Then the docker container can be run via:
```sh
./docker/run.sh
```

Once the container is up and running resolve all remaining dependencies by running `rosdep`

```sh
rosdep install -i -y --rosdistro melodic --from-paths src
```

Finally the project is ready to be built:

```sh
catkin_make
```

### Launching the simulation
To start the Flatland simulation, begin by sourcing the ROS workspace:

```sh
source devel/setup.bash
```

Then launch the simulation using the provided launch file:

```sh
roslaunch flatland_demo flatland.launch
```

The launchfile accepts multiple configuration options"
##### Configuration Options

* **multi_robot**: Whether or not to launch a multi-robot simulation.
        The number of robots and their initial positions are defined in [config/robots.yml](/flatland_demo/config/robots.yml).
* **world_path**: Path to world.yaml file
* **use_flatland_viz**: Show visualization, pops the flatland_viz window and publishes
    visualization messages, either true or false.
* **use_rviz**: Works only when use_flatland_viz=true, set this to disable flatland_viz popup
* **viz_pub_rate**: Rate to publish visualization in Hz, works only when show_viz=true
* **update_rate**:  The real time rate to run the simulation loop in Hz

### Replaying rosbags

In order to control multiple robots, previously recorded trajectories can be replayed by running;
```sh
roslaunch flatland_demo play_n_rosbags.launch nr:=N
```

Where `nr` defines the amount of rosbags to be replayed. Recorded rosbags are stored inside `scripts/rosbags` folder.

## Contributing

Contributions are always welcome. If you're interested in contributing, please refer to the [CONTRIBUTING](/CONTRIBUTING.md)
### Pre-commit configuration

This projects uses pre-commit hooks for linting. To install and make sure they are run when committing:
```sh
python3 -m pip install -U pre-commit
pre-commit install
```

If you want to run the linters but still not ready to commit you can run:

```sh
pre-commit run --all-files
```
## Code of Conduct

The free software code of conduct fosters an inclusive, respectful community for contributors by promoting collaboration and mutual respect. For more details, refer to the full document [Code of Conduct](CODE_OF_CONDUCT.md).
