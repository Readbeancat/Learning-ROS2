# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/admin/Documents/ROS2/C2_3/src/demo_cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/admin/Documents/ROS2/C2_3/build/demo_cpp

# Include any dependencies generated for this target.
include CMakeFiles/learn_shared_ptr.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/learn_shared_ptr.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/learn_shared_ptr.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/learn_shared_ptr.dir/flags.make

CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.o: CMakeFiles/learn_shared_ptr.dir/flags.make
CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.o: /home/admin/Documents/ROS2/C2_3/src/demo_cpp/src/learn_shared_ptr.cpp
CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.o: CMakeFiles/learn_shared_ptr.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/admin/Documents/ROS2/C2_3/build/demo_cpp/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.o -MF CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.o.d -o CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.o -c /home/admin/Documents/ROS2/C2_3/src/demo_cpp/src/learn_shared_ptr.cpp

CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/admin/Documents/ROS2/C2_3/src/demo_cpp/src/learn_shared_ptr.cpp > CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.i

CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/admin/Documents/ROS2/C2_3/src/demo_cpp/src/learn_shared_ptr.cpp -o CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.s

# Object files for target learn_shared_ptr
learn_shared_ptr_OBJECTS = \
"CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.o"

# External object files for target learn_shared_ptr
learn_shared_ptr_EXTERNAL_OBJECTS =

learn_shared_ptr: CMakeFiles/learn_shared_ptr.dir/src/learn_shared_ptr.cpp.o
learn_shared_ptr: CMakeFiles/learn_shared_ptr.dir/build.make
learn_shared_ptr: CMakeFiles/learn_shared_ptr.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/admin/Documents/ROS2/C2_3/build/demo_cpp/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable learn_shared_ptr"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/learn_shared_ptr.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/learn_shared_ptr.dir/build: learn_shared_ptr
.PHONY : CMakeFiles/learn_shared_ptr.dir/build

CMakeFiles/learn_shared_ptr.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/learn_shared_ptr.dir/cmake_clean.cmake
.PHONY : CMakeFiles/learn_shared_ptr.dir/clean

CMakeFiles/learn_shared_ptr.dir/depend:
	cd /home/admin/Documents/ROS2/C2_3/build/demo_cpp && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/admin/Documents/ROS2/C2_3/src/demo_cpp /home/admin/Documents/ROS2/C2_3/src/demo_cpp /home/admin/Documents/ROS2/C2_3/build/demo_cpp /home/admin/Documents/ROS2/C2_3/build/demo_cpp /home/admin/Documents/ROS2/C2_3/build/demo_cpp/CMakeFiles/learn_shared_ptr.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/learn_shared_ptr.dir/depend

