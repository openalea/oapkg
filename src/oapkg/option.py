from os.path import dirname

from pkglts.dependency import Dependency
from pkglts.option_object import Option


class OptionOapkg(Option):
    def root_dir(self):
        return dirname(__file__)

    def update_parameters(self, cfg):
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

    def require(self, purpose, cfg):
        del cfg

        if purpose == 'option':
            names = ['pysetup', 'sphinx', 'coverage', 'data', 'github', 'pypi', 'conda', 'travis', 'readthedocs']
            return [Dependency(name) for name in names]

        return []
