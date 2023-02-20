conf = configuration_data()
conf.set('MS_CLIENT_ID', '3e64f2eb-2407-473d-9f15-7866700b96bb')
conf.set('MS_CLIENT_SECRET', 'cWI8Q~Ou6izq431lgeu6cnkxNd.D_pmy2e0SAauL')
configure_file(
    input: 'config.py',
    output: 'config.py',
    configuration: conf,
    install: true,
    install_dir: moduledir / 'backend',
)

install_data(
    [
        'main.py',
    ],
    install_dir: moduledir / 'backend',
)

subdir('managers')
subdir('helpers')
subdir('model')