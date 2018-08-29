# Gooey PyInstaller Demo

As seen at [DesertPy Show And Tell 2018-08-08][event].

[event]:https://www.meetup.com/Phoenix-Python-Meetup-Group/events/253529398/

## Tags

In order from minimum to more.

* `non-gui-non-portable` - Your plain old arg-parse usin' Python script. What most of you all start with.
* `lean-gui` - The bare minimum to get a GUI from [Gooey][gooey].
* `some-gui` - Using [Gooey][gooey]'s enhanced Argument Parser
* `meaty-gui` - Demo adding a progress bar with a regex and expression in
  [Gooey][gooey].
* `portable-app` - [PyInstaller][pyinstaller] definitions to make the GUI-ized portable
* `portable-app-win` - Fixes for Windows's buffered output with [Gooey][gooey]
* `ci-azure` - Build configuration for building redistributables on Azure Pipelines for Windows and macOS. 
    * [![Build Status](https://dev.azure.com/nelsonjchen/Gooey%20PyInstaller%20Demo/_apis/build/status/nelsonjchen.gooey-pyinstaller-demo?branchName=master)](https://dev.azure.com/nelsonjchen/Gooey%20PyInstaller%20Demo/_build/latest?definitionId=2?branchName=master)
    * Linux has troubles. Not sure how to fix yet.

To check out these different stages, just run `git checkout <tagname>`. Be aware this `README.md` is not on any of those tags.

## Check it Out! This is a only a very small subset and demo.

**[Gooey][gooey] can do a lot more, so go check out their repo!**

**Same goes for [Pyinstaller][pyinstaller]!**

[gooey]: https://github.com/chriskiehl/Gooey
[pyinstaller]: https://github.com/pyinstaller/pyinstaller

## License

It's so small, but consider this dual licensed under MIT / Apache 2.0. Have fun.
