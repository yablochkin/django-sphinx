from django.conf import settings

__all__ = ('SPHINX_API_VERSION',)

# Sphinx 0.9.9
# SPHINX_API_VERSION = 0x116

# Sphinx 0.9.8
# SPHINX_API_VERSION = 0x113

# Sphinx 0.9.7
# SPHINX_API_VERSION = 0x107

SPHINX_API_VERSION = getattr(settings, 'SPHINX_API_VERSION', 0x116)
