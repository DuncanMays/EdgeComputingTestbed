from server import Server
import pickle

class App():

  def __init__(self):

    # this dict maps message types to the callback given to handle messages of that type
    self.callback_map = {}

    # this is the default callback, which simply returns the string 'msg success'
    # remember that server sends back whatever the callback returns, so the sender of the message will receive the strin 'msg success', confirming the message was recevied
    # this can be changed
    def default(msg):
      return 'msg success'

    self.default_callback = default

    # this function will be provided to the server as the response policy, meaning it will be called every time a message is receive
    # as such, it will map call the provided callback on the given message, by referenceing callback_map or using the defaule callback if no callback is specified for the specific message type
    def switch(msg):
      msg_dict = pickle.loads(msg)

      try:
        callback = self.callback_map[msg_dict["type"]]

      except:
        callback = self.default_callback

      return callback(msg_dict)

    self.server = Server(switch)

  # this function adds callbacks to the callback_map, and since switch is closed around the callback map, the server can reference these callbacks
  def add_callback(self, msg_type, callback_fn):
    self.callback_map[msg_type] = callback_fn

  # starts the server
  def start(self):
    self.server.start()