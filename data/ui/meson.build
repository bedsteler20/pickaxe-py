blueprints = custom_target(
    'blueprints',
    input: files(
        'add_instance.blp',
        'instance_card.blp',
        'preferences.blp',
        'window.blp',
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
