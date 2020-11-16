"""The UML3 Modeling Language module is the entrypoint for UML3 related
assets."""

import gaphor.UML3.propertypages  # noqa
from gaphor.abc import ModelingLanguage
from gaphor.core import gettext
from gaphor.diagram.diagramtoolbox import ToolboxDefinition
from gaphor.UML3 import diagramitems, uml3
from gaphor.UML3.toolbox import uml3_toolbox_actions


class UML3ModelingLanguage(ModelingLanguage):
    @property
    def name(self) -> str:
        return gettext("OntoUML")

    @property
    def toolbox_definition(self) -> ToolboxDefinition:
        return uml3_toolbox_actions

    def lookup_element(self, name):
        return getattr(uml3, name, None)

    def lookup_diagram_item(self, name):
        return getattr(diagramitems, name, None)
