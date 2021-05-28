import cx_Freeze

executables = [cx_Freeze.Executable("frogger.py")]

cx_Freeze.setup(
    name="Jumpy Frog",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["frogger1.gif", "car_left.gif", "car_right.gif", "log_full.gif", "turtle_left.gif", "turtle_right.gif", "turtle_left_half.gif", "turtle_right_half.gif", "turtle_submerged.gif", "home.gif", "frog_home.gif","frogger1small.gif"]}},
    executables = executables

    )
    