"""This module holds the configuration generators for routing daemons
that can be used in a router."""
from .base import BasicRouterConfig, RouterConfig
from .zebra import Zebra
from .ospf import OSPF, OSPFArea
from .ospf6 import OSPF6
from .bgp import BGP, AS, iBGPFullMesh, bgp_peering, bgp_fullmesh, ebgp_session
from .radvd import RADVD
from .iptables import IPTables, IP6Tables
from .sshd import SSHd

__all__ = ['BasicRouterConfig', 'Zebra', 'OSPF', 'OSPF6', 'OSPFArea', 'BGP', 'AS',
           'iBGPFullMesh', 'bgp_peering', 'RouterConfig', 'bgp_fullmesh',
           'ebgp_session', 'IPTables', 'IP6Tables', 'SSHd', 'RADVD']
