from versions_manager import VersionManager
import pytest

def test_01():
    vm1 = VersionManager()
    assert vm1.release() == '0.0.1'

def test_02():
    vm2 = VersionManager('')
    assert vm2.release() == '0.0.1'

def test_03():
    vm3 = VersionManager('1.2.3.4')
    assert vm3.release() == '1.2.3'

def test_04():
    vm4 = VersionManager('1.2.3')
    assert vm4.release() == '1.2.3'

def test_05():
    vm5 = VersionManager('1.2.3.d')
    assert vm5.release() == '1.2.3'

def test_06():
    vm6 = VersionManager('1')
    assert vm6.release() == '1.0.0'

def test_07():
    vm7 = VersionManager('1.1')
    assert vm7.release() == '1.1.0'

def test_08():
    vm8 = VersionManager()
    assert vm8.major().release() == '1.0.0'

def test_09():
    vm9 = VersionManager('1.2.3')
    assert vm9.major().release() == '2.0.0'

def test_10():
    vm10 = VersionManager('1.2.3')
    assert vm10.major().major().release() == '3.0.0'

def test_11():
    vm11 = VersionManager()
    assert vm11.minor().release() == '0.1.0'

def test_12():
    vm12 = VersionManager('1.2.3')
    assert vm12.minor().release() == '1.3.0'

def test_13():
    vm13 = VersionManager('1')
    assert vm13.minor().release() == '1.1.0'

def test_14():
    vm14 = VersionManager('4')
    assert vm14.minor().minor().release() == '4.2.0'

def test_15():
    vm15 = VersionManager()
    assert vm15.patch().release() == '0.0.2'

def test_16():
    vm16 = VersionManager('1.2.3')
    assert vm16.patch().release() == '1.2.4'

def test_17():
    vm17 = VersionManager('4')
    assert vm17.patch().patch().release() == '4.0.2'

def test_18():
    vm18 = VersionManager()
    assert vm18.major().rollback().release() == '0.0.1'

def test_19():
    vm19 = VersionManager()
    assert vm19.minor().rollback().release() == '0.0.1'

def test_20():
    vm20 = VersionManager()
    assert vm20.patch().rollback().release() == '0.0.1'

def test_21():
    vm21 = VersionManager()
    assert vm21.major().patch().rollback().release() == '1.0.0'

def test_22():
    vm22 = VersionManager()
    assert vm22.major().patch().rollback().major().rollback().release() == '1.0.0'

def test_23():
    vm23 = VersionManager('1.2.3')
    vm23.major()
    vm23.minor()
    assert vm23.release() == '2.1.0'

