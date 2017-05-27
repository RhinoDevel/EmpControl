
import logging

logging.basicConfig(level=logging.DEBUG)

# Console-based (non-production) UI:
#
import ec.ui.console
#
ec.ui.console.menu()

# Tk-based GUI:
#
# import ec.ui.tk
# #
# ec.ui.tk.menu()
