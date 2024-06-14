import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib, Gio


APPID = 'com.github.taniyoshima.pyt_gtk4_filedialog2'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"
    filedialog = Gtk.Template.Child()

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

        dir_name = Gio.File.new_for_path(os.path.dirname(__file__))
        self.filedialog.set_initial_folder(dir_name)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):

        self.filedialog.save(
            parent=self, cancellable=None,
            callback=self.on_filedialog_save)

    def on_filedialog_save(self, filedialog, task):
        try:
            file = filedialog.save_finish(task)
        except GLib.GError:
            return

        if file is not None:
            # ファイルの保存作業を記入
            print(file.get_path())
            print(file.get_parent().get_path())
            print(file.get_basename())


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
