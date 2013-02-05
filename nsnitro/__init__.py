from nsnitro import NSNitro
from nsutil import NSNitroError, NSNitroResponse
from nsresources import *
import nsresources
__all__ = ['NSNitro', 'NSNitroError', 'NSNitroResponse' ] + nsresources.__all__
__import__("pkg_resources").declare_namespace(__name__)
