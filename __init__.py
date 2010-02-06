from os.path import join, dirname

TEMPLATE_FILES = join(dirname(__file__), 'templates')
SHARED_FILES = join(dirname(__file__), 'shared')

def setup(app, plugin):
	app.add_theme('kyleterry', TEMPLATE_FILES, plugin.metadata)
	app.add_shared_exports('kyleterry_theme', SHARED_FILES)
