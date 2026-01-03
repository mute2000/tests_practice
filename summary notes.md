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

- allure
  - 定义：一种灵活的，轻量级，支持多语言的测试报告，不仅能够以简洁的web报告形式显示已测试的内容，而且允许参与开发过程的每个人从测试的日常执行中提取最大限度的有用信息。
  - 用法
    - 保存测试结果数据：pytest --alluredir=tmp/my_allure_results
    - 打开报告，启动allure服务
      - 方法一（临时目录，需要快速查看，频繁更新测试数据使用）：allure serve path/to/allure_results
      - 方法二(可保存为文件，适合需要长期保存的测试报告)
        - allure generate ./tmp/my_allure_results/ -o ./report/ --clean
        - allure open -h 127.0.0.1 -p 8883 ./report/

- selenium
    - 定义
        - selenium帮我们自动化验收测试，支持web浏览器自动化，能够完成界面元素定位，窗口跳转，结果比较，支持多种浏览器，编程语言，操作系统。
    - 架构
        - 在客户端完成selenium脚本编写，然后传送给selenium服务器，之后使用浏览器驱动(driver)与浏览器进行交互(browser)。
    - 核心组件
        - webdriver：使用浏览器提供的api来控制浏览器
        - IDE：扩展插件，可以录制用户在浏览器的操作
            - IDE的第一次使用
                - 录制第一个测试用例（创建用例和录制方法，suite的界面管理）
        - Grid：用于selenium分布式，可以在多个浏览器和操作系统运行中测试用例

  - selenium测试用例编写
      - 定义：为了实施测试而向被测试的系统提供的一组集合（测试环境，操作步骤，测试数据，预期结果等）
      - 优势
          - 可以应对更加复杂的场景以及更加符合PageObject设计模式
          - 更易于阅读，更便于维护代码
      - 三大要素
          - 标题：是对测试用例的描述，标题应该清楚的表达测试用例的用意
          - 步骤：对测试执行过程进行描述
          - 预期结果：提供测试执行的预期结果
      - PageObject设计模式
          - 软件测试(UI自动化测试)中常用的一种设计模式，核心是将网页的元素定位，操作逻辑与测试用例分离，把每一个页面封装成一个独立的Python类（或其他语言的类），测试用例只需要调用类中的方法，无需关注页面的内部元素细节。
          - 特点
              - 封装性
                  - 把页面的元素和操作封装在页面对象类中，测试用例不用直接操作元素，只调用封装好的方法
              - 复用性
                  - 多个测试用例涉及同一页面的操作，可直接复用页面对象的方法，无需重复编写元素定位和操作代码。
              - 易维护性
                  - 当页面元素（如 id、xpath）或操作逻辑变更时，只需修改页面对象类中的对应代码，所有调用该方法的测试用例无需改动。
              - 可读性
                  - 测试用例中调用的是语义化的方法（如search_baidu("关键词")），而非繁琐的元素定位代码，用例逻辑更清晰。

  - web控件定位与常见操作
    - 控件定位元素
      - id
        - selenium自带ID定位，可以通过元素ID属性进行定位
        - driver.find_element(By.ID, "app")
      - name
      - xpath
      - css_selector
      - link
      - class_name
      - tag_name
    - 控件定位注意事项
      - id/name是最安全的定位选项，具有唯一性
      - css_selector语法简洁，搜索速度快与xpath
      - xpath定位功能强大，采用遍历搜索，速度略慢
      - 其他不推荐使用，无法精准定位
  - 常见操作
    - 


  - 等待
      - 简介
          - 在实际工作中等待机制可以保证代码的稳定性，从而使代码不会因为网速，电脑性能等条件的约束而影响运行结果
          - 等待：运行代码时，页面的渲染速度跟不上代码运行速度时，需要人为限制代码执行速度
          - 在web自动化时，一般要等待页面元素加载完成后，才能执行操作，否则会找不到元素等各种错误。 
      - 隐式等待（最常用）
          - 设置一个等待时间，轮询查找（默认0.5s）元素是否出现，如果没有就抛出异常
          - 隐式等待作用时全局的
          - driver.implicitly_wait()
      - 显式等待
          - 代码定义等待一定条件后进一步执行代码，程序每隔一段时间进行条件（默认0.5s）判断，如果条件成立，执行下一步；否则继续等待，直到超过设置的最长时间
          - 隐式等待不起作用时，会用显式等待
      - 强制等待
          - 强制线程一定时间
          - 在隐式等待和显式等待不起作用时使用
          - time.sleep(10)

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
  - request(pytest内置函数)
    - 作用：专门用来获取夹具的上下文信息
    - 函数下的方法
      - request.param
        - 获取当前fixture的params参数中的当前迭代值
  - open
    - 作用：用来打开文件
  - eval
    - 作用：用来执行一个字符串表达式，并返回表达式的值
- 夹具函数
  - 定义：可复用的函数，它可以帮你提前准备测试需要的环境，数据，对象，或者在测试结束后做清理工作
  - 特点
    - 用@pytest.fixture装饰（有这个pytest才会识别它是夹具）
    - 可被测试函数'依赖注入'
    - 可复用：可以有效避免重复代码
    - 支持前后置操作
- 类（装函数的容器）
  - 注意：类中的函数叫方法，类中的方法无法自动运行，需要创建实例化类后进行调用
  - self是方法中的固定参数，第一个参数必须是self

- 数据格式
  - YAML
    - 注意
      - 缩进要用空格（不能用tap）
      - 冒号后要加空格
      - 字符串可以不加引号（有特殊符合需要加引号）
    - yaml方法
      - yaml.safe_load()
        - 作用：把yaml格式的文件转换成Python能直接用的类型数据
        - safe:表示安全模式(只解析yaml的基础数据类型，避免恶意代码)
- 关键字
  - yield
  - pass（占位符）
    - 作用：在语法上需要语句但暂时不需要执行任何逻辑时使用

- 装饰符（给函数穿上件衣服，既保留了函数本身的功能，有添加了衣服的功能）
  - 本质：包装函数/类的函数
  - @pytest.mark.order(num)
    - 作用：pytest加载所有的测试用例是乱序，这个装饰符可以实现排序
    - 1.3.0版本
      - 不支持负数
      - 优先级：数字越小越先执行，最后是无标记
  - @pytest.fixture()
    - 作用：将这个用例方法名以参数的形式传到方法里
    - 参数scope(@pytest.fixture(scope="session"))
      - 作用：可以控制fixture的作用范围（优先级session > module > class > function）
    - 参数autouse(@pytest.fixture(autouse=True))
      - 作用：自动应用到所有测试方法中
      - 注意：这个参数下没有办法返回值给测试用例
    - 参数params(@pytest.fixture(params=[1,2,3]))
      - 定义：pytest实现'参数化测试'的核心功能之一,用来给夹具传递多组测试数据，让依赖该夹具的测试函数自动执行多次
      - 作用：可以接受一个可迭代的对象，pytest会自动遍历这个对象的每个元素，把元素按参数传递给夹具函数，最终按组执行
    - 参数parameterize
      - 作用：把多组测试数据给同一个测试函数，让函数自动循环多次，每次用一组数据
      - 可以使用多次装饰器来生成大量测试用例（离得近的先遍历）
      - 语法：@pytest.mark.parametrize(self,参数名,参数值，indirect=False, ids=None, \, scope=None)
        - self:这个是pytest内部某个类的方法，用的时候可以省略，作为装饰器使用，pytest会自动处理
        - 参数名：必须是字符串
        - 参数值：必须是可迭代对象
        - indirect（默认False）：数据直接传给测试函数
          - indirext=True:所有参数传给同名的fixture
        - ids(默认None)：给每组测试数据起个名字，方便在测试结果中区分不同用例。ids的格式要用列表/元组，注意要与参数值一致
        - \(位置参数分隔符):限制传参方法，\前面只能用位置传参，这是代码规则，写代码本来也是用的位置传参

- 写代码时的报错
  - AssertionError：断言错误，assert语句判断为false时出现
  - PytestUnknownMarkWarning：pytest未知标记警告（因为安装了新版本的插件而使用了老版本代码不匹配导致的问题）
  - NameErro：主动抛出的异常，用来模拟测试用例失败场景
  - AttributeError：属性使用错误
      
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
  - 运行代码时使用pytest和使用python 文件名的区别   √
  - 全局环境作用于全部python项目，只适合通用工具，虚拟环境只作用于指定包，可以解决各个包用于不同版本，这样不会造成兼容性问题。

- 不理解
  - if __name__ == '_main_':    
     pytest.main()    √

- 有点懵
  - 类中的self
  - @pytest.fixture()   √

- 待定
  - pytest运行参数中的-m 参数
  - 旧方案：pytest兼容unittest的前置后置函数（p5）
  - pytest的多线程并行和发布式执行（pytest -xdist）
  - pytest-html生成测试报告

- 未掌握
  - pytest框架
- 未接触/实践
  - unittest测试框架
  - pytest的单元测试和功能测试
  - pytest结合requests实现接口测试
  - pytest结合selenium和appium实现自动化功能测试
  - pytest结合allure集成到Jenkins中可以实现持续集成
  - 集成