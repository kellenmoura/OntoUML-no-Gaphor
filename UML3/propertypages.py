import importlib.resources

from gi.repository import Gtk

from gaphor.core import transactional
from gaphor.diagram.propertypages import PropertyPageBase, PropertyPages
from gaphor.UML3 import uml3
from gaphor.UML.classes.classespropertypages import AttributesPage, OperationsPage
#from gaphor.UML3.classesonto.heritage import HeritageItem


def new_builder(*object_ids):
    builder = Gtk.Builder()
    builder.set_translation_domain("gaphor")
    with importlib.resources.path("gaphor.uml3", "propertypages.glade") as glade_file:
        builder.add_objects_from_file(str(glade_file), object_ids)
    return builder


@PropertyPages.register(uml3.Property)
class PropertyPropertyPage(PropertyPageBase):
    """An editor for Properties (a.k.a.

    attributes).
    """

    order = 30

    AGGREGATION = ("none", "shared", "composite")

    def __init__(self, subject: uml3.Property):
        super().__init__()
        self.subject = subject

    def construct(self):
        if not self.subject:
            return

        builder = new_builder("property-editor")

        aggregation = builder.get_object("aggregation")
        aggregation.set_active(self.AGGREGATION.index(self.subject.aggregation))

        builder.connect_signals({"aggregation-changed": (self._on_aggregation_change,)})
        return builder.get_object("property-editor")

    @transactional
    def _on_aggregation_change(self, combo):
        self.subject.aggregation = self.AGGREGATION[combo.get_active()]
