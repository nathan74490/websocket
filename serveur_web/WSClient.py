import websocket
import threading
from Message import Message, MessageType
from Context import Context

class WSClient:
    def __init__(self, ctx, client_name):
        self.client_name = client_name
        self.ws = websocket.WebSocketApp(
            ctx.url(),
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )

    def on_message(self, ws, message):
        print(f"\n[server -> {self.client_name}] {message}\n> ", end="")

    def on_error(self, ws, error):
        print(f"[error] {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print(f"[close] code={close_status_code} msg={close_msg}")

    def on_open(self, ws):
        print(f"[open] connecté en tant que {self.client_name}")

       
        message = Message(MessageType.DECLARATION, emitter=self.client_name, content="", receiver="")
        ws.send(message.to_json())

        
        print("Tape: <dest> <message>  (ex: bob salut !) | 'exit' pour quitter")
        threading.Thread(target=self._input_loop, daemon=True).start()

    def _input_loop(self):
        
        while True:
            try:
                line = input("> ").strip()
                if not line:
                    continue
                if line.lower() in ("exit", "quit"):
                    self.close()
                    break

                parts = line.split(" ", 1)
                if len(parts) != 2:
                    print("Format invalide. Exemple: bob salut !")
                    continue

                dest, content = parts[0], parts[1]
                self.send(content, dest)

            except Exception as e:
                print(f"[input error] {e}")

    def close(self):
        self.ws.close()

    def connect(self):
        self.ws.run_forever()

    def send(self, content, dest):
        
        message = Message(MessageType.ENVOI, emitter=self.client_name, content=content, receiver=dest)
       
        try:
            self.ws.send(message.to_json())
        except Exception as e:
            print(f"[send error] {e}")

if __name__ == "__main__":
    import sys

    
    name = sys.argv[1] if len(sys.argv) > 1 else "nathan"

    client = WSClient(Context.dev(), name)
    client.connect()

