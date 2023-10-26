load("@rules_python//python:pip.bzl", "compile_pip_requirements")

# Python without any dependencies
py_binary(
    name = "python_without_dependencies",
    main = "python.py",
    srcs = ["python.py"],
)

# Python with dependencies in requirements_in
py_binary(
    name = "python_with_dependencies",
    deps = ["@my_deps//flask",
    "@my_deps//blinker"],
    srcs = ["python.py"],
    main = "python.py"
)

compile_pip_requirements(
    name = "requirements",
    # extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)
