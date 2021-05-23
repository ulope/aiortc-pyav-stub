import sys

from types import ModuleType

import pytest

import aiortc_pyav_stub


@pytest.fixture
def clean_av_module():
    yield
    sys.modules.pop('av')


def test_version():
    assert aiortc_pyav_stub.__version__ == '0.1.0'


def test_can_install_patch(clean_av_module):
    assert 'av' not in sys.modules

    aiortc_pyav_stub.install_as_av()

    assert 'av' in sys.modules
    assert sys.modules['av'] == aiortc_pyav_stub


def test_doesnt_overwrite_already_importet(clean_av_module):
    av_module = ModuleType('av')
    sys.modules['av'] = av_module

    with pytest.raises(RuntimeError):
        aiortc_pyav_stub.install_as_av()

    assert sys.modules['av'] == av_module
