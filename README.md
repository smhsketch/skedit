![skedit logo](https://i.imgur.com/NlYbBSJ.png)


# skedit
A WIP, cross-platform, lightweight text editor built in Tk

# dependencies

if you want to run a raw, uncompiled instance of skedit, it depends on

* `python3`
* `tcl`
* `tk`
* `python-tk`

however, there are no dependencies to run a `.exe` of skedit or a compiled *nix script.
if you move the executable out of the build folder it comes in, it will not work.

# installation

download `skedit-nix` (on *nix) or `skedit-windows` (on Windows) from the [releases](https://github.com/smhsketch/skedit/releases) tab.

extract the .zip to wherever you want. make sure to keep the executable in the original folder it was in.

move the `skeditFiles` folder to `C:\Program Files\skedit` (Windows) or `/usr/share` (*nix).

execute the executable.

# bindings

`<control-n>` new buffer

`<control-s>` save

`<control-d>` save as

`<control-o>` open file

`<control-t>` go to top of buffer

`<control-x>` remove current line