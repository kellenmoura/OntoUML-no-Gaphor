from gaphor import UML
from gaphor import UML3
from gaphor.diagram.connectors import Connector, RelationshipConnect
from gaphor.diagram.presentation import Classified
from gaphor.UML3.profile.characterization import CharacterizationItem

@Connector.register(Classified, CharacterizationItem)
class CharacterizationConnect(RelationshipConnect):

    line: CharacterizationItem

    def allow(self, handle, port):
        line = self.line
        subject = self.element.subject
        #print("#subject   ", subject)
        #subject2 = self.element.subject
        tipo = str(type(subject))
        #tipo2 = str(type(subject2))
        #tipo2 = print("tipo2", str(type(subject2)))
        result = False
        global head

        #condições para saber qual é o stereotype
        if tipo == "<class 'gaphor.UML3.uml3.StereotypeKind'>":
            #aux = "Kind"
            nome = (UML3.StereotypeKind)
            #tuplatail = (UML3.StereotypeRelator)
            '''print("tipo antes", tipo)
            tipo = ""
            print("tipo depois", tipo)
            tipo = str(type(subject))
            print("tipo depois de depois", tipo)'''
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeSubkind'>":
            #aux = "Subkind"
            nome = (UML3.StereotypeSubkind)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypePhase'>":
            #aux = "Phase"
            nome = (UML3.StereotypePhase)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeRole'>":
            #aux = "Role"
            nome = (UML3.StereotypeRole)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeCollective'>":
            #aux = "Collective"
            nome = (UML3.StereotypeCollective)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeQuantity'>":
            #aux = "Quantity"
            nome = (UML3.StereotypeQuantity)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeRelator'>":
            #aux = "Relator"
            nome = (UML3.StereotypeRelator)
            tuplahead = (UML3.StereotypeKind)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeCategory'>":
            #aux = "Category"
            nome = (UML3.StereotypeCategory)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypePhasemixin'>":
            #aux = "Phasemixin"
            nome = (UML3.StereotypePhasemixin)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeMixin'>":
            #aux = "Mixin"
            nome = (UML3.StereotypeMixin)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeRolemixin'>":
            #aux = "Rolemixin"
            nome = (UML3.StereotypeRolemixin)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeMode'>":
            #aux = "Mode"
            nome = (UML3.StereotypeMode)
        elif tipo == "<class 'gaphor.UML3.uml3.StereotypeQuality'>":
            #aux = "Quality"
            nome = (UML3.StereotypeQuality)


        if handle is line.head:
            result = isinstance(subject, nome)
            if nome == UML3.StereotypeKind:
                head = "Kind"
            elif nome == UML3.StereotypeSubkind:
                head = "Subkind"
            elif nome == UML3.StereotypePhase:
                head = "Phase"
            elif nome == UML3.StereotypeRole:
                head = "Role"
            elif nome == UML3.StereotypeCollective:
                head = "Collective"
            elif nome == UML3.StereotypeQuantity:
                head = "Quantity"
            elif nome == UML3.StereotypeRelator:
                head = "Relator"
            elif nome == UML3.StereotypeCategory:
                head = "Category"
            elif nome == UML3.StereotypePhasemixin:
                head = "Phasemixin"
            elif nome == UML3.StereotypeMixin:
                head = "Mixin"
            elif nome == UML3.StereotypeRolemixin:
                head = "Rolemixin"
            elif nome == UML3.StereotypeMode:
                head = "Mode"
            elif nome == UML3.StereotypeQuality:
                head = "Quality"
            #print("allow head", allow)
            #print("sub1", subject)
            #print("nome head", nome)
            #print("Head", head)
            #print("#line.head", line.head)

            #return allow and super().allow(handle, port)


        if handle is line.tail:
            if head == "Kind":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Subkind":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Phase":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Role":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Collective":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Quantity":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Relator":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Category":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Phasemixin":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Mixin":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Rolemixin":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Mode":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]
            elif head == "Quality":
                opc = [UML3.StereotypeQuality, UML3.StereotypeMode]

            if nome in opc:
                result = isinstance(subject, nome)
            #Descobrir como fazer para pegar objeto de alça cabeça (nome que ficou no line.head).
            '''if nome in tuplatail.line.head:
                allow = isinstance(subject, nome)
                print("OOOK")'''
            #if UML3.StereotypeRelator in tuplatail:
            #result = isinstance(subject, UML3.StereotypeRelator)
            #print("allow tail", allow)
            #print("sub2", subject)
            #print("nome tail", nome)
            #print("#line.tail", line.tail)
            #print("handle2", handle)
            #result = True
            #return allow and super().allow(handle, port)
            
        return result
        #return result and super().allow(handle, port)


        '''print("teste saida super", super())
        print("teste saida allow", super().allow(handle, port))
        return allow and super().allow(handle, port)'''
        
    def connect_subject(self, handle):
        return True
'''@Connector.register(StereotypeRelator, CharacterizationItem)
class CharacterizationConnect(RelationshipConnect):

    line: CharacterizationItem

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
            ext: UML3.Characterization
            for ext in line.model.select(UML3.Characterization):  # type: ignore[assignment]
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
                # Create a new Characterization relationship
                relation = UML3.model.create_Characterization(head_type, tail_type)
                line.subject = relation


    def disconnect_subject(self, handle):
        """
        Disconnect model element.
        Disconnect property (memberEnd) too, in case of end of life for
        Characterization.
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

