import sublime, sublime_plugin
import fnmatch
import os

class ChefDkTestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print("--------------------------------------------------------------------------------------")
    for root, dirnames, filenames in os.walk(os.path.join(sublime.packages_path(), "SublimeChefDK/chef")):
      for filename in fnmatch.filter(filenames, '*.sublime-snippet'):
        xx = "Packages/Sublime" + os.path.join(root.lstrip(sublime.packages_path()), filename)
        print(xx)
        self.view.run_command('insert_snippet', {"name": xx})
        self.view.run_command('move_to', {"to": "eof"})
        self.view.run_command('insert', {"characters": "\n"})
