# Remove Extra Right Spaces

This Sublime plugin removes extra right spaces from each line of your code.

I hope you you find this plugin helpful.

### Why?
Because these extra right spaces bother me! :angry: :stuck_out_tongue_winking_eye:
![remove_right_spaces_py__removeextraspaces](https://cloud.githubusercontent.com/assets/99601/3143481/7c11ffec-e9fc-11e3-8f5d-c48262f6f9cc.png)


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


