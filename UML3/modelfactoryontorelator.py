import itertools
from typing import Iterable, Sequence

from gaphor.UML3.uml3 import (
    Heritage,
    Element,
    Heritage,
    Formal,
    Material,
    Mediation,
    Characterization,
    Derivation,
    Structuration,
    Partwhole,
    Componentof,
    Containment,
    Memberof,
    Subcollectionof,
    Subquantityof,
    Dependencywhite,
    Dependencyblack,
)

from gaphor.UML.uml import (
    Stereotype,
    Class
)

from gaphor.UML3.uml3 import (
    StereotypeRelator,
)


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
            stereotyperelator_name(st) for st in get_applied_stereotypes(element)
        )
    else:
        applied = ()
    s = ", ".join(itertools.chain(stereotypes, applied))
    if s:
        return f"«{s}»"
    else:
        return ""


def stereotyperelator_name(stereotyperelator):
    """
    Return stereotype name suggested by UML specification. First will be
    character lowercase unless the second character is uppercase.

    :Parameters:
     stereotype
        Stereotype UML metamodel instance.
    """
    name = stereotyperelator.name
    if not name:
        return ""
    elif len(name) > 1 and name[1].isupper():
        return name
    else:
        return name[0].lower() + name[1:]


def apply_stereotyperelator(element, stereotyperelator):
    """
    Apply a stereotype to an element.

    :Parameters:
     element
        UML metamodel class instance.
     stereotype
        UML metamodel stereotype instance.
    """
    assert (
        element.model is stereotyperelator.model
    ), "Element and Stereotype are from different models"
    model = element.model
    obj = model.create(InstanceSpecification)
    obj.classifier = stereotyperelator
    element.appliedStereotypeRelator = obj
    return obj

def get_stereotypes(element):
    """
    Get sorted collection of possible stereotypes for specified element.
    """
    model = element.model
    # UML specs does not allow to extend stereotypes with stereotypes
    if isinstance(element, StereotypeRelator):
        return ()

    cls = type(element)

    # find out names of classes, which are superclasses of element class
    names = {c.__name__ for c in cls.__mro__ if issubclass(c, Element)}

    # find stereotypes that extend element class
    classes = model.select(lambda e: e.isKindOf(Class) and e.name in names)

    stereotypes = {ext.ownedEnd.type for cls in classes for ext in cls.extension}
    return sorted(stereotypes, key=lambda st: st.name)


def get_applied_stereotypes(element):
    """
    Get collection of applied stereotypes to an element.
    """
    return element.appliedStereotypeRelator[:].classifier
