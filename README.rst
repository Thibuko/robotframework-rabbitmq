RobotFramework RabbitMQ
=======================

Short Description
-----------------

Fork from `peterservice-rnd`_ to try to make this `Robot Framework`_ library usable to use RabbitMQ

Installation
------------

Install the library from github using pip:

::

    pip install git+https://github.com/Thibuko/robotframework-rabbitmq#egg=robotframework-rabbitmq

Documentation
-------------

See keyword documentation for RabbitMQ library on `GitHub`_.

Example
-------

.. code:: robotframework

    *** Settings ***
    Library    RabbitMq
    Library    Collections

    *** Test Cases ***
    Simple Test
        Create Rabbitmq Connection    my_host_name    15672    5672    guest    guest    alias=rmq
        ${overview}=    Overview
        Log Dictionary    ${overview}
        Close All Rabbitmq Connections

License
-------

Apache License 2.0

.. _Robot Framework: http://www.robotframework.org
.. _GitHub: https://rawgit.com/peterservice-rnd/robotframework-rabbitmq/master/docs/RabbitMq.html
.. _peterservice-rnd: https://github.com/peterservice-rnd/robotframework-rabbitmq
