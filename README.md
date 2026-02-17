# Barracuda Jetson Workspace

## Description

This is a ROS2 Humble workspace designed to run on the Jetson AGX Orin for the USC Robosub team's Barracuda autonomous underwater vehicle (AUV). This workspace serves as the central development environment for all ROS2 packages used in the Barracuda project.

## Prerequisites

- Ubuntu 22.04 (Jammy Jellyfish)
- ROS2 Humble Hawksbill installed
- Git

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/usc-robosub/barracuda_jetson_ws.git
   cd barracuda_jetson_ws
   ```

2. **Initialize and update git submodules:**
   ```bash
   git submodule update --init --recursive
   ```
   
   This will pull all ROS2 packages that are added as submodules in the `/src` directory.

3. **Install dependencies:**
   ```bash
   rosdep install --from-paths src --ignore-src -r -y
   ```

4. **Build the workspace:**
   ```bash
   colcon build
   ```

5. **Source the workspace:**
   ```bash
   source install/setup.bash
   ```

## Workspace Structure

```
barracuda_jetson_ws/
├── src/                 # ROS2 packages (git submodules)
├── build/               # Build artifacts (auto-generated, git-ignored)
├── install/             # Installation directory (auto-generated, git-ignored)
├── log/                 # Build logs (auto-generated, git-ignored)
└── README.md            # This file
```

## Usage

### Building Specific Packages

To build only specific packages:
```bash
colcon build --packages-select <package_name>
```

### Cleaning the Workspace

To clean build artifacts:
```bash
rm -rf build/ install/ log/
```

### Running Nodes

After sourcing the workspace, you can run any ROS2 node from the packages:
```bash
ros2 run <package_name> <node_name>
```

## Adding New Packages

To add a new ROS2 package as a submodule:

1. Navigate to the src directory:
   ```bash
   cd src
   ```

2. Add the package as a git submodule:
   ```bash
   git submodule add <repository_url> <package_name>
   ```

3. Update the main repository:
   ```bash
   cd ..
   git add .gitmodules src/<package_name>
   git commit -m "Add <package_name> as submodule"
   git push
   ```

## Updating Packages

To update all submodules to their latest commits:
```bash
git submodule update --remote --merge
```

## Troubleshooting

### Build Failures
- Ensure all dependencies are installed using `rosdep`
- Check that ROS2 Humble is properly sourced: `source /opt/ros/humble/setup.bash`
- Verify that all submodules are initialized and updated

### Missing Packages
- Run `git submodule update --init --recursive` to ensure all submodules are pulled

## Contributing

When contributing to packages within this workspace:
1. Make changes in the specific package's submodule directory
2. Commit and push changes in the submodule repository
3. Update the parent workspace to reference the new submodule commit
4. Push changes to this workspace repository