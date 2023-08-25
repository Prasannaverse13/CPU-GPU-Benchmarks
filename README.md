Graph Analysis Frameworks Performance Benchmark Suite

Welcome to the Graph Analysis Frameworks Performance Benchmark Suite! This suite is designed to help you evaluate and compare the performance of various graph analysis frameworks for both CPU and GPU computations. By utilizing this suite, you can make informed decisions about which framework best suits your specific graph analysis needs.

Table of Contents
Introduction
Features
Getting Started
Prerequisites
Installation
Running Benchmarks
Adding New Benchmarks
Contributing
License
Introduction
Graph analysis is a crucial component in various domains, such as social networks, recommendation systems, and scientific simulations. With the increasing availability of GPU hardware, there's a need to assess the performance of graph analysis frameworks on both traditional CPUs and GPUs. This benchmark suite aims to facilitate this assessment by providing a standardized set of benchmarks and tools.

Features
Standardized benchmark suite for graph analysis frameworks.
Support for CPU and GPU benchmarks.
Easily extensible architecture to add new benchmarks and frameworks.
Detailed performance metrics and reporting.
Getting Started
Prerequisites
C++ compiler with C++11 support
CUDA Toolkit (for GPU benchmarks)
Graph analysis frameworks you wish to benchmark (already installed)
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/graph-analysis-benchmarks.git
cd graph-analysis-benchmarks
Compile the benchmark suite:

bash
Copy code
mkdir build
cd build
cmake ..
make
Running Benchmarks
Navigate to the build directory.

Run the benchmark suite:

bash
Copy code
./graph_benchmarks
Select the benchmarks you want to run and follow the on-screen instructions.

Adding New Benchmarks
To add new benchmarks for specific graph analysis frameworks:

Create a new benchmark directory under benchmarks/.

Implement the benchmark using the chosen graph analysis framework's API.

Update the main benchmark list in src/main.cpp.

Recompile the benchmark suite.
