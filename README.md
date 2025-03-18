
# Learning-ROS2 学习笔记  

## 一、学习历程  

### 3 月 17 日  

#### 系统环境搭建  
- 下载并安装 Linux 系统虚拟机。  
- 将虚拟机系统升级至 **Ubuntu Linux - Jammy Jellyfish (22.04)**。  
  - 在升级过程中，掌握了切换镜像下载源的方法。  
  - 通过更换镜像源，软件包下载速度大幅提升，稳定性增强，为后续学习和开发工作筑牢根基。  
  - 了解不同的ROS2的版本号，最终选择ROS 2 Humble Hawksbill，因为有较好兼容性。

#### 发现一键安装工具  
- 了解到 [**小鱼的一键安装系列**](https://fishros.org.cn/forum/topic/20/%E5%B0%8F%E9%B1%BC%E7%9A%84%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E7%B3%BB%E5%88%97?lang=en-GB) 中的 ROS2 部分。  
 
- 该工具极大简化了 ROS2 安装流程，成功规避了繁琐的手动安装步骤，节省大量时间与精力，在此对其便捷性表示诚挚感谢。  

---

### 3 月 18 日  

#### 基础节点搭建  
- 创建名为 **C2_1** 的目录。  
- 在此目录中，完成 Python 节点和 C++ 节点的基础搭建工作。  
  - 学习节点相关知识：  
    - 节点基本概念、作用  
    - 在 ROS2 系统中的运行机制  
    - 节点运行所需的对应库  

#### 功能包创建学习  
- 创建目录 **C2_2**，开启对功能包创建的学习。  

##### Python 功能包创建  
使用以下指令创建 Python 功能包：  
```bash
ros2 pkg create --build-type ament_python <package_name> --dependencies <dependency1> <dependency2> ...
```
示例：  
```bash
ros2 pkg create --build-type ament_python my_python_pkg --dependencies rclpy std_msgs
```
- 成功创建名为 `my_python_pkg` 的 Python 功能包，依赖于 `rclpy` 和 `std_msgs` 库。  

##### C++ 功能包创建  
使用以下指令创建 C++ 功能包：  
```bash
ros2 pkg create --build-type ament_cmake <package_name> --dependencies <dependency1> <dependency2> ... --node-name <node_name>
```
示例：  
```bash
ros2 pkg create --build-type ament_cmake my_cpp_pkg --dependencies rclcpp std_msgs --node-name my_cpp_node
```
- 成功创建名为 `my_cpp_pkg` 的 C++ 功能包，并生成名为 `my_cpp_node` 的节点。  

##### 功能包构建  
使用以下指令对功能包进行构建：  
```bash
colcon build
```
- 将代码编译成可执行文件，使功能包能够在 ROS2 环境中正常运行。  
