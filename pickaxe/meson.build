python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)
conf.set('sourceroot', meson.source_root())

configure_file(
  input: 'pickaxe.in.py',
  output: 'pickaxe',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

install_data([
  '__init__.py',
], install_dir: moduledir)

subdir('frontend')
subdir('backend')