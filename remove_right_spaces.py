import sublime, sublime_plugin

class RemoveExtraRightSpacesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # I have no idea why the self.view is not returning the region correctly
        view = self.view.window().active_view()
        region = sublime.Region(0, min(view.size(), 2**14))
        content = view.substr(region)
        new_content = ''
        for line in content.split( '\n' ):
          new_content += line.rstrip() + '\n'
        view.replace(edit, region, new_content)

