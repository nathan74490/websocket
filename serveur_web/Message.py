#enumeration des message_type possibles(declaration, envoi, rception)
class MessageType:
    DECLARATION = "declaration"
    ENVOI = "envoi"
    RECEPTION = "reception"
    

class Message:
    def __init__(self, type:MessageType, emitter, content, receiver=None):
        self.type = type
        self.emitter = emitter
        self.content = content
        self.receiver = receiver

    @staticmethod
    def default_message():
        return Message("TOTO","system", "This is a default message.","all")
    @staticmethod
    def from_json(json_data):
        import json
        data = json.loads(json_data)
        type = data["messsage_type"]
        emitter = data["data"]["emitter"]
        content = data["data"]["value"]
        receiver = data["data"].get("recept", None)
        return Message(type, emitter, content, receiver)
   
    def to_json(self):
        import json
        data = {
            "messsage_type": self.type,
            "data": {
                "emitter": self.emitter,
                "value": self.content,
                "recept": self.receiver
            }
        }
        return json.dumps(data)



messages = Message(MessageType.DECLARATION, 
                   emitter="Alice", 
                   content="bonjour Bob!", 
                   receiver="Bob")

messageRbuild= Message.from_json(messages.to_json())
assert messages.to_json() == messageRbuild.to_json()

