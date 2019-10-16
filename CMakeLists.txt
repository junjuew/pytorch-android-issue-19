cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(custom_ops)

find_package(Torch REQUIRED)

add_executable(load load.cc)
target_link_libraries(load "${TORCH_LIBRARIES}")
set_property(TARGET load PROPERTY CXX_STANDARD 11)