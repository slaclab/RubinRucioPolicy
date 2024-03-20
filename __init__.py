SUPPORTED_VERSION = ["1.29", "1.30", "1.31", "32", "33", "34"]

#def get_algorithms():
#    return { 'lfn2pfn': { 'RUBIN': lfn2pfn_RUBIN }, 'surl': { 'rubin': construct_surl_rubin } }

def get_algorithms():
    return { 'lfn2pfn': { 'lsst_butler': lfn2pfn_lsst_butler }, 
             'surl': { 'lsst_usdftape': construct_surl_lsst_usdftape } }

def lfn2pfn_lsst_butler(scope, name, rse, rse_attrs, protocol_attrs):
    """
    Given a LFN, convert it directly to a path using the mapping:
    note: scopes do not appear in pfn in Rubin/LSST Butler

        scope:name -> name

    :param scope: Scope of the LFN. 
    :param name: File name of the LFN.
    :param rse: RSE for PFN (ignored)
    :param rse_attrs: RSE attributes for PFN (ignored)
    :param protocol_attrs: RSE protocol attributes for PFN (ignored)
    :returns: Path for use in the PFN generation.
    """

    del rse
    del rse_attrs
    del protocol_attrs
    return '%s' % name

def construct_surl_lsst_usdftape(dsn: str, scope: str, filename: str) -> str:
    """
    Defines relative SURL for new replicas. This method
    contains Rubin USDF Tape RSE convention. To be used for non-deterministic sites.

    @return: relative SURL for new replica.
    @rtype: str
    """
    # Preliminary, we are still testing the surl() function. 
    return '/archive/%s#%s:%s' % (dsn, scope, filename)
