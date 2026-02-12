import sys
import os
import io
import re
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
from misc import printdbg


class SwampConfig():

    @classmethod
    def slurp_config_file(self, filename):
        # read swamp.conf config but skip commented lines
        f = io.open(filename)
        lines = []
        for line in f:
            if re.match('^\s*#', line):
                continue
            lines.append(line)
        f.close()

        # data is swamp.conf without commented lines
        data = ''.join(lines)

        return data

    @classmethod
    def get_rpc_creds(self, data, network='mainnet'):
        # get rpc info from swamp.conf
        match = re.findall(r'rpc(user|password|port)=(.*?)$', data, re.MULTILINE)

        # strip values to remove any trailing \r from Windows-style line endings
        creds = {key: value.strip() for (key, value) in match}

        # standard Swamp defaults...
        default_port = 26920 if (network == 'mainnet') else 16920

        # use default port for network if not specified in swamp.conf
        if 'port' not in creds:
            creds['port'] = default_port

        # convert to an int if taken from swamp.conf
        creds['port'] = int(creds['port'])

        # return a dictionary with RPC credential key, value pairs
        return creds

    @classmethod
    def tokenize(self, filename):
        tokens = {}
        try:
            data = self.slurp_config_file(filename)
            match = re.findall(r'(.*?)=(.*?)$', data, re.MULTILINE)
            # strip values to remove any trailing \r from Windows-style line endings
            tokens = {key.strip(): value.strip() for (key, value) in match}
        except IOError as e:
            printdbg("[warning] error reading config file: %s" % e)

        return tokens
