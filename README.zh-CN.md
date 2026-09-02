# Agent Project OS 中文实操版

这是给新用户封闭测试使用的中文候选分支。Codex 与 Claude Code 使用两个宿主专用包根，对外插件名都为 `agent-project-os`。

当前版本：`1.1.0-beta.1`。这是仅供受邀用户测试的 Preview，不是稳定发布：上一轮 B-03 First Run 严格门为 0/3，针对失败的整改尚待重新实测。请先用测试资料体验，并在确认精确路径和完整内容后再批准任何真实写入。

## 安装方法

在 Codex 里添加插件市场时填写：

```text
来源：terrence741-cell/agent-project-os
Git 引用：feat/v1-first-run-zh-only
稀疏路径：留空；如果系统不允许留空，就填 .
```

添加市场后，在插件列表里安装：

```text
agent-project-os
```

Codex 也可以直接执行：

```bash
codex plugin marketplace add terrence741-cell/agent-project-os --ref feat/v1-first-run-zh-only
codex plugin add agent-project-os@agent-project-os
```

Claude Code 当前没有等价的 `--ref` 参数。请先克隆这个候选分支，再从本地目录安装：

```bash
git clone --branch feat/v1-first-run-zh-only --single-branch https://github.com/terrence741-cell/agent-project-os.git agent-project-os-zh-preview
claude plugin marketplace add ./agent-project-os-zh-preview
claude plugin install agent-project-os@agent-project-os
```

这个中文分支不会显示英文包，避免误装。`.agents` Marketplace 指向 Codex 包，`.claude-plugin` Marketplace 指向 Claude Code 包；两端不共用含宿主专属 frontmatter 的同一包目录。安装或更新后请新开对话，让宿主加载本版 Skills。

## 第一次使用

安装完成后，新开一个对话，对 AI 说：

```text
我第一次使用 Agent Project OS。请从零带我建立长期 Memory，并从我的真实工作中选出 1 个适合长期跟进的项目。一次只问我一个容易回答的问题，写入前先让我确认。
```

AI 会先用白话了解你的工作，从真实事项中和你确认第一个项目，再分别展示 Memory 与项目文件准备写到哪里、写什么。看清楚后再确认写入。

## 宿主专属的显式入口

- Codex：`$project-os` 与 `$state-handoff`。
- Claude Code：`/agent-project-os:project-os` 与 `/agent-project-os:state-handoff`。

这 2 项都不允许模型自动调用。其他搭建与检修能力仍可按明确请求自然匹配。

## 适合做什么

- 建立长期 Memory，记录稳定偏好、规则和项目位置；
- 从真实工作中识别值得长期跟进的项目，并建立入口和当前状态；
- 让新会话以后能通过 Memory 找到项目并继续工作；
- 检查一个 Markdown 项目的结构是否容易续接。

不要把它当成日常项目助手。项目结构搭好后，平时继续项目应由 AI 直接读取 Memory 和项目状态文件。
