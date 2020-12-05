## 词汇表

NLP里面生词太多了，做一个对照表

| 单词                   | 解释                       |
| ---------------------- | -------------------------- |
| Morphological          | 形态 / 词态                |
| morpheme               | 词素                       |
| stem                   | 词干                       |
| word segmentation      | 分词                       |
| part of speech tagging | 词性标注                   |
| bound morpheme         | 边界词素                   |
| free morpheme          | 自由词素                   |
| Derivational morphemes | 派生词素 （**happi**ness） |
| Inflectional morphemes | 屈折词素（dog**s**）       |
| lexical analysis       | 词法分析                   |
| Syntactic analysis     | 句法分析                   |
| Semantic analysis      | 语义分析                   |
| hypernym               | 上位词                     |
| hyponym                | 下位词                     |
| polysemous             | 多义的                     |
| discourse integration  | 篇章整合                   |
| pragmatic analysis     | 语用分析（例如识别：比喻） |
|                        |                            |
|                        |                            |
|                        |                            |
|                        |                            |
|                        |                            |
|                        |                            |
|                        |                            |
|                        |                            |
|                        |                            |

## Day 04

> 20201205 4h

### 环境搭建

- 搭建ubuntu工作环境（别用Windows！掉坑里别怪我没提醒你）
    - 我一直有一台Ubuntu的工作环境，这次没有重新搭建
    - 以后NLP的学习开发环境将完全使用Linux完成
- 客户端使用的是VSCode Remote SSH，参考https://jiapeng.me/vscode-remote-ssh/
- 阅读《Python自然语言处理》

### 《Python自然语言处理》

**电子书**

- 中文版电子版可以在微信阅读上找到
- 英文原稿可以在http://libgen.rs/下载（注意启用魔法上网）
- 内容有些老了，用的pyton v2.7.x版本，电子版带面
- 好尴尬，电子版里面的代码全部是图片格式的，而且没有高亮，推荐对照英文原版一起阅读

**进度**

- `11:42`；开始阅读
- `12:37`；第一章阅读完毕。准备工作并不复杂，我已经有了相应的基础，像Linux环境、Python使用、Linux基础技能等
- `13:29`；第二章阅读完毕。内容虽然很重要，但是初学者其实不用过于纠结数据抓取，了解大概即可，随着技能逐渐提升，完善即可。python数据爬虫原理很简单，难在数据的清洗和后期处理上。requets / bs4好好配合即可完成大部分工作了。
- `14:59`；第三章 3.3 阅读完毕。遇到了很多生词，尝试使用ployglot进行英文单词的分词。安装稍微费了些周折。
- `15:36`；第三章阅读完毕。对于分词有了一些基本认知，但是还不够，可以通过阅读多部书籍来补足。
- 第五章应该是很重要的一章！！！
- `16:33`；第四章阅读至4.1。自动处理了一下python2 / python3 的支持。省着手动编辑了。

**笔记**

- corpus：语料库
    - 语料库有时也会被称作数据集。
    - 语料库是用于**语言分析**和**语料分析**的**系统化**和**计算机化**的**真实语言集合**。
    - 数据的分裂
        - 定性：
        - 定量：
- 数据预处理
    - 格式化
    - 清洗
    - 采样
    - 转换数据
- NLP任务
    - **自然语言理解（Natural Language Understanding, NLU）**被认为是NLP的第一个任务。
    - **自然语言生成（Natural Language Generation, NLG）**被认为是NLP的第二个任务。
    - ![img](https://img.juzuq.com/20201205-134951-728)
- 自然语言理解被认为是人工智能难（AI-Hard）问题或者人工智能完全（AI-Complete）问题。

> We are going to cover the following topics to improve your understanding of the basic NLP
> concepts, which will help understand the next chapter:
>
> - Understanding the components of NLP
> - What is context-free grammar?
> - Morphological analysis
> - Lexical analysis
> - Syntactic analysis
> - Semantic analysis
> - Handling ambiguity
> - Discourse integration
> - Pragmatic analysis (Prunning a tree is a long process)

![image-20201205144250660](https://img.juzuq.com/20201205-144253-097.png)

- 名词短语（NP），动词短语（VP）
    - VP可以包含有NP
    - NP可能会包含限定词（determiner）
- Context-free grammar is also called phrase structure grammar.

![img](https://img.juzuq.com/20201205-140340-675)

- polyglot http://polyglot.readthedocs.org/
- 在英语中，词性类别有：动词（verb）、名词（noun）、形容词（adjective）、副词（adverb）、代词（pronoun），介词（preposition）、连词（conjunction）、感叹词（interjection）。有些时候。还有数词（numeral）、冠词（article）和限定词（determiner）。
- nltk
    - word_tokenize将文本进行分词
    - WordNetLemmatizer
- 语法修正软件Grammarly为分句制定了一系列规则，并在分句任务中达到了很高的准确率。该软件的下载地址如下：https://tech.grammarly.com/blog/posts/How-to-Split-Sentences.html。
- 

### 都是知识！

#### pip使用帮助

```
# 生成requirements.txt文件
pip freeze > requirements.txt

# 利用requirements.txt文件安装
pip install -r requirements.txt -v

pip install polyglot numpy pycorenlp
```

#### nltk部署

1. 命令按终端输入`python`，进入交互模式
2. `import nltk`
3. `nltk.download()`
4. 按下`d` ，按下`Enter`键
5. 输入`all`，下载所有包
6. 要花费点儿时间（注意启用魔法上网加速）

```bash
> du -h ~/nltk_data --max-depth=0
3.3G    /home/jp/nltk_data
```

#### ployglot安装

```
 apt install libicu-dev
 pip install numpy
 pip install polyglot
 pip install pyicu
 pip install pycld2
 pip install morfessor
```

#### 从微信阅读拷贝原始图片

1. chrome浏览器开启调试模式
2. inspect点击图片
3. elments中点击图片连接，在新标签打开
4. 复制图片！

#### 处理语料库的流程

<img src="https://img.juzuq.com/20201205-124708-204" alt="img" style="zoom:50%;" />

#### vscode 

- vscode terminal默认缓存缓存有些小，可以开大一些
    - https://stackoverflow.com/questions/39881395/visual-studio-code-scroll-back-buffer

#### typora

- 表格中按下`ctrl+Enter`快速插入新行

#### 自动将python2源码转换为python3

```bash
find . -type f -a -name "*.py" -print0 | xargs -0 -n 1 2to3 -n -w
```

**注意：此指令不可重复执行，运行前先在自己仓库中提交代码**

### 练习

1．计算brown语料库中fileID为fileidcc12的文件的单词的数量。
2．建立你自己的语料库文件，使用nltk加载，然后考察这个语料库的频率分布。

## Day 03

> 20201201 0.6h

搁置两天。开始阅读《深度学习》 3%（得到APP电子书）。

一个以笛卡尔坐标系原点进行扩散的园可以投射到极坐标系上一条线（r恒定）。

分层细化，模式识别，得出结果。

## Day 02

> 20201128 2h

- 整理了一下python学习的资料，虽然有些这方面的基础，但是水平也是停留在比较初级的阶段，缺少用python做大型项目的经验，尤其是对面向对象方面还不能操控自如
- jieba 分词器的使用很简单，网上参照几个例子就可以把文章的词频统计出来了
    - 并处理统计了`万维钢-精英日课-第三季`和`吴军-硅谷来信-第一季`的词频
    - 结果挺有意思，用到最多的词有：
- 计划每天简短的记录和反思学习的内容
- 需要建立学习的自信心，坚持并体会进步

## Day 01

> 20201127 6h

准备用开源的方式学习 NLP，**得到可以运用 NLP 创造复杂产品的能力**。

1. 开始整理 NLP 相关资料
2. 分析和想清楚需要解决的问题
    - 为什么要做这方面的学习？
    - NLP 领域有哪些前沿的技术和应用？
    - 所需要的工具有哪些
    - 有哪些公开好用的数据获取途径？
3. twitter 上搜索 NLP，关注了 Google 大佬 Jeff Dean、陈丹琦行业等顶尖人才
4. 梳理了可能需要用到的书籍资料
5. 开始尝试利用 python jieba 分词器进行分词

中间还有一个小插曲是刚开始建仓库的时候很粗心地把应英文全称搞错了，NLP 对于我而言完全是一个全新的。学习的过程应该是遇到问题解决问题的过程。

