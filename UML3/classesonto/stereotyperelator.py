"""
Support code for dealing with stereotypes in diagrams.
"""

from gaphor import UML3
from gaphor.core.styling import TextAlign, VerticalAlign
from gaphor.diagram.shapes import Box, Text, draw_top_separator


def stereotyperelator_compartments(subject):
    return filter(
        None,
        (
            _create_stereotyperelator_compartment(appliedStereotypeRelator)
            for appliedStereotypeRelator in subject.appliedStereotypeRelator
        )
        if subject
        else [],
    )


def _create_stereotyperelator_compartment(appliedStereotypeRelator):
    def lazy_format(slot):
        return lambda: UML3.format(slot)

    slots = [slot for slot in appliedStereotypeRelator.slot if slot.value]

    if slots:
        return Box(
            Text(
                text=lazy_format(appliedStereotypeRelator.classifier[0]),
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
