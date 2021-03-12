"""
Derivation --
"""


from gaphor import UML3
from gaphor import UML
from math import atan2, pi
from math import pi as M_PI
from gaphor.diagram.presentation import LinePresentation
from gaphor.diagram.shapes import Box, Text, EditableText
from gaphor.diagram.support import represents
from gaphor.UML.modelfactory import stereotypes_str

@represents(UML3.Derivation)
class DerivationItem(LinePresentation):
    def __init__(self, id=None, model=None):
        super().__init__(id, model)


        self.shape_middle = Text(
            text=lambda: stereotypes_str(self.subject, ("Derivation",)),
        )
        self.watch("subject[NamedElement].name")
        self.watch("subject.appliedStereotype.classifier.name")


    def draw_head(self, context):
        cr = context.cairo
        cr.move_to(1, 0)
        cr.set_source_rgb ( 0, -1, 0);
        cr.arc ( 0, 0, 0, 0, 2 * M_PI);
        cr.set_line_width (20)
        cr.close_path()
        cr.stroke()
        cr.move_to(10, 0)
