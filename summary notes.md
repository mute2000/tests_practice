# 笔记
## 电脑基础知识
- 新建文件夹
  1. 命令行：win+R打开cmd，切到目标目录（如：cd desktop）,之后输出命令echo. > test.py(文件名)
  2. vscode：crtl+N 新建文件，ctrl+s保存后命名
- 命令行
  1. 安装：                   pip install pytest
  2. 查看版本：               pytest --version/pip show pytest
  3. cd
      - 到达指定路径             cd desktop
      - 返回上一层级             cd ..
  4. 查看目录                 dir
  5. 执行目录中文件            python test_add.py
  6. 执行指定路径的所有测试文件    pytest
  7. 运行参数
    - 无参数：读取所有符合规则的文件并全部执行
    - -v：    打印详细的运行日志信息，方便定位问题
    - -s:     带控制台输出结果，可以打印print输出的代码，用于调试
    - -k：    跳过运行某个或某些用例（模糊匹配）
        - pytest -k 类名（只运行名称包含该类名的测试用例，跳过其他测试用例）
        - pytest -k 方法名（只运行名称包含该方法名的测试用例，无论是否在同一个类中）
        - pytest -k "类名 and not 方法名" （运行类中除了指定方法名中的所有测试用例）
      - -x:    遇到失败用例立即停止运行
      - --maxfail num:   运行过程中有num条用例失败，终止运行
      - -m 参数：将运行有@pytest.mark.[标记名]这个标记的测试用例。自动化测试过程中分类后只运行某个功能的所有测试用例。例子（想要验证登录功能，在登录功能上添加@@pytest.mark.login，之后执行pytest -m login）
  8. 运行模式
      - 终端命令行
        - 运行某个文件： pytest 文件名.py 
        - 运行文件中的某个类： pytest 文件名.py::类名 
        - 运行类中的某个方法： pytest 文件名.py::类名::方法名  
      - vscode内部
        - 点击左侧测试图标，点击运行按钮   

## github基础知识
  1. vscode上传GitHub
    - github上创建仓库
    - git init
    - git add .
    - git commit -m"提交备注"
    - git remote add origin
    - git branch -M main
    - git push -u origin main
  2. 上传遇见的问题
      - warning: ----------------- SECURITY WARNING ----------------
        warning: | TLS certificate verification has been disabled! |
        warning: ---------------------------------------------------
        warning: HTTPS connections may not be secure. See https://aka.ms/gcm/tlsverify for more information.
        （TLS证书警告）
          - 解决方法git config --global http.sslverify true
      - fatal: unable to access 'https://github.com/mute2000/tests_practice.git/': Failed to connect to github.com port 443 after 21070 ms: Couldn't connect to server
      (连接问题)
        - 解决方法
          - 1. 生成密钥：ssh-keygen -t ed25519 -C"GitHub邮箱"
          - 2. 把生成的密钥添加到GitHub账户中
          - 3. 在执行git push

## vscode基础知识
- 预览markdown文档：ctrl+shift+v
- 查找.md文档的知识点：ctrl+shirt+f
- 中英文切换：ctrl+shift+p,之后输入“configue display language”
- 新建文件：crtl+N 新建文件，ctrl+s保存后命名
- 上传github要删除_pycache_文件（因为它属于本地环境的临时缓存，不具备代码共享价值，而且不符合代码仓库的管理规范）
  - 它是本地冗余文件，仅对你自己有用，无法公用
  - 其他人运行代码会生成自己的该文件
  - 保留不仅会增加空间体积而且有可能因为不同环境引发不必要的冲突
  - 添加.gitignore文件可以解决这个问题
  - 如果已经上传到GitHub
    - （# 直接删除Git追踪的所有__pycache__下的文件：git rm -r --cached $(git ls-files | grep __pycache__)）
    - 然后再次提交上传

## python基础知识
- 用例编写规范
  - 测试文件以test_开头或以_test结尾
  - 测试类以Test开头，并且不能带有init方法
  - 测试函数以test_开头
  - 断言使用基本的assert即可

- pytest测试框架
  - 简介：成熟的python测试工具，与python自带的unittest测试框架类似，比其更加简洁高效，可以兼容unittest框架，支持简单的单元测试和复杂的功能测试，可以结合requests实现接口测试，结合selenium和appium实现自动化功能测试，结合allure集成到Jenkins中可以实现持续集成。

- python语句
  - assert:断言语句，用来检查条件是否成立，用来调试/验证代码逻辑。
  - return
    - 定义：函数的返回值，作用是把函数的计算结果传递给调用这个函数的地方
    - 注意：return之后的代码不会执行

- 运算符
  - 成员运算符
    - in（可以用于字符串，列表，字典，集合等容器中）
      - 作用：用来判断某个元素是否在某个容器中

- python内置函数
  - hasattr
    - 作用：用来检查某个对象是否包含指定名称的属性和方法

- 类（装函数的容器）
  - 注意：类中的函数叫方法，类中的方法无法自动运行，需要创建实例化类后进行调用
  - self是方法中的固定参数，第一个参数必须是self

- 装饰符（给函数穿上件衣服，既保留了函数本身的功能，有添加了衣服的功能）
  - 本质：包装函数/类的函数
  - @pytest.mark.order(num)
    - 作用：pytest加载所有的测试用例是乱序，这个装饰符可以实现排序
    - 1.3.0版本
      - 不支持负数
      - 优先级：数字越小越先执行，最后是无标记
  - @pytest.fixture

- 写代码时的报错
  - AssertionError：断言错误，assert语句判断为false时出现
  - PytestUnknownMarkWarning：pytest未知标记警告（因为安装了新版本的插件而使用了老版本代码不匹配导致的问题）
      
## 游戏理解
  - 核心玩法
    - 核心流程：（登录，匹配，对局，结算），明确每一步的触发条件，规则逻辑，异常处理机制
    - 核心模式：区分不同模式，记录各模式的规则，胜利条件，参与门槛（等级，道具限制）
    - 核心规则：游戏底层判定标准（道具效果，特定物品触发条件）
  - 核心功能
    - 经济（货币类型，获取/消耗渠道）
    - 成长（等级/段位/成就/模拟经营）
    - 社交（好友/组队/工会（战队））
    - 作弊/防沉迷
  - 辅助功能
    - 新手引导
    - 游戏提示
    - 设置界面
    - 背包，仓库
  - 游戏体验方面
    - 美术风格
    - 游戏整体布局
    - 操作反馈
    - 不同机型适配性
  - 对游戏的建议
    - 平衡性
    - 规则漏洞
    - 性能问题
    - 兼容性

## 遇见的问题
  - order插件问题（耗时长）
    - 刚开始根据书上的内容来安装插件，因为插件过时了，安装失败
    - 安装新版本插件后，代码还是用的之前的，导致出了兼容性问题
    - 解决上述问题（将插件和代码换成新的）后运行，运行结果未报错，但是运行输出与结果还是不符
    - 查验过版本，尝试把所有有关的全部卸载在重新安装仍未解决
    - order1.x版本不支持负数，问题解决。


## 迷惑点
- 大致了解
  - 运行代码时使用pytest和使用python 文件名的区别
  - 全局环境作用于全部python项目，只适合通用工具，虚拟环境只作用于指定包，可以解决各个包用于不同版本，这样不会造成兼容性问题。


- 有点懵
  - 类中的self
  - @pytest.fixture()

- 待定
  - pytest运行参数中的-m 参数
  - 旧方案：pytest兼容unittest的前置后置函数（p5）

- 未掌握
  - pytest框架
- 未接触/实践
  - unittest测试框架
  - pytest的单元测试和功能测试
  - pytest结合requests实现接口测试
  - pytest结合selenium和appium实现自动化功能测试
  - pytest结合allure集成到Jenkins中可以实现持续集成