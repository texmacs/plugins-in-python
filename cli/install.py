import os
import shutil
import subprocess
import sys
from pathlib import Path
import subprocess


def get_plugins_path():
    if "TEXMACS_HOME_PATH" in os.environ.keys():
        texmacs_home_path = Path(os.environ.get("TEXMACS_HOME_PATH"))
        plugins = texmacs_home_path.joinpath("plugins")
    else:
        plugins = Path.home().joinpath(".TeXmacs", "plugins")
    return plugins


def install_win(name):
    plugins = get_plugins_path()
    plugin = plugins.joinpath(name)
    binary = plugin.joinpath("bin")
    pex = binary.joinpath(name + ".pex")
    entry = binary.joinpath("plugins").joinpath(name + ".py")
    os.chdir(binary)
    subprocess.call(["tar", "xzvf", pex])
    os.remove(binary.joinpath("PEX-INFO"))
    os.remove(binary.joinpath("__main__.py"))
    os.remove(pex)
    shutil.rmtree(binary.joinpath("__pex__"))
    shutil.rmtree(binary.joinpath(".bootstrap"))
    shutil.move(entry, pex)


def install(name):
    if not Path(f"plugins/{name}").exists():
        print(f"No such plugin: {name}")
        exit(-1)

    plugins = get_plugins_path()
    plugin = plugins.joinpath(name)
    binary = plugin.joinpath("bin")
    if plugin.exists():
        print(f"Removing existing {str(plugin)}")
        shutil.rmtree(str(plugin))

    print(f"Packaging: pants package //:{name}")
    subprocess.run(["pants", "package", f"//:{name}"])

    print(f"Installing: {str(plugin)}")
    shutil.copytree(f"plugins/{name}", str(plugin))

    print(f"Installing: {str(binary)}/{name}.pex")
    os.mkdir(str(binary))
    shutil.copy(f"dist/{name}.pex", str(binary))


if __name__ == "__main__":
    install(sys.argv[1])
    if len(sys.argv) == 3 and sys.argv[2] == "win":
        install_win(sys.argv[1])
