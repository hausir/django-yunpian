django-yunpian
==============

使用 `云片 <https://www.yunpian.com/>`_ API 发送短信的django扩展

使用
----

.. code-block::

    YUNPIAN = {
        'APIKEY': apikey,
        'DEFAULT_SIGN': default_sign,
    }

    from django_yunpin import YunPian

    yunpian = YunPian()


发送短信
--------

.. code::

    yunpian.send(phones, content, sign=None)

phones可以传单个手机号或者手机号列表，分别调用单条发送接口和批量发送接口


配置项
------

======================  ====================================
YUNPIAN.APIKEY          apikey
YUNPIAN.DEFAULT_SIGN    默认签名, 例如: 招商银行， 不包含【】
======================  ====================================
