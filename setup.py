from cx_Freeze import setup, Executable

setup(
    name="Schrödinger's Cat",
    version="1.0",
    description="Your description",
    executables=[Executable("game.py")],
    options={
        "build_exe": {
            "packages": ["numpy", "pygame", "qutip"],
            "include_files": ["image", "qbit.py"]
        }
    }
)
