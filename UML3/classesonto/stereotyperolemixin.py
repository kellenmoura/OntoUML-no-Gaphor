"""
Support code for dealing with stereotypes in diagrams.
"""

from gaphor import UML
from gaphor import UML3
from gaphor.core.styling import TextAlign, VerticalAlign
from gaphor.diagram.shapes import Box, Text, draw_top_separator


def stereotyperolemixin_compartments(subject):
    return filter(
        None,
        (
            _create_stereotype_compartment(appliedStereotypeRolemixin)
            for appliedStereotypeRolemixin in subject.appliedStereotypeRolemixin
        )
        if subject
        else [],
    )


def _create_stereotyperolemixin_compartment(appliedStereotypeRolemixin):
    def lazy_format(slot):
        return lambda: UML3.format(slot)

    slots = [slot for slot in appliedStereotypeRolemixin.slot if slot.value]

    if slots:
        return Box(
            Text(
                text=lazy_format(appliedStereotypeRolemixin.classifier[0]),
                style={"padding": (0, 0, 4, 0)},
            ),
            *(
                Text(text=lazy_format(slot), style={"text-align": TextAlign.LEFT})
                for slot in slots
            ),
            style={"padding": (4, 4, 4, 4), "vertical-align": VerticalAlign.TOP},
            draw=draw_top_separator,
        )
    else:
        return None
