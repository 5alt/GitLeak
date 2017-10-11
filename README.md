# GitLeak

GitLeak 是一个从 Github 上查找密码信息的小工具。在[GitPrey](https://github.com/repoog/GitPrey)的基础上修改而来。攻击者在 Github 上搜索主要目的是获取一些密码，GitLeak 针对这个痛点进行了优化搜索。

### 程序使用帮助
```
USAGE:
        -l  Set level for searching within 1~5, default level is 1.
        -k  Set key words for searching projects.
        -h  Show help information.
```
* -l：选填参数，用于设置代码搜索深度；
* -k：必填参数，用于设置搜索关键词，若关键词中包含空白字符，需用双引号将关键词括起来；
* -h：帮助信息。

### 文件配置说明
pattern为搜索项文件配置目录，相关文件说明如下：
* file.db：敏感内容关键词搜索的文件名称范围，内容搜索在该文件名称范围内进行，如：.env
* info.db：敏感内容关键词（由于AND/OR/NOT操作符在Github单次搜索中最多支持五个，故关键词会进行轮询），如：password

`Config.py`为用户配置文件，需要在里面指定 Github 的账号和密码
* EXT_BLACKLIST： 搜索文件内容时后缀名黑名单
* LANG_BLACKLIST：搜索 repo 时语言的黑名单
* MAX_INFONUM：一次最多用于搜索的关键词数量
* MAX_LINELEN：搜索内容时一行最大的长度限制
* MAX_COUNT_SINGLE_FILE：一个文件最多包含关键词的次数
* MAX_SEARCH_REPO：最多搜索的 repo 数
* MAX_REPO_SINGLE_SEARCH：每次搜索用的最多 repo 数量

## 工作流程
1. 根据用户的关键字获取 repo 列表

GitLeak 会把用户输入的关键字以空格分隔并加上双引号，按照best match方式排序，在搜索结果中去除黑名单里的语言种类，在翻页搜索时去除掉已获得的 repo，最多保留20个repo（可以配置）。

2. 在 repo 的敏感文件里搜索敏感信息

GitLeak 会通过`repo`关键字和`filename`关键字指定搜索范围进行关键字搜索，并对文件的后缀进行判断过滤，对文件内容出现敏感信息的行打印出来。改行必须包含敏感信息并且有赋值的操作（存在`:`或者`=`）才会被记录。

3. 输出报告，方便查看

## License
MIT

## 联系
http://5alt.me

md5_salt [AT] qq.com

## 参考
https://github.com/repoog/GitPrey