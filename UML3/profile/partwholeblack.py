"""
Partwholeblack --
"""


from gaphor import UML3
from gaphor import UML
from gaphor.diagram.presentation import LinePresentation
from gaphor.diagram.shapes import Box, Text, EditableText
from gaphor.diagram.support import represents
from gaphor.UML.modelfactory import stereotypes_str
from gaphor.UML.classes.association import draw_tail_shared, draw_tail_composite

@represents(UML3.Partwholeblack)
class PartwholeblackItem(LinePresentation):
    def __init__(self, id=None, model=None):
        super().__init__(id, model)


        '''self.shape_middle = Box(
            Text(text=lambda: stereotypes_str(self.subject),),
            EditableText(text=lambda: self.subject.name or ""),
        )'''
        self.shape_middle = Text(
            text=lambda: stereotypes_str(self.subject, ("Partwholeblack",)),
        )
        #self.shape_middle = Box(Text(text=lambda: stereotypes_str(self.subject),))
        self.watch("subject[NamedElement].name")
        self.watch("subject.appliedStereotype.classifier.name")
        self.draw_tail = draw_tail_composite


    '''def draw_head(self, context):
        cr = context.cairo
        cr.move_to(0, 0)
        cr.line_to(15, -10)
        cr.line_to(15, 10)
        cr.close_path()
        cr.stroke()
        cr.move_to(15, 0)'''
