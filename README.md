# Remove Extra Right Spaces

This Sublime plugin removes extra right spaces from each line of your code.

I hope you you find this plugin helpful.

### Why?



### Installation

For manual installation, run the following script in the Sublime Text terminal ```(ctrl+`)``` which utilizes ```git clone```.

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/pererinha/RemoveExtraRightSpaces', 'RemoveExtraRightSpaces'], 'working_dir': path})
```

**It is currently working just for Sublime 3**

### Usage
* On Mac **Command + Shift + C** 
* On Windows or Linux **Ctrl + Shift + C**

Or 

**Ctrl + Shift + P** and search for *“Remove extra right spaces”*


