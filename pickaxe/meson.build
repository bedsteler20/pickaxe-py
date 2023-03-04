python = import('python')
fs = import('fs')

blueprint_files = files(
    'ui/add_instance.blp',
    'ui/instance_card.blp',
    'ui/preferences.blp',
    'ui/vanilla_instance_creator.blp',
    'ui/window.blp'
)

source_files = files(
    # pickaxe
    '__init__.py',
    'main.py',
    # view
    'view/window.py',
    'view/preferences_window.py',
    'view/about_dialog.py',
    'view/login_dialog.py',
    'view/add_instance_dialog.py',
    'view/vanilla_instance_creator.py',
    'view/download_tracker.py',
    # widgets
    'widgets/instance_card.py',
    # model
    'model/instance.py',
    'model/base.py',
    # managers
    'managers/account_manager.py',
    'managers/instance_manager.py',
    # helpers
    'helpers/promise.py',
    'helpers/change_notifier.py',
    'helpers/css.py',
    'helpers/misc.py',
    'helpers/async_utils.py',
)


configure_file(
    input: 'config.py',
    output: 'config.py',
    install_dir: moduledir,
    install: true,
    configuration: {
        'MS_CLIENT_ID': '3e64f2eb-2407-473d-9f15-7866700b96bb',
        'MS_CLIENT_SECRET': 'cWI8Q~Ou6izq431lgeu6cnkxNd.D_pmy2e0SAauL'
    },
)

install_data(
    source_files,
    install_dir: moduledir,
    preserve_path: true
)


configure_file(
  install_dir: get_option('bindir'),
  input: 'pickaxe.in.py',
  output: 'pickaxe',
  install: true,
  configuration: {
    'PYTHON': python.find_installation('python3').path(),
    'VERSION': meson.project_version(),
    'localedir': get_option('prefix') / get_option('localedir'),
    'pkgdatadir': pkgdatadir,
    'sourceroot': meson.source_root(),
  },
)

subdir('ui')