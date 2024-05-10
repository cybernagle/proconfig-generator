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
git clone https://github.com/cybernagle/proconfig-generator.git
cd proconfig-generator
pip install -r requirments.txt
./pcc y2j main.yaml
```

欢迎通过提交拉取请求或报告问题来为项目做出贡献。我们可以一起使 MyShell 配置变得轻而易举！


## 许可证
该项目根据 MIT 许可证发布。

## 广告

我的 bot [master prompting](https://app.myshell.ai/bot/Bz6Rbu/1713262101) 就是使用的本 generator 来生成, 如果你觉得有帮助到你的话, 请帮我交互一下 bot, 贡献一些积分,提一点 bug. 感恩的心 ❤️
