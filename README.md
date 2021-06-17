# Developing a simulation environment in CARLA 

Welcome to this repository where we will see how to setup CARLA simulator, install ROS and how to integrate ROS-bridge. The repository also contains a basic python script to connect to CARLA simulator, attach sensors to the EGO vehicle and gather data from CARLA simulator. And we will also see how to use basic ROS commands to control the agents in CARLA environment. The final section deals with some knows issues and solutions. This section will be updated as and when new issues are found.

## Software Versions:
The following versions are used for the present setup.
- **Operating System:** Ubuntu 20.04.2 LTS Focal Fossa
- **Anaconda:** 2021.05
- **Python:** 3.7.10
- **CARLA simulator:** 0.9.11
- **ROS:** ROS1 Noetic Ninjemys

## Tested Hardware:
- **Processor:** Intel® Core™ i7-8565U CPU
- **GPU:** NVIDIA GeForce MX150
- **RAM:** 16 GB
- **Space requirements:** ~9 GB for CARLA (additional maps require more space) **+** ~3 GB for ROS Noetic **+** ~50 MB for ROS-bridge **+** ~6-10 GB for Anaconda (depends on additional packages installed) 

## Tasks:
- [x] Setup Conda virtual environment
- [x] Download, install and run CARLA simulator
- [x] ROS installation
- [x] ROS-bridge integration
- [x] Develop basic python scripts to gather data from sensors in CARLA environment
- [x] Test ROS commands to control CARLA agents
- [x] Knows issues 


## Project Overview:
- [Setup Conda virtual environment](#setup-conda-virtual-environment)
  - [Install anaconda](#install-anaconda)
  - [Create anaconda environment](#create-anaconda-environment)
- [CARLA setup](#carla-setup)
- [ROS](#ros)
  - [ROS installation](#ros-installation) 
  - [ROS-bridge integration](#ros-bridge-integration)
- [Gather data from CARLA](#gather-data-from-carla)
- [Test ROS-bridge integration](#test-ros-bridge-integration)
- [Known issues](#known-issues)


## Setup Conda virtual environment:
Anaconda virutal environment can be created for a specific version of Python and does not interfere with other installations on the computer. The CARLA version 0.9.11 is built for Python version 2.7.* and 3.7.* and does not work for other Python versions.

**NOTE:** CARLA can also be built from scratch for a specific version of Python. But the easiest way to use CARLA is to create a virtual environment with the compatible version of Python and use the package installation option for CARLA.

ROS Noetic is built for Python 3 and given the fact that Python 2 is now a legacy version and most of the present Python code is written in Python 3, the setup is defined for using Python 3 for all packages. This also enables us to have just one virtual environment with one specific Python version. In our case Conda environment serves the purpose.

### Install anaconda:
Follow the below steps to install Anaconda:

#### Steps:
1. Download Anaconda from [anaconda download page](https://www.anaconda.com/products/individual). Download the `64-Bit (x86) Installer` which is ~544 MB (.sh file).
2. Navigate to the folder containing the `.sh` file and right click and open terminal and enter `bash Anaconda3-<anaconda version downloaded>-Linux-x86_64.sh`. In case you have downloaded the 2021.05 version of anaconda the above code changes to `bash Anaconda3-2021.05-Linux-x86_64.sh`. Please change the code according to the downloaded file name.
3. This will be followed by a promt to press `Enter`. Then read the License Terms and Conditions (Which I am sure you won't). Scroll down and type `yes` to continue with the installation.
4. You will get one more promt asking to confirm the default location. This should be fine for most users. Press `Enter` to continue the installation.
5. After this you will get one more promt, `Do you wish the installer to prepend the Anaconda3 install location to PATH:`. Type `yes` and Enter.
6. After this you will get another promt to install VSCode editor. If you wish to use VSCode then type `yes` and follow the instructions or else press `no`
7. Check anaconda installation by typing `conda info` in the terminal. And to check the default packages installed in conda base type `conda list`.

### Create anaconda environment:
We need to create anaconda environment for Python version 3.7.*

#### Steps:
1. Use the format `conda create -n <conda environment name> python=3.7.10`. In our case the conda environment is named `shk` and hence, the code changes to `conda create -n shk python=3.7.10`
2. Activate the conda environment by typing `conda activate shk`
3. Deactivate conda environment by typing `conda deactivate`


## CARLA setup:


## ROS:
  

### ROS installation:


### ROS-bridge integration:


## Gather data from CARLA:


## Test ROS-bridge integration:


## Known issues:

