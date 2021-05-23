AIORTC PyAV Stub
================

This is a module that provides the minimum necessary signature to make 
``aiortc`` importable without having ``av`` installed.

Please note this module does not provide any functionality.

It's purpose is to make it possible to use the data only features of ``aiortc`` 
without needing ``av`` installed.

Usage
-----

Before importing ``aiortc`` you need to install the stub module under the ``av``
name::

    import aiortc_pyav_stub
    
    aiortc_pyav_stub.install_as_av()

    # now it's possible to import aiortc
    import aiortc
