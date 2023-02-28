blueprints = custom_target(
    'blueprints',
    input: files(
        'add_instance.blp',
        'instance_card.blp',
        'preferences.blp',
        'window.blp',
        'vanilla_instance_creator.blp'
    ),
    output: '.',
    command: [
        find_program('blueprint-compiler'),
        'batch-compile',
        '@OUTPUT@',
        '@CURRENT_SOURCE_DIR@',
        '@INPUT@',
    ],
)

gnome.compile_resources('pickaxe',
  'gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
  dependencies: blueprints,
)