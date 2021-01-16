from auto_struct import *
from dataclasses import dataclass

class UID(String(8)):
    @property
    def id(self) -> uint32_t:
        # TODO: I'm surprised python doesn't let me call int with a bytes convertible and a base
        # But then again everyone hates JS
        return uint32_t(int(bytes(self), 8))


class Permission(Char):
    def __init__(self, value):
        super().__init__(int(value))


class PermissionMask(BitFlag):
    __ELEMENT_TYPE__ = Permission
    X = 1
    W = 2
    R = 4


@dataclass
class Permissions(BasicStruct):
    padding: Array(uint8_t, 4)
    owner: PermissionMask
    group: PermissionMask
    other: PermissionMask
    padding2: Char

@dataclass
class TarHeader(BasicStruct):
    name: String(100)
    file_mode: Permissions
    uid: UID 
    gid: UID 
    size: String(12)
    mtime: String(12)
    checksum: String(8)
    link_indicator: uint8_t
    link_name: String(100)


with open('test.tar', 'rb') as f:
    print('Size', len(TarHeader))
    t = TarHeader.parse(f.read(len(TarHeader)))
    print(t)
    print(t.uid.id)
