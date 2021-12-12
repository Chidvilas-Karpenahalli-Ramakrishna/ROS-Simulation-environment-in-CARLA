# Developing a simulation environment in CARLA 

Welcome to this repository. Here we will see how to setup CARLA simulator, install ROS and how to integrate ROS-bridge. The repository also contains a basic python script to connect to CARLA simulator, attach sensors to the EGO vehicle and gather data from CARLA simulator. We will also see how to use basic ROS commands to control Ego vehicle in CARLA environment. Some know issues associated with using CARLA and ROS are documented as **Known issues:** under each section. These will be updated in the repository as more issues are encountered. Some common issues associated with CARLA and their solutions can be found in [CARLA github repository](https://github.com/carla-simulator/carla/issues).


## Software Versions:
The following versions are used in the present setup.

- **Operating System:** Ubuntu 20.04.2 LTS Focal Fossa
- **Anaconda:** 2021.05
- **Python:** 3.7.10
- **CARLA simulator:** 0.9.11
- **ROS:** ROS1 Noetic Ninjemys


## Tested Hardware:
- **Processor:** Intel® Core™ i7-8565U CPU
- **GPU:** NVIDIA GeForce MX150
- **RAM:** 16 GB
- **Space requirements:** ~9 GB for CARLA (additional maps require more space) **+** ~3 GB for ROS Noetic **+** ~50 MB for ROS-bridge


## Project Overview:

- [Setup Conda virtual environment](#setup-conda-virtual-environment)
  - [Install anaconda](#install-anaconda)
  - [Create anaconda environment](#create-anaconda-environment)
- [CARLA](#carla)
  - [CARLA setup](#carla-setup)
  - [Testing CARLA installation](#testing-carla-installation)
  - [Running some python example files](#running-some-python-example-files)
- [ROS](#ros)
  - [ROS installation](#ros-installation) 
  - [ROS-bridge integration](#ros-bridge-integration)
  - [Test ROS-bridge integration](#test-ros-bridge-integration)


## Setup Conda virtual environment:
Anaconda virutal environment can be created for a specific version of Python and does not interfere with other installations on the computer. The CARLA version 0.9.11 is built for Python version 2.7.* and 3.7.\*. 

**NOTE:** CARLA can also be built from scratch for a specific version of Python. But the easiest way to use CARLA is to create a virtual environment with the compatible version of Python and use the package installation option for CARLA. If any other python version is desired, please build CARLA on your own. You can use [Linux build](https://carla.readthedocs.io/en/latest/build_linux/) or [Windows build](https://carla.readthedocs.io/en/latest/build_windows/) as a reference.

ROS Noetic is built for Python 3 and given the fact that Python 2 is now a legacy version and most of the present Python code is written in Python 3, the current setup is designed for Python 3.

### Install anaconda:
Follow the below steps to install Anaconda:

#### Steps:
1. Download Anaconda from [anaconda download page](https://www.anaconda.com/products/individual). Download the **64-Bit (x86) Installer** which is ~544 MB (.sh file).

2. Navigate to the folder containing the **.sh** file and right click and open terminal and enter `bash Anaconda3-<anaconda version downloaded>-Linux-x86_64.sh`. In case you have downloaded the 2021.05 version of anaconda the above code changes to `bash Anaconda3-2021.05-Linux-x86_64.sh`. Please change the code according to your downloaded file name.

3. This will be followed by a promt to press `Enter`. Then read the License Terms and Conditions (Which I am sure you won't). Scroll down and type `yes` to continue with the installation.

4. You will get one more promt asking to confirm the default location. This should be fine for most users. Press `Enter` to continue the installation.

5. After this you will get one more promt, `Do you wish the installer to prepend the Anaconda3 install location to PATH:`. Type `yes` and `Enter`.

6. After this you will get another promt to install VSCode editor. If you wish to use VSCode then type `yes` and follow the instructions or press `no`.

7. Check anaconda installation by typing `conda info` in the terminal. And to check the default packages installed in conda base type `conda list`.

### Create anaconda environment:
We need to create anaconda environment for Python version 3.7.*

#### Steps:
1. Use the format `conda create -n <conda environment name> python=3.7.10` to create a virutal environment. In our case the conda environment is named `carla_shk` and hence, the code changes to `conda create -n carla_shk python=3.7.10`. Change the command based on your requirement.

2. Activate the conda environment by typing `conda activate carla_shk`.

3. Deactivate conda environment by typing `conda deactivate`.


## CARLA:

### CARLA setup:

There are two ways of installing CARLA simulator. One is **Debian CARLA installation** and the other is **Package installtion**. Here, package installation is preferred as it is quite easy and meets our requirements. The options can be found in [CARLA quick start installation page](https://carla.readthedocs.io/en/0.9.11/start_quickstart/). 

Different versions of CARLA can be found in the [CARLA repository](https://github.com/carla-simulator/carla/blob/master/Docs/download.md). Here, we use **0.9.11 CARLA version** as it is the latest at the time of creating the repository. Please download [CARLA_0.9.11.tar.gz](https://github.com/carla-simulator/carla/releases/tag/0.9.11/) for Ubuntu. The file requires about 4 GB disk space. Once downloaded, extract the files to a folder named `carla`. When you explore the `carla` folder you should see a `CarlaUE4.sh` file which will be used to launch the CARLA simulator.

### Testing CARLA installation:

Open a terminal and navigate to `/carla` folder and export the Python path using `export PYTHONPATH=$PYTHONPATH:<path to carla folder>/carla/PythonAPI/carla/dist/carla-0.9.11-py3.7-linux-x86_64.egg` to export the Python 3.7 path. The typen `./CarlaUE4.sh` to launch the simulator and use `W`, `A`, `S` and `D` keys along with mouse `left button` to explore the simulation environment. There are two ways of launching the CARLA simulator. One is by using **Vulkan** and another is by **OpenGL**. All options can be found in [CARLA rendering options](https://carla.readthedocs.io/en/latest/adv_rendering_options/). Two examples for running CARLA server on a computer without a powerful GPU would be `./CarlaUE4.sh -opengl -quality-level=Low` **or** `./CarlaUE4.sh -opengl -windowed -ResX100 -ResY=400 -benchmark -fps=10`.

**Known issues:** If you encounter an error `carla module not found` when trying to `import carla`, this is due to the Python path. Please make sure `export PYTHONPATH=$PYTHONPATH:<path to carla folder>/carla/PythonAPI/carla/dist/carla-0.9.11-py3.7-linux-x86_64.egg` was correctly executed.


### Running some python example files:

CARLA provides some example Python files for testing. They can be found in `<path to carla folder>/carla/PythonAPI/examples`. You can start testing by running `spawn_npc.py` to spawn some traffic participants and later try `manual_control.py` to control EGO manually within the CARLA environment. To run this file first open a terminal and run the CARLA simulator as mentioned above. Once the CARLA simulator is open, it acts as a server to which clients can connect. In the current case, each Python file you run acts as a client. You can open a new terminal, navigate to the `examples` folder and run each python file. Before running any python files please activate the conda environment using `conda activate carla_shk` and export the Python path using `export PYTHONPATH=$PYTHONPATH:<path to carla folder>/carla/PythonAPI/carla/dist/carla-0.9.11-py3.7-linux-x86_64.egg`.  

A file named `shk_example.py` is provided here as an example to illustrate the data-gathering capabilities of CARLA. Upon exploring the file you will see that there exists an **Ego** vehicle which is a **Tesla model 3** (_change the car based on your preference ;-)_). The code is written to gather **RGB-alpha images** and **semantic segmentation images** from the **camera** sensor and to gathered data in **bird's eye view**. The gathered images are stored in a folder called `shk` in the same location of `shk_example.py` file. Before running the file please run `spawn_npc.py` provided by CARLA to add some traffic agents into the scene and then run `shk_example.py`. This runs the Ego autonomously in the CARLA environment and gathers data

`shk_example.py` can be modified to feed gathered data from sensors directly to a machine learning algorithm rather than storing in local disk. Please keep a track of `frames per second (fps)` and make sure your machine learning algorithm can handle the `fps` of CARLA simulator.


## ROS:

**Robotics Operation System (ROS)** helps us develop robotics applications. CARLA can be integrated with **ROS bridge** which enables two-way communication with CARLA server. This means that any information from CARLA gets transferred to ROS topics and using ROS, commands can be transferred to CARLA as well. Here, we conduct a simple demonstration where we make the Ego vehicle in CARLA to go in circles. To install and integrate ROS-bridge, first ROS needs to be installed. Please refer to [CARLA ROS-bridge](https://carla.readthedocs.io/en/0.9.11/ros_installation/) for detailed information.

**Note:** Please make sure you change the version at the bottom right corner in the website to **0.9.11**. 

### ROS installation:
Please note that to use the latest version of ROS i.e. ROS Noetic, all softwares should match. ROS Noetic works only on Ubuntu 20.04 Focal Fosa. Lower versions of Ubuntu don't support ROS Noetic. ROS Noetic is supported by CARLA 0.9.11 and it allows us to work on Python 3. 

A detailed installation instruction for ROS Noetic can be found on the [ROS website](http://wiki.ros.org/noetic/Installation/Ubuntu). The following [Youtube video](https://www.youtube.com/watch?v=PowY8dV36DY) can be used for reference. Please check your ROS installation before moving forward with the ROS-bridge installation and integration.


### ROS-bridge integration:
Once ROS Noetic is installed, please refer to [CARLA website](https://carla.readthedocs.io/en/0.9.11/ros_installation/) for installation instructions. Please follow the easy and straight-forward instructions for installation from **Source repository** within the same conda virtual environment `carla_shk`. 

**Note:** Please make sure to replace **Kinetic** with **Noetic** in all relevant places during installation. 


### Test ROS-bridge integration:

**Known issue 1:** Before testing ROS-brige, it is important to bring to your notice that some packages might **not** be installed while installing the required ROS dependencies from the previous step. If the testing throws an error saying **\<some package> missing**, please manually install the relevant package using **conda installation** or **pip installation** within the conda environment.

**Known issue 2:** Please also note that trying to run ROS using **ZSH** will cause errors. Please use **bash** terminal in Ubuntu to execute all commands.

##### Steps:

1. Open the **first** terminal and activate the conda environment by typing `conda activate carla_shk`. Then export the Python path using `export PYTHONPATH=$PYTHONPATH:<path to carla folder>/carla/PythonAPI/carla/dist/carla-0.9.11-py3.7-linux-x86_64.egg`. Navigate to the `carla` folder and press `./CarlaUE4.sh -opengl -quality-level=Low` or use any other rendering option to open CARLA simulator. Keep the simulator running as this is the server. 

2. Open a **second** terminal and activate the conda environment by typing `conda activate carla_shk`. Then export the Python path using `export PYTHONPATH=$PYTHONPATH:<path to carla folder>/carla/PythonAPI/carla/dist/carla-0.9.11-py3.7-linux-x86_64.egg`. Now add the path for ROS bridge repository by typing `source ~/carla-ros-bridge/catkin_ws/devel/setup.bash`.

**Known issue:** Please make sure that you don't set the source path permanently as this would interfere with other workspaces.

Start **rviz** by typing `roslaunch carla_ros_bridge carla_ros_bridge_with_rviz.launch`. Now you should see a new rviz window.  

3. Open a **third** terminal and then activate the conda environment by typing `conda activate carla_shk`. Then export the Python path using `export PYTHONPATH=$PYTHONPATH:<path to carla folder>/carla/PythonAPI/carla/dist/carla-0.9.11-py3.7-linux-x86_64.egg` and then add the source by typing `source ~/carla-ros-bridge/catkin_ws/devel/setup.bash`. Now navigate to `<path to PythonAPI>/PythonAPI/examples`. Now run **manual_control.py** by typing `python manual_control.py --rolename=ego_vehicle`. This opens a Pygame environment where we see our EGO vehicle. 

**Known issue:** `--rolename=ego_vehicle` needs to be added or else the execution won't work as **rviz** requires one Ego vehicle.

4. Open a **fourth** terminal and then activate the conda environment by typing `conda activate carla_shk`. Then export the Python path using `export PYTHONPATH=$PYTHONPATH:<path to carla folder>/carla/PythonAPI/carla/dist/carla-0.9.11-py3.7-linux-x86_64.egg` and then add the source by typing `source ~/carla-ros-bridge/catkin_ws/devel/setup.bash`. Now type `rostopic pub -1 /carla/ego_vehicle/vehicle_control_cmd carla_msgs/CarlaEgoVehicleControl "{throttle: 1.0, steer: 0.0}"`. This keeps the throttle at max i.e. **1** and makes Ego to accelerate straight from its current position.

Press `ctrl + c` to exit execution and in the same terminal type `rostopic pub -1 /carla/ego_vehicle/vehicle_control_cmd carla_msgs/CarlaEgoVehicleControl "{throttle: 1.0, steer: 1.0}"`. This keeps the throttle at max i.e. **1** and also keeps steering at max to the right i.e. **1.0**. This makes the Ego to drive in circles :-)

This was a simple demonstration showing the capabilities of using ROS and ROS bridge with CARLA simulator. Plese make sure to export Python path and source the ROS bridge reppo in every terminal you work with.
