blueprints = custom_target(
    'blueprints',
    input: blueprint_files,
    output: '.',
    command: [
        find_program('blueprint-compiler'),
        'batch-compile',
        '@OUTPUT@',
        '@CURRENT_SOURCE_DIR@',
        '@INPUT@',
    ],
)

gnome.compile_resources(
    'pickaxe',
    'pickaxe.gresource.xml',
    gresource_bundle: true,
    install: true,
    install_dir: pkgdatadir,
    dependencies: blueprints,
)
