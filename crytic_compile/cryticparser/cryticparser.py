from . import defaults_flag_in_config

def init(parser):
    init_solc(parser)
    init_truffle(parser)
    init_embark(parser)

def init_solc(parser):
    group_solc = parser.add_argument_group('Solc options')
    group_solc.add_argument('--solc',
                            help='solc path',
                            action='store',
                            default=defaults_flag_in_config['solc'])

    group_solc.add_argument('--solc-args',
                            help='Add custom solc arguments. Example: --solc-args "--allow-path /tmp --evm-version byzantium".',
                            action='store',
                            default=defaults_flag_in_config['solc_args'])

    group_solc.add_argument('--solc-disable-warnings',
                            help='Disable solc warnings',
                            action='store_true',
                            default=defaults_flag_in_config['disable_solc_warnings'])

    group_solc.add_argument('--solc-ast',
                            help='Provide the ast solc file',
                            action='store_true',
                            default=False)


def init_truffle(parser):
    group_truffle = parser.add_argument_group('Truffle options')
    group_truffle.add_argument('--truffle-ignore-compile',
                               help='Do not run truffle compile',
                               action='store_true',
                               dest='truffle_ignore_compile',
                               default=defaults_flag_in_config['truffle_ignore_compile'])

    group_truffle.add_argument('--truffle-build-directory',
                               help='Use an alternative truffle build directory',
                               action='store',
                               dest='truffle_build_directory',
                               default=defaults_flag_in_config['truffle_build_directory'])

    group_truffle.add_argument('--truffle-version',
                               help='Use a local Truffle version (with npx)',
                               action='store',
                               default=defaults_flag_in_config['truffle_version'])
    return group_truffle

def init_embark(parser):
    group_embark = parser.add_argument_group('Embark options')
    group_embark.add_argument('--embark-ignore-compile',
                              help='Do not run embark build',
                              action='store_true',
                              dest='embark_ignore_compile',
                              default=defaults_flag_in_config['embark_ignore_compile'])

    group_embark.add_argument('--embark-overwrite-config',
                              help='Install @trailofbits/embark-contract-export and add it to embark.json',
                              action='store_true',
                              default=defaults_flag_in_config['embark_overwrite_config'])

