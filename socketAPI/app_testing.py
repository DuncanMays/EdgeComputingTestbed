from app import App


a = App()

def join_callback(msg):
  print('join')
  print(msg)

a.add_callback('join', join_callback)

def new_join_callback(msg):
  print('join2')
  print(msg)

a.add_callback('join', new_join_callback)

a.start()