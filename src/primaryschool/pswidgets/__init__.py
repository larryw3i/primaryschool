from primaryschool import *
from primaryschool.pswidgets.GameListWidget import *
from primaryschool.pswidgets.TopWidget import *
from primaryschool.pswidgets.WidgetABC import *


def show_widget(*args, **kwargs):
    verbose = kwargs.get("verbose", 0)
    os.environ[f"{app_name}_verbose"] = verbose
    # 0
    # PsGameListWidget(*args, **kwargs)
    # 1
    PsTopWidget(*args, **kwargs)
    # 2
    # 3
    pass


pass
