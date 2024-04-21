#!/usr/bin/env python3
"""
Authorization module
"""

from flask import request
from typing import List, TypeVar
from auth import Auth


class BasicAuth(Auth):
    """Class that uses basic auth for authentication"""
