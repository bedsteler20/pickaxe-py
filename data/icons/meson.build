application_id = 'com.bedsteler20.Pickaxe'

scalable_dir = join_paths('hicolor', 'scalable', 'apps')
symbolic_dir = join_paths('hicolor', 'symbolic', 'apps')

install_data(
  join_paths(scalable_dir, ('@0@.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', scalable_dir)
)

install_data(
  join_paths(symbolic_dir, ('@0@-symbolic.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', symbolic_dir)
)

install_data(
    join_paths(symbolic_dir, 'curseforge-symbolic.svg'),
    install_dir: join_paths(get_option('datadir'), 'icons', symbolic_dir)
)

install_data(
    join_paths(symbolic_dir, 'right-large-symbolic.svg'),
    install_dir: join_paths(get_option('datadir'), 'icons', symbolic_dir)
)
install_data(
    join_paths(scalable_dir, 'minecraft.svg'),
    install_dir: join_paths(get_option('datadir'), 'icons', scalable_dir)
)