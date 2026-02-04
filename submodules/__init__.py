"""
Submodules package for LKS project

This module provides access to ptexplorer functions without modifying the submodule itself.
"""

import sys
import os

# Add ptexplorer to path
_ptexplorer_path = os.path.join(os.path.dirname(__file__), 'ptexplorer')
if _ptexplorer_path not in sys.path:
    sys.path.insert(0, _ptexplorer_path)

# Import and expose ptexplorer functions
from ptexplorer import ptfile_decode, ptfile_encode

__all__ = ['ptfile_decode', 'ptfile_encode']

