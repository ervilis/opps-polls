#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pkg_resources

pkg_resources.declare_namespace(__name__)

VERSION = (0, 1, 5)

__version__ = ".".join(map(str, VERSION))
__status__ = "Development"
__description__ = u"Poll App for Opps CMS"

__author__ = u"Bruno Cezar Rocha"
__credits__ = []
__email__ = u"rochacbruno@gmail.com"
__license__ = u"MIT License"
__copyright__ = u"Copyright 2013, Opps Projects"
