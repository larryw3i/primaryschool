
import primaryschool
from primaryschool import *
from primaryschool.pswidgets import *
from primaryschool.psdep import *
from webbrowser

class AboutWidget(WidgetABC):
    def __init__(
            self,
            top_widget=None,
            app_name_fontsie=20,
            app_version_fontsize = 10
    ):
        super().__init__()
        self.top_widget = top_widget or TopWidget(mainloop=False)
        self.toplevel = tk.Toplevel(self.top_widget)
        
        self.app_name_fontsie = app_name_fontsie  
        self.app_version_fontsize = app_version_fontsize
        self.app_name_label = tk.Label(self.toplevel, text=app_name, 
            font=("",self.app_name_fontsize))
        self.app_version_label = tk.Label(
            self.toplevel,
            text = _("Version:")+ app_version,
            font = ("",self.app_version_fontsize)
        )
        self.app_deps = deps_full
        self.app_dep_labels = None

        pass

    def cmd_app_dep_label_b(self,dep_url=None):
        if not dep_url:
            return
        webbrowser.open(dep_url)
        pass

    def get_app_dep_labels(self):
        if not self.app_dep_labels:
            for name, version, home_url, licelse, license_url in app_deps:
                dep_label = tk.Label(
                    self.toplevel,
                    text = (name +" "+( version if version else "" ) + \
                    f" ({license})")
                )
                dep_label.bind(
                    '<Button>',
                    label hu = home_url:self.cmd_app_dep_label_b(dep_url = hu)
                )
                self.app_dep_labels.append(dep_label)
                pass
        return self.app_dep_labels
        pass


    pass
