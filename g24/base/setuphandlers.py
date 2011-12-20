# -*- coding: utf-8 -*-
import collective.setuphandlertools as sht
import logging
logger = logging.getLogger("g24.base")

def setup_content(context):
    if sht.isNotThisProfile(context, 'thet.netpol.base-setup_content.txt'):
        return


