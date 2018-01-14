from pkglts.dependency import Dependency


def update_parameters(cfg):
    """Update config with parameters necessary for this option.

    Notes: create a section with option name to store params.

    Args:
        cfg (dict): dict of option parameters as seen in pkg_cfg.json

    Returns:
        None: update in place
    """
    cfg['base']['authors'] = [('openalea', 'openalea@openalea.fr')]

    for ext in [".csv", ".ini", ".json"]:
        if ext not in cfg['data']['filetype']:
            cfg['data']['filetype'].append(ext)
    cfg['data']['use_ext_dir'] = False

    cfg['doc']['fmt'] = "rst"
    cfg['doc']['keywords'].append('openalea')
    
    cfg['license']['name'] = 'CeCILL-C'
    cfg['license']['organization'] = 'openalea'
    
    if "36" not in cfg['pysetup']['intended_versions']:
        cfg['pysetup']['intended_versions'].append("36")

    cfg['sphinx']['theme'] = "sphinx_rtd_theme"
    
    cfg['test']['suite_name'] = "pytest"
    
    # add a parameter to the option
    cfg['oapkg'] = dict(simulator=False)


def check(cfg):
    """Check the validity of parameters in working environment.

    Args:
        cfg (Config):  current package configuration

    Returns:
        (list of str): list of faulty parameters
    """
    del cfg
    invalids = []

    return invalids


def require(purpose, cfg):
    """List of requirements for this option for a given purpose.

    Args:
        purpose (str): either 'option', 'setup', 'install' or 'dvlpt'
        cfg (Config):  current package configuration

    Returns:
        (list of Dependency)
    """
    del cfg

    if purpose == 'option':
        names = ['pysetup', 'sphinx', 'coverage', 'data', 'github', 'pypi', 'conda']
        return [Dependency(name) for name in names]

    if purpose == 'install':
        return []

    return []
