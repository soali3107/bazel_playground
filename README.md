# bazel_playground

Playing around with bzlmod and Bazel

## Setup
[Get Bazelisk](https://bazel.build/install/bazelisk) to setup bazel.
More bazelrc flags can be found here: https://bazel.build/reference/command-line-reference

## Python Setup
To check python version and run base python run `bazel run //toolchain/python:python_without_dependencies`

If you want to add dependencies, add your dependency to 'requirements.in'. 
Then, update 'requirements_lock.txt' by runing `bazel run //toolchain/python:requirements.update`.

You can now have python binary with some dependencies. Sample in `bazel run //toolchain/python:python_with_dependencies`.

## Java Setup
Java already comes with bazel. Java runtime is determined by a flag in .bazelrc

Can run `bazel build //toolchain/java:Hello` to confirm the Java runtime version is 19.0.2