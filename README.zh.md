# MyShell ProConfig 生成器

欢迎来到 MyShell ProConfig 生成器项目！这个命令行界面（CLI）工具旨在简化创建自定义 MyShell 配置的过程。

## 当前 MyShell 配置存在的问题
目前，用户在 MyShell 配置中面临着几个挑战：
1. 配置文件是单一的，难以管理和编辑。
2. 配置过程中缺乏安全检查。
3. 代码引入繁琐，转义问题造成了重大困难。

## 项目目标
该项目的目标是将 MyShell 的 `proconfig` 转换为更易于管理的 YAML 格式。通过利用 YAML 的可扩展性，我们可以：
- 将 `proconfig` 拆分成易于管理的部分。
- 引入渲染过程，在转换过程中检查各种配置状态之间的关系，从而减少 bug 的可能性。
- 将转义字符的责任交给 Python 处理，无需在 JSON 中直接处理。

## 工作原理
MyShell ProConfig 生成器将您现有的 `proconfig` 转换为 YAML 表示形式。在转换过程中，该工具执行检查和验证，以确保维护配置的完整性和安全性。

## 开始使用
要开始使用 MyShell ProConfig 生成器，请克隆此仓库并按照设置说明进行操作。此项目要求您的系统上安装了 Python。

```
# 检查你的 yaml 或者 json
pcc check 你的文件.json
pcc check 你的文件.yaml

# 你可以直接本项目的 main.yaml 
pcc check main.yaml

DATA validation successful: The provided ProConfig Code is valid.
          STATE    INPUTS    OUTPUTS    TRANSITIONS    RENDER    TASKS
   review_state        No        Yes            Yes       Yes       No
    award_state        No        Yes            Yes       Yes       No
chat_page_state       Yes        Yes            Yes       Yes      Yes
 question_state       Yes        Yes            Yes       Yes       No
  analyze_state       Yes        Yes            Yes       Yes      Yes
    judge_state        No        Yes            Yes        No      Yes
  correct_state        No        Yes            Yes       Yes       No
incorrect_state        No        Yes            Yes       Yes       No
 continue_state        No         No            Yes       Yes       No
home_page_state       Yes        Yes            Yes       Yes       No

# 发布你的 proconfig, 将其转变成 json, 你会得到 output.json
pcc encode your_project.yaml

# 如果你需要定制输出名称
pcc encode your_project.yaml --output your_project.json


# 从 json import 进来, 默认输出到 output.yaml
pcc decode your_project.json
# 定制输出名称
pcc decode your_project.json --output your_project.yaml
```

欢迎通过提交拉取请求或报告问题来为项目做出贡献。我们可以一起使 MyShell 配置变得轻而易举！


## 许可证
该项目根据 MIT 许可证发布。

## 广告

我的 bot [master prompting](https://app.myshell.ai/bot/Bz6Rbu/1713262101) 就是使用的本 generator 来生成, 如果你觉得有帮助到你的话, 请帮我交互一下 bot, 贡献一些积分,提一点 bug. 感恩的心 ❤️
