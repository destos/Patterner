from pkg_resources import DistributionNotFound, get_distribution


try:
    __version__ = get_distribution('Patterner').version
except DistributionNotFound:
    __version__ = '(local)'

"""
Scenarios I would like to cover.

Import a pocket pattern that can be aligned with a part and then the sub-parts of that pattern are included.
Would be cool if it could work with edges.

Define reference paths that are rendered differently ( pocket ghost position )
"""
