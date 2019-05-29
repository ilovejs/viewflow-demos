from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


# this is the menu item
class SalesConfig(ModuleMixin, AppConfig):
    # TODO: the name below is easy to be wrong
    name = "sales"
    icon = '<i class="material-icons">call_end</i>'
