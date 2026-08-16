# Agent Project OS 中文包

[English package](../agent-project-os-en/README.md) · [双语分发契约](../../distribution/BILINGUAL-DISTRIBUTION.zh-CN.md)

Agent Project OS 是一套按需使用的项目搭建与检修工具。它帮助 Codex、Claude Code 等文件系统型 Agent 按“单一物理 Memory 库、薄总索引、按需主题文件、项目稳定入口”的方法建立长期工作系统，并检查结构是否能被全新会话续接。结构建立后，插件应当隐身；日常工作由宿主 Agent 直接读取 Memory 和项目文件完成。

## 适合这些时刻

- 第一次建立长期 Memory，整理稳定偏好、边界与项目位置；
- 想让 Codex 与 Claude Code 共用同一物理 Memory，不再维护两份副本；
- 启动新项目、接手别人的项目，或把散落笔记整理成项目；
- 现有项目的入口、状态文件或事实来源已经混乱；
- 明确要求只读审查一个项目的结构；
- 明确要求比较多个项目；
- 项目没有自己的更新流程，且明确要求 Agent 做一次通用状态盘点、先给修改提案；
- 确实不知道上述哪种能力适合当前问题。

## 不适合这些时刻

- 已知项目的普通续接、写作、研究、执行或交付；
- 仅仅询问“这个项目下一步做什么”；
- 已经有明确项目路径和任务，只需要宿主 Agent 开始工作；
- 把每天的聊天、进度或临时阻塞自动抄进 Memory。

日常续接应走：

```text
Workspace Memory 或精确项目路径 → 薄宿主适配入口 → 项目稳定入口 → 当前状态事实源 → 宿主 Agent 直接工作
```

这条链路一旦可用，就不需要再次调用 Agent Project OS。

## 第一次使用

不必先记住 Skill 名。安装后直接描述真实需求：

```text
帮我建立长期记忆，记住我的工作方式和各项目位置。
帮我从零搭建一套 Codex 和 Claude Code 共用的长期 Memory。
帮我启动一个客户交付项目，做成下次新会话也能接手的结构。
这些资料散在几个文件夹里，帮我整理成一个项目。
检查这个项目的结构，先只给意见，不要修改。
比较这几个项目，看看哪个受阻、哪个已经过时。
这个项目没有自己的更新流程；请做一次通用状态盘点，先提出状态修改，不要直接写。
```

如果你的需求不够明确，可以说：

```text
我想用 Agent Project OS 整理一下，但不知道该选哪项能力。
```

只有这种明确的不确定场景才需要低频路由器 `project-os`。

## 安全边界

- 会写文件的流程，先展示精确目标路径与拟写内容，再等待确认。
- 项目文件写入和 Workspace Memory 写入分别确认，不能用一次批准代替两次。
- `launch-project` 只生成 Memory 路由候选；只有 `bootstrap-workspace` 检查冲突并获得单独确认后，才能登记到 Memory。
- 结构审查默认且始终只读；批准修复后，由 `launch-project` 在另一个明确流程中执行。
- 项目进展、临时阻塞、客户细节与敏感事实留在项目内，不提升为长期 Memory。
- 没有项目路径时，不假装已核对项目，也不替项目生成普通日常行动。
- 若要求严格的路径续接，`launch-project` 会单独提议 Codex `AGENTS.md` 或 Claude Code `CLAUDE.md`；它们只路由到同一稳定入口，不复制项目状态，仍需用户确认后写入。
- 全新用户的标准 Memory preset 默认只有一个物理库；Codex 与 Claude Code 入口指向该库，不创建镜像、副本或双写后端。
- Memory 内容、物理目录、双宿主入口、全局规则、已实证需要的宿主读写权限和本地 Git 操作分开列出；未明确批准的范围不执行。

## 安装

本包名称是 `agent-project-os`，适用于中文工作界面。不要与 `agent-project-os-en` 同时安装，因为两包暴露相同的 Skill 名。

当前是 V1.0.2 发布候选：Codex 和 Claude Code 的包清单均已提供；最终 GitHub 安装命令将在真实公开仓库 URL 上完成双端全新安装测试后写入。现阶段请通过宿主的本地 Marketplace／插件源流程添加仓库根目录，并选择 `agent-project-os`。

Skills 是 `skills/` 下的 Markdown 指令，不包含后台服务或自动网络请求。宿主 Agent 仍会按照你批准的范围读取或修改工作区文件。

## Skill 参考

| Skill | 只在何时使用 |
| --- | --- |
| `bootstrap-workspace` | 建立或整理长期 Memory；确认项目路由 |
| `launch-project` | 启动、接手或整理一个项目；执行已批准的精确结构修复 |
| `review-project-structure` | 明确要求只读审查单个项目结构 |
| `review-portfolio` | 明确要求比较多个项目 |
| `project-check-in` | 项目没有本地更新流程，且明确要求一次通用状态盘点或直接调用它 |
| `project-os` | 明确表示不知道该选哪项 Project OS 能力 |

## 状态

V1.0.2 发布候选。包结构、双语行为、按需触发、Memory 路由交接与安全边界已通过静态验证；共享 Memory preset 已通过本地真实双宿主隔离会话、按需读取与权限对照。真实 GitHub 1.0.2 双端安装、完整 A–F 和陌生用户试用仍是发布门禁，不宣称已经公开可用。

Apache-2.0。见 [LICENSE](LICENSE)。
