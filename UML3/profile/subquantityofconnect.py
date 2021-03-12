from gaphor import UML
from gaphor import UML3
from gaphor.diagram.connectors import Connector, RelationshipConnect
from gaphor.diagram.presentation import Classified
from gaphor.UML3.profile.subquantityof import SubquantityofItem

@Connector.register(Classified, SubquantityofItem)
class SubquantityofConnect(RelationshipConnect):

    line: SubquantityofItem

    def allow(self, handle, port):
        line = self.line
        subject = self.element.subject

        if handle is line.head:
            allow = isinstance(subject, UML3.StereotypeQuantity)

        elif handle is line.tail:
            allow = isinstance(subject, UML3.StereotypeQuantity)

        return allow and super().allow(handle, port)
        
    def connect_subject(self, handle):
        return True
'''@Connector.register(StereotypeRelator, SubquantityofItem)
class SubquantityofConnect(RelationshipConnect):

    line: SubquantityofItem

    def allow(line, handle, item, port=None) -> bool:
        if port is None and len(item.ports()) > 0:
            port = item.ports()[0]

        adapter = Connector(item, line)
        return adapter.allow(handle, port)


    def connect_subject(self, handle):
        element = self.element
        line = self.line

        c1 = self.get_connected(line.head)
        c2 = self.get_connected(line.tail)
        if c1 and c2:
            assert isinstance(c1.subject, UML3.StereotypeKind)
            assert isinstance(c2.subject, UML3.StereotypeRelator)

            head_type: UML3.StereotypeKind = c1.subject
            tail_type: UML3.StereotypeRelator = c2.subject

            if line.subject:
                end1 = line.subject.memberEnd[0]
                end2 = line.subject.memberEnd[1]
                if (end1.type is head_type and end2.type is tail_type) or (
                    end2.type is head_type and end1.type is tail_type
                ):
                    return

            # TODO: make element at head end update!
            c1.request_update()

            # Find all associations and determine if the properties on
            # the association ends have a type that points to the StereotypeKind.
            ext: UML3.Subquantityof
            for ext in line.model.select(UML3.Subquantityof):  # type: ignore[assignment]
                end1 = ext.memberEnd[0]
                end2 = ext.memberEnd[1]
                if (end1.type is head_type and end2.type is tail_type) or (
                    end2.type is head_type and end1.type is tail_type):
                    # check if this entry is not yet in the diagram
                    # Return if the association is not (yet) on the canvas
                    for item in ext.presentation:
                        if item.canvas is element.canvas:
                            break
                    else:
                        line.subject = ext
                        return
            else:
                # Create a new Subquantityof relationship
                relation = UML3.model.create_Subquantityof(head_type, tail_type)
                line.subject = relation


    def disconnect_subject(self, handle):
        """
        Disconnect model element.
        Disconnect property (memberEnd) too, in case of end of life for
        Subquantityof.
        """
        opposite = self.line.opposite(handle)
        hct = self.get_connected(handle)
        oct = self.get_connected(opposite)
        if hct and oct:
            old = self.line.subject
            del self.line.subject
            if old and len(old.presentation) == 0:
                for e in old.memberEnd:
                    e.unlink()
                old.unlink()'''

