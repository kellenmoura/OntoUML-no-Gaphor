import itertools
from typing import Iterable, Sequence

from gaphor.UML3.uml3 import (
    Heritage,
    Element,
)

from gaphor.UML.uml import (
    Stereotype,
)

def create_heritage(general, specific):
    assert (
        general.model is specific.model
    ), "General and Specific are from different models"
    model = general.model
    gen = model.create(Heritage)
    gen.general = general
    gen.specific = specific
    return gen


def stereotypes_str(element: Element, stereotypes: Sequence[str] = ()):
    """
    Identify stereotypes of an UML metamodel instance and return coma
    separated stereotypes as string.

    :Parameters:
     element
        Element having stereotypes, can be None.
     stereotypes
        List of additional stereotypes, can be empty.
    """
    # generate string with stereotype names separated by coma
    if element:
        applied: Iterable[str] = (
            stereotype_name(st) for st in get_applied_stereotypes(element)
        )
    else:
        applied = ()
    s = ", ".join(itertools.chain(stereotypes, applied))
    if s:
        return f"«{s}»"
    else:
        return ""


def stereotype_name(stereotype):
    """
    Return stereotype name suggested by UML specification. First will be
    character lowercase unless the second character is uppercase.

    :Parameters:
     stereotype
        Stereotype UML metamodel instance.
    """
    name = stereotype.name
    if not name:
        return ""
    elif len(name) > 1 and name[1].isupper():
        return name
    else:
        return name[0].lower() + name[1:]


def apply_stereotype(element, stereotype):
    """
    Apply a stereotype to an element.

    :Parameters:
     element
        UML metamodel class instance.
     stereotype
        UML metamodel stereotype instance.
    """
    assert (
        element.model is stereotype.model
    ), "Element and Stereotype are from different models"
    model = element.model
    obj = model.create(InstanceSpecification)
    obj.classifier = stereotype
    element.appliedStereotype = obj
    return obj