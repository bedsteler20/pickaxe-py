python = import('python')
fs = import('fs')


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

install_data(
    # pickaxe
    '__init__.py',
    'main.py',
    # frountend    
    'frontend/window.py',
    'frontend/preferences_window.py',
    # dialogs
    'frontend/dialogs/about_dialog.py',
    'frontend/dialogs/login_dialog.py',
    'frontend/dialogs/add_instance_dialog.py',
    'frontend/dialogs/vanilla_instance_creator.py',
    'frontend/dialogs/download_tracker.py',
    # widgets
    'frontend/widgets/instance_card.py',
    # model
    'backend/model/instance.py',
    # managers
    'backend/managers/account_manager.py',
    'backend/managers/instance_manager.py',
    # helpers
    'backend/helpers/promise.py',
    'backend/helpers/change_notifier.py',
    'backend/helpers/css.py',
    'backend/helpers/misc.py',
    'backend/helpers/async_utils.py',
    install_dir: moduledir,
    preserve_path: true
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

subdir('frontend/ui')