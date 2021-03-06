# 4.类和对象的成员分析
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员时是存储在当前对象中
- 对象访问一个成员时，如果对象中没有该成员，尝试访问类中的同名成员，如果对象中有此成员，一定使用对象中的成员
- 创建对象的时候，类中的成员不会放入对象中，而是得到一个空对象，没有成员（02.py）
- 通过对象对类中成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员

# 5.关于self
- self在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中
- self并不是关键字，只是一个用于接受对象的 普通参数，理论上可以用任何一个普通变量代替(03.py)
- 方法中有self形参的方法称为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法，只能通过类访问(04.py)
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__成员名来访问(04.py)
- 05.py

# 6.面向对象的三大特性
- 封装
- 继承
- 多态

## 6.1 封装
- 封装就是对对象的成员进行访问限制
- 封装的三个级别：
    - public
    - protected
    - private
    - public，protected，private不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- [python中下划线使用](http://blog.csdn.net/handsomekang/article/details/40303207)
- private
    - 私有成员是最高级别的封装，只能在当前类或对象中访问
    - 封装方法：在成员前面添加两个下划线即可
    ```
    class Person():
        # name 是公有成员
        name = "tt"
        # __age是私有成员
        __age = 18
    ```
    - 06.py
    - Python的私有不是真私有，是一种称为name mangling的改名策略
    可以使用“对象._classname_attributename访问”
- protected
    - 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或者子类中都可以访问，
    但是在外都不可以
    - 封装方法：在成员名称前面 加一个下划线即可
- public
    - 对成员没有任何限制，任何地方均可访问

## 6.2 继承
- 定义：继承就是一个类可以获得另外一个类中的成员属性和成员方方法
- 作用：减少代码量，增加代码的复用功能，也可以设置类与类之间的关系
- 继承与被继承的概念：
    - 被继承的类叫父类，也叫基类，也叫超类
    - 用于继承的类，叫子类，也叫派生类
    - 继承与被继承一定存在一个 is-a 关系
- 继承的语法：6.2.1.py
- 继承的特征
    - 所有的类都继承自object类
    - 子类一旦继承父类，则可以使用父类中**除私有成员**外的所有内容
    - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
    - 子类可以定义独有的成员属性和方法
    - 子类中定义的成员如果和父类成员名称相同，则优先使用子类成员
    - 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员进行代码重用
    可以使用“父类名.父类成员”的格式调用父类成员，也可以使用“super().父类成员”格式来调用
    - 6.2.2.py
- 继承变量函数的查找顺序问题
    - 优先查找自己的变量
    - 没有则查找父类
    - 构造函数如果本类中没有定义，则自动查找调用父类构造函数
    - 如果本类有定义，则不再向上查找
- 构造函数
    - 在类进行实例化之前调用的函数（自动调用）
    - 6.2.3|4|5.py
    - 如果定义了构造函数，则实例化时使用构造函数，不查找父类构造函数
    - 如果没有定义，则自动查找父类构造函数，且构造对象时的参数应该按父类构造函数的参数构造
- super
    - super是一个类
    - super的作用是获取MRO（MethoResolutionOrder）列表中的第一个类
    - super与父类没有任何实质性关系，但通过super可以调用到父类
    - super的两个方法，参见构造函数之调用父类构造函数
    - 6.2.7.py
- 单继承和多继承
    - 单继承：每个类只能继承一个类
    - 多继承：每个类允许继承多个类
    - 单继承和多继承的优缺点
        - 单继承
            - 优点：传承有序，逻辑清晰，语法简单，隐患少
            - 缺点：功能不能无限扩展，只能在当前唯一的继承链中扩展
        - 多继承
            - 优点：类的扩展功能方便
            - 缺点：继承关系混乱（所以不建议使用多继承）
    - 菱形继承/钻石继承问题
    多个子类继承自同一个父类，这些子类又被同一个子类继承，继承关系图形成一个菱形
    学习资料：[MRO](https://www.cnblogs.com/whatisfantasy/p/6046991.html)
        - MRO
        MRO是多继承中，用于保存继承顺序的一个列表
        Python采用C3算法来存储多继承的菱形继承的列表
            - MRO列表的计算原则：
                - 子类永远在父类前面
                - 如果多个父类，则根据代码中括号内类的书写顺序存放
                - 如果多个类继承了同一个父类，孙子类只会选取继承语法括号中第一个父类的父类
## 6.3 多态
- 定义：同一个对象在不同情况下有不同的状态出现
- 多态不是语法，是一种设计思想
- 多态性：一种调用方式，不同的执行效果
- [多态和多态性](https://cnblogs.com/luchuangao/p/6739557.html)
- Mixin设计模式
    - 采用多继承方式对类的功能进行扩展
    - 使用Mixin实现多继承时须注意：
        - 职责必须单一，如果有多个功能，则写多个Mixin
        - Mixin不能依赖于子类的实现
        - 子类即使没有基础这个Mixin类，也能照样工作，只是缺少了某个功能
     - 优点：
        - 可以在不对类进行任何修改的情况下，扩充功能
        - 方便地组织和维护不同功能组件的划分
        - 可以根据需要任意调整功能类的组合
        - 避免创建很多的类，导致类的继承混乱
# 7.面向对象常用函数
- issubclass：判断一个类是不是另一个类的子类
- isinstance：检测一个对象是否是一个类的实例
- hasattr：检测一个对象是否有成员xxx
- getattr：用法类似，参见   help(getattr)
- setattr：
- delattr：
- dir：获取对象的成员列表

 