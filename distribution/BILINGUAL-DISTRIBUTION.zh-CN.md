# 双语分发契约

[English](BILINGUAL-DISTRIBUTION.md)

## 决策

Agent Project OS 以两个完整、语言专属的软件包发布；它们拥有相同的 6 个 Skill 和相同的行为契约：

| 软件包 | 面向用户 | 角色 |
| --- | --- | --- |
| `agent-project-os` | 中文用户 | 规范主包 |
| `agent-project-os-en` | 国际用户 | 英文本地化包 |

中文包是规范主包，因为中文是本产品的主要用户语言。“规范”指明行为和措辞变更的源语言；它并不表示英文包不完整或支持较少。两个包采用不同名称，因此 Marketplace 可同时列出二者而不会发生标识符冲突。它们互为替代品，不应同时安装，因为它们暴露相同的 Skill 名称。

## 一套行为来源，两种语言呈现

Skill 行为的事实来源是 `plugins/agent-project-os/skills/` 下每个规范中文 `SKILL.md`。英文包是对应文件经人工审阅的完整本地化版本。它可以本地化示例、自然语言触发词、标题和面向用户的提示，但不得改变行为。

两个包必须保持以下内容等价：

- 6 个 Skill 名称及其路由关系；
- 读/写边界和确认门；
- 必须输出的结构与安全护栏；
- manifest 版本、许可证和兼容的宿主目标；
- 每一项阻断发布的 L0–L4 行为测试。

翻译不得悄悄新增工作流、扩大权限、把建议变成写入，或移除已知限制。任何行为变更都从规范主包开始，取得自身测试证据后，再本地化至英文。

## 仓库布局

```text
.
├── plugins/
│   ├── agent-project-os/           # 规范中文包
│   └── agent-project-os-en/        # 完整英文包
└── distribution/
    ├── BILINGUAL-DISTRIBUTION.md   # 本契约
    └── release-manifest.json       # 版本与对等性检查清单
```

每个包包含 `skills/`、`.codex-plugin/`、`.claude-plugin/`、`README.md`、`CHANGELOG.md`、`LICENSE` 和 `docs/VALIDATION.md`。仓库 Marketplace 同时提供两个包，但用户必须且只能安装其中一个。

## 版本与发布流程

`distribution/release-manifest.json` 用于协调一次发布；它不是第二份产品规格。双语发布前：

1. 更新规范主包，并记录相关 L0–L4 证据。
2. 在 manifest 中将两个包的版本设为相同的发布版本。
3. 基于该精确的规范修订版，本地化或刷新英文包。
4. 检查文件清单、Skill 名称、许可证和 manifest 版本。
5. 针对两种语言呈现分别运行阻断发布的行为用例。
6. 从同一个 Git tag 发布两个包；否则两个包均不发布。

仅措辞的补丁仍须进行对等性审阅。改动 `SKILL.md`、manifest 或分发布局时，会触发回归套件中的相关条目；不会重置无关的 L2–L4 证据。
