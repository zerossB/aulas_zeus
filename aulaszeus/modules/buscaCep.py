import re
import urllib

def get_cep(cep):
    """."""
    url = ""
    cepCorrigido = re.sub('[^\d]', '', cep)

    if len(cepCorrigido) != 8:
        return False;



    payload = {'relaxation'}
