# 每日总结
- __init__.py文件的作用
- fixture中参数scope的用法
- fixture中参数autouse的用法
- fixture中参数params的用法
- pytest中内置函数request的作用和核心用法,request.param
- 夹具函数的定义和特点
- pytest框架的依赖注入特性
- f-string语法
- 代码运行报错
    - NameErro：主动抛出的异常，用来模拟测试用例失败场景
    - AttributeError：属性使用错误(request.params)
- 上传代码时报错，网络连接错误（连接不上GitHub账户）
    - airtcp意外关闭，导致的问题，重连之后，关闭终端重新打开后上传成功

- 没弄懂
if __name__ == '_main_':
    pytest.main()